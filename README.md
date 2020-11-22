# tuf-on-a-plane

[![Tests](https://github.com/trishankatdatadog/tuf-on-a-plane/workflows/Tests/badge.svg)](https://github.com/trishankatdatadog/tuf-on-a-plane/actions?workflow=Tests)

Allegedly, a minimal, Pythonic TUF client can be written on a long flight. This was written _after_ that flight, but hey, it's a shot.

Features include:
* A ["hypermodern"](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/) Python setup for packaging, testing, linting, typing, documentation, and CI/CD
* Abstract metadata "syntax trees" a.k.a. [models](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)
* [Recursive descent parsers](https://en.wikipedia.org/wiki/Recursive_descent_parser) for concrete metadata formats (e.g., JSON)

The idea is not necessarily to rewrite the TUF reference implementation from scratch, but to imagine what could be done when not encumbered by legacy code.
