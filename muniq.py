import argparse
import sys
from typing import List

def read_file(filename):
    """Read file"""
    with open(filename, 'rb') as f:
        return f.read()

def get_uniq_lines(content) -> List[tuple[str, int]]:
    """Retrieve unique lines from the content of the input"""
    list_lines = []
    lines = content.decode('utf-8').split('\n')
    for i, line in enumerate(lines):
        if list_lines and list_lines[-1][0] == line:
            continue

        occ = 0
        for j in range(i, len(lines)):
            if lines[j] != line:
                break
            occ += 1
        list_lines.append((line, occ))

    return list_lines

def write_to_output(output_file, uniq_lines):
    """Write output"""
    if isinstance(output_file, str):
        # Output to file
        with open(output_file, 'w') as f:
            for line in uniq_lines:
                print(line, file=f)
    else:
        # Output to stdout
        for line in uniq_lines:
            print(line, file=output_file)

def main():
    """
    Main function to parse arguments and execute the appropriate counting operation.
    """
    parser = argparse.ArgumentParser(
        description="uniq command"
    )

    parser.add_argument('filenames', nargs='*', default=None,
                        help="input file and output file (if exists)")
    parser.add_argument('-c', '--count', action="store_true", 
                        help="count number of line appearance in the file")

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
    output_lines = []
    if args.count:
        output_lines = [
            f"{line[1]} {line[0]}"
            for line in uniq_lines
        ]
    else:
        output_lines = [
            line[0]
            for line in uniq_lines
        ]

    write_to_output(output_file, output_lines)


if __name__ == '__main__':
    main()
