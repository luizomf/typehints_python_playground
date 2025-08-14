import random
import time
import unicodedata as ud

import pyautogui

# dead keys do macOS para PT:
#   U+0301 COMBINING ACUTE      → "'" (acute dead key)
#   U+0300 COMBINING GRAVE      → "`" (grave dead key)
#   U+0303 COMBINING TILDE      → option+n (˜)
#   U+0302 COMBINING CIRCUMFLEX → option+i (ˆ)
#   U+0308 COMBINING DIAERESIS  → option+u (¨)

COMBINING_TO_KEYS = {
    "\u0301": ("'",),  # acento agudo
    "\u0300": ("`",),  # acento grave
    "\u0303": ("option", "n"),  # til (~)
    "\u0302": ("option", "i"),  # circunflexo (^)
    "\u0308": ("option", "u"),  # trema (¨)
    "\u0327": ("'",),  # cedilla
}


def press_keys(*keys: str, interval: float = 0) -> None:
    if len(keys) == 1:
        pyautogui.press(keys[0], interval=interval * 2)
    else:
        pyautogui.hotkey(*keys, interval=interval * 3)


def type_base_char(ch: str, interval: float = 0) -> None:
    # trata ç/Ç como teclas diretas no mac
    if ch == "ç":
        press_keys("option", "c", interval=interval)
        return
    if ch == "Ç":
        press_keys("option", "shift", "c", interval=interval)
        return
    # pyautogui.typewrite entende uppercase/minuscula direto
    pyautogui.typewrite(ch, interval=interval)


def human_type_pt_mac(
    text: str,
    min_delay: float = 0,
    max_delay: float = 0,
) -> None:
    base_delay = random.uniform(min_delay, max_delay)

    for ch in text:
        rand_delay = random.uniform(0.000000001, 0.001)
        normal_delay = base_delay + rand_delay

        print(ch, normal_delay)

        # simples: espaço/enter/tab etc
        if ch in {"\n", "\r"}:
            press_keys("enter", interval=normal_delay)
            continue
        if ch == "\t":
            press_keys("tab", interval=normal_delay)
            continue

        # normaliza para NFD
        nfd = ud.normalize("NFD", ch)

        # separa base + combinings
        base = ""
        combs: list[str] = []
        for c in nfd:
            if ud.combining(c):
                combs.append(c)
            else:
                base += c

        # aplica cada combining como dead key do mac
        for cmb in combs:
            keys = COMBINING_TO_KEYS.get(cmb)
            if keys:
                press_keys(*keys, interval=normal_delay * 2)
            else:
                # se aparecer um combining não mapeado, cai no paste de fallback
                pyautogui.typewrite(ch, interval=normal_delay)
                break
        else:
            # depois dos dead keys, envia a base
            # (maiúsculas funcionam direto via typewrite)
            type_base_char(base or ch, interval=normal_delay)


text = """
# Exemplo concreto para pré-condições (inputs / parâmetros)
# Vejamos um exemplo onde o subtipo viola uma pré-condição do LSP:

class Tags:
    def __init__(self, tags: set[str]) -> None:
        self._tags = tags

    # Contrato amplo: aceita qualquer objeto
    def __contains__(self, item: object) -> bool:
        return item in self._tags  # Para tipo "errado", retorna False


class StrictTags(Tags):
    # Pré-condição mais restritiva: agora só aceita str
    def __contains__(self, item: object) -> bool:
        if not isinstance(item, str):
            raise TypeError("item must be str")
        return item in self._tags


# Cliente escrito para o tipo base:
def has_tag(t: Tags, q: object) -> bool:
    return q in t


t1 = Tags({"python", "types"})
t2 = StrictTags({"python", "types"})

print(has_tag(t1, 123))  # False (ok no contrato do base)
print(has_tag(t2, 123))  # TypeError, subtipo ficou mais restritivo

# No código acima, Tags aceita que qualquer object seja utilizado com __contains__ (in e not in). Mas StrictTags impõe que apenas str pode ser utilizado. O type checker não reclama, mas o comportamento mudou, quebrando a pré-condição da classe base.

# Pode parecer sutil, pode funcionar agora, mas em algum momento isso vai quebrar.
"""

for i in range(3, -1, -1):
    print(f"começando em {i}...")
    time.sleep(1)  # tempo pra você focar na janela certa
print("vai...")

human_type_pt_mac(text, min_delay=0, max_delay=0.0000005)

# human_type_pt_mac(
#     """ \
# from typing import TypeVar, Generic
#
# T = TypeVar('T')  # Define type variable "T"
#
# class Stack(Generic[T]):
#     def __init__(self) -> None:
#         # Create an empty list with items of type T
#         self.items: list[T] = []
#
#     def push(self, item: T) -> None:
#         self.items.append(item)
#
#     def pop(self) -> T:
#         return self.items.pop()
#
#     def empty(self) -> bool:
#         return not self.items
# """.strip(),
# )
