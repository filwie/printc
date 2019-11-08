from sys import stdout

    
class Color:
    def __init__(self, c=15, flush=False):
        self.c = c
        self.flush = flush

    def __enter__(self):
        base = 30 if self.c < 16 / 2 else 90
        val = base + self.c % 8
        print(f"\033[0;{val};40m", end="")

    def __exit__(self, exc_t, exc_v, trace):
        print("\033[0m", end="", flush=self.flush)


def printc(*args, c=15, file=stdout, flush=False, **kwargs):
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
    if not isinstance(c, int) or c not in range(16):
        raise ValueError('c has to be a number in range 0..15')

    if all([c != 15,
            file is stdout,
            stdout.isatty()]):
        with Color(c, flush):
            print(*args, file=file, **kwargs)
    else:
        print(*args, file=file, flush=flush, **kwargs)


if __name__ == '__main__':
    block = '████'
    for i in range(0, 8):
        printc(block, c=i, end='')
    printc()
    for i in range(8, 16):
        printc(block, c=i, end='')
    printc()
