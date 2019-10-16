# listdir

## What is it?
This is a Python program that implements the UNIX command grep.

## Requirements
- [Python 3](https://www.python.org/downloads/)

## How to use?
```
grep.py [-h] [-l] [-r] [-i] [-I] [-c] expression file_pattern directory
```

## Arguments
```
positional arguments:
  expression          Expression to look for.
  file_pattern        file name.
  directory           Directory to look into.

optional arguments:
  -h, --help          show this help message and exit
  -l, --line_number   Print the line number.
  -r, --recursive     Go through subdirectories.
  -i, --ignore_case   Ignore case.
  -I, --invert_match  Look for lines not containing the expression.
  -c, --count         Print the number of line occurrences.

```
