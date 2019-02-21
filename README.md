# printc
Simple package for adding a bit more colors to scripts' output.

## Usage
Import `printc` function and use it for colored output.
The function works in the exact same manner as `print` `built in`,
with addition of __optional__ `c` keyword argument used to specify
the color __number__.

Can be used in scripts - color escape sequences are added only when
outputting to `stdout` (no codes when `piping`, `redirecting` and `writing
to file`).

Color are specified as numbers between 0 and 15.

Example for green color:
```python
from printc import printc

printc('Hello, World!', c=2)
```

## Compatibility
Should work on anything supporting ANSI escape sequences (so `*nixes`).
Windows support is out of scope.
