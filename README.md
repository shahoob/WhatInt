# `WhatInt` ![GitHub release (latest by date)](https://img.shields.io/github/v/release/shahoob/WhatInt?label=%20&logo=python&logoColor=white&style=flat-square)
Another "guess a number" game.

## Installation
```
pip install -r requirements.txt
```

## Usage
```
Usage: main.py [OPTIONS]

Options:
  -m, --max INTEGER  The max range for generating the integer (that you're
                     trying to guess)

  -M, --min INTEGER  The min range for generating the integer (that you're
                     trying to guess)

  --help             Show this message and exit.
```

What the game looks like:
```
what integer: 3
too far away
what integer: 1
far behind.
what integer: 2
yes
you toke 3 tries to get 2.
you have used these integers:
3
1
2
```
To stop the game:
```
what integer: stop
you have canceled the game
```
