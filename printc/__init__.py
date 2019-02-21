from sys import stdout


def add_color_esc_codes(text: str, c: int) -> str:
    """Surround string with escape color code and
    """
    cnum = 16
    base = 30 if c < cnum / 2 else 90
    color_code = f'\033[0;{base + c % 8};40m'
    reset_code = '\033[0m'
    return f'{color_code}{text}{reset_code}'


def printc(*objects, c=15, sep=' ', end='\n', file=stdout, flush=False):
    """Print text in one of 16 base colors

    Colors are only added if the output is to stdout and not
    piped or redirected.

    Colors:
        0 - black       8 - brightblack
        1 - red         9 - brightred
        2 - green      10 - brightgreen
        3 - yellow     11 - brightyellow
        4 - blue       12 - brightblue
        5 - magenta    13 - brightmagenta
        6 - cyan       14 - brightcyan
        7 - white      15 - brightwhite (default)
    """
    if not isinstance(c, int):
        raise ValueError('c has to be a number in range 0..15')
    msg = sep.join(str(o) for o in objects)
    if file is stdout and c != 15:
        if stdout.isatty():
            msg = add_color_esc_codes(msg, c=c)
    print(msg, end=end, file=file, flush=flush)


if __name__ == '__main__':
    block = '████'
    for i in range(0, 8):
        printc(block, c=i, end='')
    printc()
    for i in range(8, 16):
        printc(block, c=i, end='')
