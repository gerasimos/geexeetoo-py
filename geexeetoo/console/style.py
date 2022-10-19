# https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal

from enum import IntEnum
from typing import Iterable


class ColorCode(IntEnum):
    BLACK = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    MAGENTA = 5
    CYAN = 6
    WHITE = 7


class FormatCode(IntEnum):
    BOLD = 1
    FAINT = 2
    ITALIC = 3
    UNDERLINE = 4
    BLINKING = 5
    FAST_BLINKING = 6
    REVERSE = 7
    HIDE = 8
    STRIKETHROUGH = 9


def style_reset():
    return '\x1b[0m'


def style_set(fg: ColorCode = None, bg: ColorCode = None, st: Iterable[FormatCode] = None):
    """

    """

    props = []
    if isinstance(st, list):
        props = [s.value for s in st]
    if isinstance(fg, ColorCode):
        props.append(f'{90 + fg.value}')
    if isinstance(bg, ColorCode):
        props.append(f'{40 + bg.value}')

    props = ';'.join([str(x) for x in props])

    return f'\x1b[{props}m'
