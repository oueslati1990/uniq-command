# muniq

A Python implementation of the Unix `uniq` command.

## Description

`muniq` filters adjacent matching lines from input, similar to the standard Unix `uniq` utility. It can display unique lines, count occurrences, and output results to a file or stdout.

## Installation

```bash
pip install -e .
```

## Usage

```bash
# Display unique lines from a file
muniq test.txt

# Count occurrences of each line
muniq -c test.txt

# Display only repeated lines
muniq -d test.txt

# Display only unique lines (non-repeated)
muniq -u test.txt

# Write output to a file
muniq test.txt output.txt

# Read from standard input
cat test.txt | muniq
```

## Options

- `-c, --count`: Prefix lines with the number of occurrences
- `-d, --repeated`: Only print duplicate lines
- `-u, --unique`: Only print unique lines

## Requirements

- Python 3.7 or higher

## Testing

Run tests with:

```bash
python muniq_tests.py
```

## License

MIT

## Author

Mohamed Oueslati (eng.oueslati.mohamed@gmail.com)
