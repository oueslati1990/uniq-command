import argparse
import sys
from typing import List

def read_file(filename):
    """Read file"""
    with open(filename, 'rb') as f:
        return f.read()

def get_uniq_lines(content) -> List[str]:
    """Retrieve unique lines from the content of the input"""

    dict_lines = {}
    for line in content.decode('utf-8').split('\n'):
        if line in dict_lines.keys():
            dict_lines[line] += 1
        else:
            dict_lines[line] = 1

    return dict_lines.keys()

def main():
    """
    Main function to parse arguments and execute the appropriate counting operation.
    """
    parser = argparse.ArgumentParser(
        description="uniq command"
    )

    parser.add_argument('filenames', nargs='*', default=None,
                        help="input file and output file (if exists)")

    args = parser.parse_args()

    content = b''
    output_file = sys.stdout
    input_filename = None

    try:
        count = len(args.filenames)

        # Handle input
        if count == 0:
            content = sys.stdin.buffer.read()
        elif args.filenames[0] == '-':
            content = sys.stdin.buffer.read()
            input_filename = '-'
        else:
            input_filename = args.filenames[0]
            content = read_file(args.filenames[0])

        # Handle output
        if count == 2:
            output_file = args.filenames[1]
    except FileNotFoundError:
        print(f"{input_filename}: no such file", file=sys.stderr)
        exit(1)
    except PermissionError:
        print(f"You have no permission to access this file {input_filename}", file=sys.stderr)
        exit(1)
    except IOError:
        print(f"Something went wrong when reading the file {input_filename}")
        exit(1)

    uniq_lines = get_uniq_lines(content)

    # Write output
    if isinstance(output_file, str):
        # Output to file
        with open(output_file, 'w') as f:
            for line in uniq_lines:
                print(line, file=f)
    else:
        # Output to stdout
        for line in uniq_lines:
            print(line, file=output_file)


if __name__ == '__main__':
    main()
