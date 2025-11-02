# BookBot (Text Analytics in Python)

## Overview
CLI app that reads a text file and prints **word & character frequency** and simple analytics. Boot.dev project.

## Features
- Counts words/characters
- Top-N words
- Report to stdout (optionally to file)

## Tech
- Python 3.11+
- Standard library

## How to run

### MacOS / Linux
```bash
python -m venv .venv
source .venv/bin/activate
python main.py path/to/book.txt --top 25 --out report.txt
```
