# pyright: reportMissingTypeStubs=false
from collections.abc import MutableMapping
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path


@dataclass
class VideoInfo:
    original_path: Path  # This is the file found for the first time
    real_filepath: Path  # This is the real file that should be used
    output_filepath: Path  # This is where to send the file after done

    duration_seconds: float
    duration_hhmmss: str

    video_title: str
    sequence: str  # if it is a sequence, it is better to use 001, 002, 003, etc

    def to_dict(self) -> MutableMapping[str, str]:
        return {k: str(v) if isinstance(v, Path) else v for k, v in vars(self).items()}


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


def main() -> None:
    input_dir = Path("/Users/luizotavio/Desktop/deleteme")

    # ffmpeg_command = (
    #     f"cd {input_dir}\n"
    #     "ffmpeg -f concat -safe 0 -i concat.txt -c:v libx264 -preset fast "
    #     "-crf 18 -c:a aac -b:a 320k "
    #     "-movflags +faststart -fflags +genpts FINAL.mp4 -y\n"
    # )
    # print("\nTudo pronto... Agora execute os comandos abaixo:\n")
    # print(ffmpeg_command)


if __name__ == "__main__":
    main()
