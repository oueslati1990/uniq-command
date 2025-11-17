import argparse
import sys
from typing import List

def read_file(filename):
     """Read file"""
     with open(filename, 'rb') as f:
          return f.read()
     
def get_uniq_lines(content) -> List[str]:
    """Retrieve unique lines from the content of the input"""
    
    uniq_lines = {}
    for line in content.decode('utf-8').split('\n'):
        if line in uniq_lines.keys():
            uniq_lines[line] += 1
        else:
            uniq_lines[line] = 1

    return uniq_lines.keys()
     
def main():
     """
     Main function to parse arguments and execute the appropriate counting operation.
     """
     parser = argparse.ArgumentParser(
         description="uniq command"
     )

     parser.add_argument('filename', nargs='?', default=None, 
                         help="file to analyze")
     
     args = parser.parse_args()

     content = b''
     try:
         if args.filename:
            content = read_file(args.filename)
     except FileNotFoundError:
         print(f"{args.filename}: no such file", file=sys.stderr)
         exit(1)
     except PermissionError:
         print(f"You have no permission to access this file {args.filename}", file=sys.stderr)
         exit(1)
     except IOError:
         print(f"Something went wrong when reading the file {args.filename}")
         exit(1)

     uniq_lines = get_uniq_lines(content)

     for key in uniq_lines:
         print(key, file=sys.stdout)


if __name__ == '__main__':
    main()