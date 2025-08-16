# pyright: reportMissingTypeStubs=false
import json
from collections.abc import Callable, MutableMapping, MutableSequence
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import overload

from ffmpeg import probe  # pyright: ignore[reportUnknownVariableType]


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

    # Additional information (whatever you need)
    aivideocut_path: Path | None = None

    def __post_init__(self) -> None:
        if not self.original_filename:
            self.original_filename = self.filename

        if self.original_path is None:
            self.original_path = self.path

        if self.filename != self.original_filename:
            self.was_renamed = True

    def to_dict(self) -> MutableMapping[str, str]:
        return {k: str(v) if isinstance(v, Path) else v for k, v in vars(self).items()}


@overload
def get_video_filepaths[T, R](
    input_dir: T,
    extensions: tuple[str, ...] = ("mp4", "mkv", "mov"),
    *,
    create_json: bool,
    create_concat_file: bool,
    callback: Callable[[T], R],
) -> MutableSequence[R]: ...
@overload
def get_video_filepaths[T](
    input_dir: T,
    extensions: tuple[str, ...] = ("mp4", "mkv", "mov"),
    *,
    create_json: bool,
    create_concat_file: bool,
    callback: None = None,
) -> MutableSequence[T]: ...
def get_video_filepaths[T, R](
    input_dir: T,
    extensions: tuple[str, ...] = ("mp4", "mkv", "mov"),
    *,
    create_json: bool = False,
    create_concat_file: bool = False,
    callback: Callable[[T], R] | None = None,
) -> MutableSequence[T] | MutableSequence[R]:
    assert isinstance(input_dir, Path), "Input directory is not a Path"

    in_dir = input_dir.resolve()
    assert in_dir.is_dir(), "Input path is not a directory"

    filepaths: list[T] = []
    video_infos: list[R] = []

    for file in in_dir.iterdir():
        ext = file.suffix

        if not ext.endswith(extensions):
            continue

        if callback:
            video_infos.append(callback(file))

        filepaths.append(file)

    if video_infos:
        if create_json:
            video_infos = sorted(video_infos, key=lambda v: getattr(v, "filename", ""))
            json_file = in_dir / "video_info.json"
            json_data = [v.to_dict() for v in video_infos if isinstance(v, VideoInfo)]

            with json_file.open("w", encoding="utf8") as file:
                json.dump(json_data, file, indent=2)

        if create_concat_file:
            concat_file = in_dir / "concat.txt"
            concat_data = "\n".join(
                [
                    f"file {v.filename!r}"
                    for v in video_infos
                    if isinstance(v, VideoInfo)
                ],
            )

            with concat_file.open("w", encoding="utf8") as file:
                file.write(concat_data)

        return video_infos

    return filepaths


def create_videoinfo(video_path: Path) -> VideoInfo:
    probe_data = probe(video_path)

    assert probe_data["format"]["duration"], "Could not find video duration"

    duration_seconds = float(probe_data["format"]["duration"])
    duration_hhmmss = seconds_to_hhmmss(duration_seconds)

    aivideocut_path = video_path.parent / video_path.name.replace(".", "_")
    aivideocut_final = aivideocut_path / "04_FINAL.mp4"

    if not aivideocut_final.is_file():
        aivideocut_path = None

    return VideoInfo(
        filename=video_path.name,
        extension=video_path.suffix,
        path=video_path.resolve(),
        duration_seconds=duration_seconds,
        duration_hhmmss=duration_hhmmss,
        aivideocut_path=aivideocut_path,
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


def copy_aivideocut_final(
    videos: MutableSequence[VideoInfo],
    output_dir: Path,
    *,
    delete_originals: bool = False,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    for video in videos:
        assert video.aivideocut_path, "Video does not have aivideocut_path"

        new_video = output_dir / f"{video.path.stem}{video.extension}"

        final_video_name = f"04_FINAL{video.extension}"
        final_video = video.aivideocut_path / final_video_name

        assert final_video.is_file(), f"Video does not have a {final_video_name!r}"

        new_video.write_bytes(final_video.read_bytes())

        final_video_stat = final_video.stat()
        new_video_stat = new_video.stat()

        assert new_video_stat.st_size == final_video_stat.st_size, (
            "Fail to copy video data"
        )

        if delete_originals:
            for file in video.aivideocut_path.iterdir():
                if file == new_video:
                    continue

                file.unlink()


def create_youtube_chapters(json_file: Path) -> None:
    with json_file.open("r", encoding="utf8") as file:
        video_info = json.load(file)

    total_duration = 0
    chapters_timestamp: list[tuple[str, str]] = []
    for info in video_info:
        chapters_timestamp.append(
            (seconds_to_hhmmss(total_duration), Path(info.get("filename")).stem),
        )
        total_duration += float(info.get("duration_seconds", 0))

    for chapter, video in chapters_timestamp:
        print(chapter, video)


def main() -> None:
    # THIS SECTION TAKES INTO ACCOUNT THE USE OF AIVIDEOCUT
    # Input files made with aivideocut
    # input_dir = Path("/Users/luizotavio/Desktop/deleteme")

    # Output files from aivideocut (could be skipped)
    # aivideocut_output_dir = Path("/Users/luizotavio/Desktop/aivideocut")

    # print(
    #     f"Generating video info from directory {input_dir.name!r}",
    # )
    # videos = sorted(
    #     get_video_filepaths(
    #         input_dir,
    #         ("mp4",),
    #         callback=create_videoinfo,
    #         create_json=True,
    #         create_concat_file=True,
    #     ),
    #     key=lambda v: v.filename,
    # )
    #
    # print(
    #     f"Copying {len(videos)} file(s) from {input_dir.name!r} "
    #     f"to {aivideocut_output_dir.name!r}. Please, wait...",
    # )
    # This step could be skipped
    # copy_aivideocut_final(videos, aivideocut_output_dir)

    # THIS SECTION IS WHERE WE DO THE WORK
    # Input files made with aivideocut
    input_dir = Path("/Users/luizotavio/Desktop/logging/")
    # input_dir = aivideocut_output_dir

    print(
        f"Generating video info from directory {input_dir.name!r}",
    )
    videos = sorted(
        get_video_filepaths(
            input_dir,
            ("mp4",),
            callback=create_videoinfo,
            create_json=True,
            create_concat_file=True,
        ),
        key=lambda v: v.filename,
    )

    ffmpeg_command = (
        f"cd {input_dir}\n"
        "ffmpeg -f concat -safe 0 -i concat.txt -c:v libx264 -preset fast "
        "-crf 18 -c:a aac -b:a 320k "
        "-movflags +faststart -fflags +genpts FINAL.mp4 -y\n"
    )
    print("\nTudo pronto... Agora execute os comandos abaixo:\n")
    print(ffmpeg_command)

    # THIS SECTION READS THE VIDEOS INFORMATION FILE AND CREATE YOUTUBE
    # CHAPTERS
    video_info_file = input_dir / "video_info.json"
    create_youtube_chapters(video_info_file)
    print()


if __name__ == "__main__":
    main()
