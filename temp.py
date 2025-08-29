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
    # ida
    assert seconds_to_hhmmss(1) == "00:00:01"
    assert seconds_to_hhmmss(10) == "00:00:10"
    assert seconds_to_hhmmss(60) == "00:01:00"
    assert seconds_to_hhmmss(70) == "00:01:10"
    assert seconds_to_hhmmss(3600) == "01:00:00"
    assert seconds_to_hhmmss(3599) == "00:59:59"

    # volta
    assert hhmmss_to_seconds("00:00:01") == 1
    assert hhmmss_to_seconds("00:01:10") == 70
    assert hhmmss_to_seconds("01:00:00") == 3600
    assert hhmmss_to_seconds("00:59:59") == 3599

    # limite de 24h (versão datetime zera)
    assert seconds_to_hhmmss(86399) == "23:59:59"
    assert seconds_to_hhmmss(86400) == "00:00:00"

    print("Tudo certo! ✅")
