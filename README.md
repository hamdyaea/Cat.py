# Cat.py — Minimal Python cat

**Developer:** Hamdy Abou El Anein  
**Contact:** info@daylightlinux.ch  
**License:** GPL v3 (see LICENSE).

A lightweight binary-safe Python implementation of the Unix `cat` command. It streams file contents without loading them into memory, accepts multiple filenames, reads stdin when given `-` or no arguments, and reports missing files without stopping subsequent files.

```sh
python3 cat.py README.md
printf 'hello' | python3 cat.py -
python3 -m unittest discover -s tests -v
```

The original implementation is preserved on [old](https://github.com/hamdyaea/Cat.py/tree/old). This is a teaching project, not a complete GNU coreutils replacement.
