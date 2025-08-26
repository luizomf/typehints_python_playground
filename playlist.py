# pyright: reportMissingTypeStubs=false
import json
import re
from collections.abc import MutableMapping
from dataclasses import asdict, dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import TypedDict

from ffmpeg import probe

RE_VIDEO_SEQUENCE = re.compile(r"(Aula)\s*(\d+)", re.IGNORECASE | re.DOTALL)
RE_DIGIT = re.compile(r"\d+")


@dataclass
class VideoInfo:
    original_path: Path  # This is the file found for the first time
    real_filepath: Path  # This is the real file that should be used

    duration_seconds: float
    duration_hhmmss: str

    video_title: str
    sequence: str | None = None

    def to_dict(self) -> MutableMapping[str, str]:
        return asdict(self)


class VideoInfoDict(TypedDict):
    original_path: str  # This is the file found for the first time
    real_filepath: str  # This is the real file that should be used

    duration_seconds: float
    duration_hhmmss: str

    video_title: str
    sequence: str | None


def seconds_to_hhmmss(seconds: float) -> str:
    duration_hhmmss = datetime(1, 1, 1, 0, 0, 0, tzinfo=UTC) + timedelta(
        seconds=seconds,
    )
    return duration_hhmmss.strftime("%H:%M:%S")


def hhmmss_to_seconds(hhmmss: str) -> float:
    expected_time_parts = 3
    time_parts = hhmmss.split(":")
    assert len(time_parts) == expected_time_parts, "Use HH:MM:SS for time format"

    total_seconds = 0
    multiplier = 1
    reversed_time_parts = reversed(time_parts)

    for time_part in reversed_time_parts:
        float_part = float(time_part)
        total_seconds += float_part * multiplier

        multiplier *= 60

    return total_seconds


def get_aivideocut_child(input_path: Path) -> Path | None:
    resolved_path = input_path.resolve()
    filename = resolved_path.stem
    extension = resolved_path.suffix
    child_directory = resolved_path.with_name(f"{filename}_{extension[1:]}")

    if not child_directory.is_dir():
        return None

    final_video = child_directory / "04_FINAL.mp4"

    if not final_video.is_file():
        return None

    return final_video


def get_video_sequence(input_path: Path) -> tuple[str, str] | None:
    resolved_path = input_path.resolve()
    filename = resolved_path.stem

    sequence = RE_VIDEO_SEQUENCE.search(filename)

    if sequence:
        sequence_name, sequence_number, *_ = sequence.groups()
        return sequence_name, sequence_number

    return None


def create_video_info(
    input_directory: Path,
) -> tuple[list[VideoInfo], list[VideoInfoDict]]:
    resolved_dir_path = input_directory.resolve()

    assert resolved_dir_path.is_dir(), "Input must be a directory"

    allowed_extensions = ".mp4", ".mov", ".mkv"
    video_infos: list[VideoInfo] = []
    video_info_dicts: list[VideoInfoDict] = []

    for file in resolved_dir_path.iterdir():
        if not file.is_file():
            continue  # not a file

        if not file.suffix.lower().endswith(allowed_extensions):
            continue  # extension not allowed

        real_filepath = get_aivideocut_child(file)

        if not real_filepath:
            real_filepath = file

        print(f"Probe: {file.name!r}")
        video_probe_info = probe(real_filepath)
        duration_seconds = float(video_probe_info["format"]["duration"])
        duration_hhmmss = seconds_to_hhmmss(duration_seconds)
        video_title = file.stem

        video_sequence_re = get_video_sequence(file)
        video_sequence = None
        sequence_number = ""

        if video_sequence_re:
            _, sequence_number, *_ = video_sequence_re
            video_sequence = f"{sequence_number:0>4}"

        video_infos.append(
            VideoInfo(
                original_path=file,
                real_filepath=real_filepath,
                duration_seconds=duration_seconds,
                duration_hhmmss=duration_hhmmss,
                video_title=video_title,
                sequence=video_sequence,
            ),
        )

        video_info_dicts.append(
            VideoInfoDict(
                original_path=str(file),
                real_filepath=str(real_filepath),
                duration_seconds=duration_seconds,
                duration_hhmmss=duration_hhmmss,
                video_title=video_title,
                sequence=video_sequence,
            ),
        )

    video_infos.sort(
        key=lambda v: v.sequence or v.video_title or v.original_path.name,
    )

    video_info_dicts.sort(
        key=lambda v: v.get("sequence")
        or v.get("video_title")
        or v.get("original_path"),
    )
    return video_infos, video_info_dicts


def main() -> None:
    input_dir = Path("/Users/luizotavio/Desktop/html_ready")
    result_json = input_dir / "video_info.json"
    output_dir = Path("/Users/luizotavio/Desktop/html_out")
    concat_file = output_dir / "concat.txt"
    chapters_file = output_dir / "chapters.txt"

    video_infos, video_info_dicts = create_video_info(input_dir)

    with result_json.open("w", encoding="utf8") as file:
        json.dump(video_info_dicts, file, indent=2)

    output_dir.mkdir(parents=True, exist_ok=True)
    concat_content = ""
    total_duration = 0
    chapters_content = ""

    for video in video_infos:
        out_video = output_dir / f"{video.sequence}{video.real_filepath.suffix}"

        # Uncomment this to copy file
        out_video.write_bytes(video.real_filepath.read_bytes())

        concat_content += f"file '{out_video.name}'\n"
        chapters_content += (
            f"{seconds_to_hhmmss(total_duration)} - {video.video_title}\n"
        )

        print("Processing video:", out_video.name)
        total_duration += video.duration_seconds

    print()
    print("Total Duration:", seconds_to_hhmmss(total_duration))
    print()
    print(chapters_content)

    # Uncomment this to create concat file
    concat_file.write_text(concat_content)
    chapters_file.write_text(chapters_content)

    ffmpeg_command = (
        f"cd {output_dir}\n"
        "ffmpeg -f concat -safe 0 -i concat.txt -c:v libx264 -preset fast "
        "-crf 18 -c:a aac -b:a 320k "
        "-movflags +faststart -fflags +genpts FINAL.mp4 -y\n"
    )
    print("Tudo pronto... Agora execute os comandos abaixo:\n")
    print(ffmpeg_command)


if __name__ == "__main__":
    main()
