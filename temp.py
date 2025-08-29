from datetime import datetime, timedelta


def seconds_to_hhmmss(seconds: float) -> str:
    return f"{datetime(1, 1, 1, 0, 0, 0) + timedelta(seconds=seconds):%H:%M:%S}"


def hhmmss_to_seconds(hhmmss: str) -> float:
    time_parts = reversed(hhmmss.split(":"))

    total = 0
    multiplier = 1
    for time_part in time_parts:
        total += int(time_part) * multiplier
        multiplier *= 60

    return total


if __name__ == "__main__":
    seconds = 86399
    hhmmss = seconds_to_hhmmss(seconds)

    seconds_from_hhmmss = hhmmss_to_seconds(hhmmss)
    hhmmss_from_seconds = seconds_to_hhmmss(seconds_from_hhmmss)

    print(f"{seconds_from_hhmmss=}")
    print(f"{hhmmss_from_seconds=}")
