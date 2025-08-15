# pyright: reportMissingTypeStubs=false
from collections.abc import Callable, MutableSequence
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import overload

from ffmpeg import probe  # pyright: ignore[reportUnknownVariableType]

from utils import logger


@dataclass
class VideoInfo:
    filename: str
    extension: str
    path: Path
    duration_seconds: float
    duration_hhmmss: str

    # Used when renaming video files
    original_path: Path | None = None
    original_filename: str = ""
    was_renamed: bool = False

    # Used to flag videos that must be reencoded
    needs_reencode: bool = False

    def __post_init__(self) -> None:
        if not self.original_filename:
            self.original_filename = self.filename

        if self.original_path is None:
            self.original_path = self.path

        if self.filename != self.original_filename:
            self.was_renamed = True


@overload
def get_video_filepaths[T, R](
    input_dir: T,
    extensions: tuple[str, ...] = ("mp4", "mkv", "mov"),
    *,
    callback: Callable[[T], R],
) -> MutableSequence[R]: ...
@overload
def get_video_filepaths[T](
    input_dir: T,
    extensions: tuple[str, ...] = ("mp4", "mkv", "mov"),
    *,
    callback: None = None,
) -> MutableSequence[T]: ...
def get_video_filepaths[T, R](
    input_dir: T,
    extensions: tuple[str, ...] = ("mp4", "mkv", "mov"),
    *,
    callback: Callable[[T], R] | None = None,
) -> MutableSequence[T] | MutableSequence[R]:
    assert isinstance(input_dir, Path), "Input directory is not a Path"

    in_dir = input_dir.resolve()
    assert in_dir.is_dir(), "Input path is not a directory"

    filepaths: list[T] = []
    video_infos: list[R] = []

    logger.info(f"Trying to traverse files in: {in_dir}")
    for file in in_dir.iterdir():
        ext = file.suffix

        if not ext.endswith(extensions):
            continue

        if callback:
            logger.debug(f"Using callback {callback.__name__!r} for {file.name!r}")
            video_infos.append(callback(file))

        filepaths.append(file)

    if video_infos:
        return video_infos

    return filepaths


def create_videoinfo(video_path: Path) -> VideoInfo:
    logger.debug(f"Creating video information for: {video_path.name!r}")
    probe_data = probe(video_path)

    assert probe_data["format"]["duration"], "Could not find video duration"

    duration_seconds = float(probe_data["format"]["duration"])
    duration_hhmmss = seconds_to_hhmmss(duration_seconds)

    return VideoInfo(
        filename=video_path.name,
        extension=video_path.suffix,
        path=video_path.resolve(),
        duration_seconds=duration_seconds,
        duration_hhmmss=duration_hhmmss,
    )


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
    logger.setLevel("INFO")

    input_dir = Path("/Users/luizotavio/Desktop/videos")
    videos = sorted(
        get_video_filepaths(
            input_dir,
            ("mp4",),
            callback=create_videoinfo,
        ),
        key=lambda v: v.filename,
    )

    logger.info(videos[0])


if __name__ == "__main__":
    main()
