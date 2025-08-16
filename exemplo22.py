#
# Classes Genéricas e TypeVar no Python 3.13 (Nova Sintaxe) - Aula 9
#
# A tipagem de Classes Genéricas ou Generic Classes seguem o mesmo padrão das
# funções genéricas que vimos na aula anterior. Defina um type parameter na
# classe e automaticamente ela se tornará uma classe genérica com a nova sintaxe
# da PEP 695 (>=3.12).
#


from dataclasses import dataclass
from datetime import UTC, datetime, timedelta

from utils import cyan_print, sep_print


class Duration:
    def __init__(self, value: str) -> None:
        self._value: str = value

    @property
    def value(self) -> str:
        return self._value

    def __repr__(self) -> str:
        return f"Duration({self._value!r})"


@dataclass
class VideoInfo:
    name: str
    duration: Duration

    @property
    def duration_time(self) -> str:
        if isinstance(self.duration.value, int | float):
            return seconds_to_time(self.duration.value)
        return self.duration.value


def seconds_to_time(seconds: float) -> str:
    delta = datetime(1, 1, 1, 0, 0, 0, tzinfo=UTC) + timedelta(seconds=seconds)
    return f"{delta:%H:%M:%S}"


if __name__ == "__main__":
    sep_print()

    # d1 = Duration(60) # Nope
    d2 = Duration("00:10:00")

    # v1 = VideoInfo("aula1.mp4", d1) # Nope
    v2 = VideoInfo("aula2.mp4", d2)

    # cyan_print(v1, v1.duration_time) # Nope
    cyan_print(v2, v2.duration_time)

    sep_print()
