"""
thumbhunter.py — garimpa frames nítidos e diversos para thumbnails de YouTube.

Requisitos:
  pip install opencv-python pillow imagehash numpy

Exemplos:
  # Pega frames nos primeiros 120s, guarda as top 12 thumbs
  python thumbhunter.py --video input.mp4 --start 0 --duration 120 --top-k 12

  # Varre de 30s a 150s, amostrando a cada 0.15s, evita duplicatas mais agressivo
  python thumbhunter.py --video input.mp4 --start 30 --duration 120 --step 0.15 --min-hash-distance 12

  # Só salva frames com nitidez alta e exposição ok
  python thumbhunter.py --video input.mp4 --sharpness-th 120.0 --min-bright 25 --max-bright 230
"""

from __future__ import annotations

import argparse
import csv
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

import cv2
import imagehash
import numpy as np
from PIL import Image


@dataclass
class FrameInfo:
    t_sec: float
    frame_idx: int
    sharpness: float
    brightness: float
    path: Path
    phash: imagehash.ImageHash


def variance_of_laplacian(gray: np.ndarray) -> float:
    # medida clássica de nitidez (quanto maior, mais detalhe / menos borrado)
    return float(cv2.Laplacian(gray, cv2.CV_64F).var())


def mean_brightness(gray: np.ndarray) -> float:
    # média simples em [0..255]
    return float(np.mean(gray))


def compute_phash(bgr: np.ndarray) -> imagehash.ImageHash:
    # usa pHash 8x8 (64 bits) via Pillow
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(rgb)
    return imagehash.phash(img, hash_size=8)


def hamming_distance(a: imagehash.ImageHash, b: imagehash.ImageHash) -> int:
    return int(a - b)


def is_diverse(
    new_hash: imagehash.ImageHash,
    selected: Iterable[FrameInfo],
    min_dist: int,
) -> bool:
    for s in selected:
        if hamming_distance(new_hash, s.phash) < min_dist:
            return False
    return True


def format_tc(t: float) -> str:
    m, s = divmod(int(round(t)), 60)
    h, m = divmod(m, 60)
    return f"{h:02d}-{m:02d}-{s:02d}"


def main() -> None:
    ap = argparse.ArgumentParser(
        prog="thumbhunter",
        description="Extrai frames nítidos e NÃO repetidos para thumbnails.",
    )
    ap.add_argument(
        "--video",
        required=True,
        type=Path,
        help="Arquivo de vídeo (ex.: .mp4)",
    )
    ap.add_argument(
        "--outdir",
        type=Path,
        default=Path("thumbhunter_out"),
        help="Diretório de saída",
    )
    ap.add_argument(
        "--start",
        type=float,
        default=0.0,
        help="Início (segundos) do intervalo a analisar",
    )
    ap.add_argument(
        "--duration",
        type=float,
        default=120.0,
        help="Duração (segundos) a partir de --start",
    )
    ap.add_argument(
        "--step",
        type=float,
        default=0.2,
        help="Intervalo entre amostras (s). 0.1–0.25 é bom",
    )
    ap.add_argument(
        "--sharpness-th",
        type=float,
        default=80.0,
        help="Limiar mínimo de nitidez (variance of Laplacian)",
    )
    ap.add_argument(
        "--min-bright",
        type=float,
        default=10.0,
        help="Brilho mínimo aceito (0..255)",
    )
    ap.add_argument(
        "--max-bright",
        type=float,
        default=245.0,
        help="Brilho máximo aceito (0..255)",
    )
    ap.add_argument(
        "--top-k",
        type=int,
        default=12,
        help="Quantos frames finais salvar (após dedupe)",
    )
    ap.add_argument(
        "--min-hash-distance",
        type=int,
        default=10,
        help="Hamming distance mínima entre pHashes (8x8 -> 0..64)",
    )
    ap.add_argument(
        "--jpeg-quality",
        type=int,
        default=96,
        help="Qualidade JPEG ao salvar (0..100)",
    )
    ap.add_argument(
        "--prefix",
        type=str,
        default="thumb",
        help="Prefixo do arquivo de saída",
    )
    ap.add_argument(
        "--save-all-candidates",
        action="store_true",
        help="Opcional: salva todos os candidatos (brutos)",
    )
    args = ap.parse_args()

    assert args.video.exists(), f"Arquivo não encontrado: {args.video}"
    args.outdir.mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(str(args.video))
    if not cap.isOpened():
        raise SystemExit(f"Não consegui abrir: {args.video}")

    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
    duration_video = (
        (total_frames / fps)
        if total_frames > 0
        else float(cap.get(cv2.CAP_PROP_POS_MSEC))
    )

    t0 = max(0.0, args.start)
    t1 = min(duration_video, t0 + max(0.1, args.duration))
    step = max(1.0 / fps, args.step)

    # Pula direto para t0
    cap.set(cv2.CAP_PROP_POS_MSEC, t0 * 1000.0)

    candidates: list[FrameInfo] = []
    t = t0
    next_msec = t0 * 1000.0

    while t <= t1:
        cap.set(cv2.CAP_PROP_POS_MSEC, next_msec)
        ok, frame = cap.read()
        if not ok:
            break

        frame_idx = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        # cinza p/ métricas
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        sharp = variance_of_laplacian(gray)
        bright = mean_brightness(gray)

        # filtros básicos: nitidez e exposição
        if sharp >= args.sharpness_th and (
            args.min_bright <= bright <= args.max_bright
        ):
            ph = compute_phash(frame)

            # salva um JPG temporário (opcional) pra inspecionar os candidatos
            out_tmp = (
                args.outdir / f"{args.prefix}_cand_{format_tc(t)}_{frame_idx:06d}.jpg"
            )
            if args.save_all_candidates:
                cv2.imwrite(
                    str(out_tmp),
                    frame,
                    [int(cv2.IMWRITE_JPEG_QUALITY), args.jpeg_quality],
                )

            # guarda só metadados por enquanto; imagem final será salva depois
            candidates.append(
                FrameInfo(
                    t_sec=t,
                    frame_idx=frame_idx,
                    sharpness=sharp,
                    brightness=bright,
                    path=out_tmp,
                    phash=ph,
                ),
            )

        # avança
        t += step
        next_msec += step * 1000.0

    cap.release()

    # ordena por nitidez (desc) e faz dedupe por pHash
    candidates.sort(key=lambda x: x.sharpness, reverse=True)
    selected: list[FrameInfo] = []
    for c in candidates:
        if is_diverse(c.phash, selected, args.min_hash_distance):
            selected.append(c)
        if len(selected) >= args.top_k:
            break

    # reabrir vídeo para resgatar exatamente esses frames em full qualidade
    cap = cv2.VideoCapture(str(args.video))
    if not cap.isOpened():
        raise SystemExit(f"Falha reabrindo vídeo: {args.video}")

    meta_rows = []
    for i, s in enumerate(selected, start=1):
        cap.set(
            cv2.CAP_PROP_POS_FRAMES,
            max(0, s.frame_idx - 1),
        )  # um passo antes ajuda a pegar o exato
        ok, frame = cap.read()
        if not ok:
            continue

        out_name = f"{args.prefix}_{i:02d}_{format_tc(s.t_sec)}_{s.frame_idx:06d}.jpg"
        out_path = args.outdir / out_name
        cv2.imwrite(
            str(out_path),
            frame,
            [int(cv2.IMWRITE_JPEG_QUALITY), args.jpeg_quality],
        )

        s.path = out_path
        meta_rows.append(
            {
                "rank": i,
                "time_sec": round(s.t_sec, 3),
                "timecode": format_tc(s.t_sec),
                "frame_idx": s.frame_idx,
                "sharpness": round(s.sharpness, 2),
                "brightness": round(s.brightness, 2),
                "file": out_path.name,
            },
        )

    cap.release()

    # salva CSV com metadados
    csv_path = args.outdir / f"{args.prefix}_metadata.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "rank",
                "time_sec",
                "timecode",
                "frame_idx",
                "sharpness",
                "brightness",
                "file",
            ],
        )
        writer.writeheader()
        writer.writerows(meta_rows)

    print(f"\nVídeo: {args.video}")
    print(f"Janela analisada: {t0:.2f}s → {t1:.2f}s | step={step:.3f}s | fps≈{fps:.3f}")
    print(
        f"Candidatos válidos: {len(candidates)} | Selecionados (diversos): {len(selected)}",
    )
    print(f"Saída: {args.outdir.resolve()}")
    if meta_rows:
        best = meta_rows[0]
        print(f"Top 1: {best['file']} @ {best['timecode']} (sharp={best['sharpness']})")


if __name__ == "__main__":
    main()

"""
 rm -Rf /Users/luizotavio/Desktop/FOTOS/ ; \
 clear ; \
 uv run --no-project --with opencv-python --with pillow --with imagehash \
 --with numpy thumbhunter.py \
 --video /Users/luizotavio/Desktop/FOTOS.mp4 \
 --start 0 --duration 300 --step 0.5 --sharpness-th 80 --min-bright 50 \
 --max-bright 200 --top-k 16 --min-hash-distance 8 --save-all-candidates \
 --outdir /Users/luizotavio/Desktop/FOTOS/
"""
