import argparse
import sys
from typing import Dict

def read_file(filename):
     """Read file"""
     with open(filename, 'rb') as f:
          return f.read()
     
def get_uniq_lines(content) -> Dict[str, int]:
    """Retrieve unique lines from the content of the input"""
    
    dic_lines = {}
    for line in content.decode('utf-8').split('\n'):
        if line in dic_lines.keys:
            dic_lines[line] += 1
        else:
            dic_lines.add({line, 1})
    
    uniq_lines = {}
    for key, value in dic_lines:
        if value == 1:
            uniq_lines.add({key, value})

    return uniq_lines
     
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

    



if __name__ == '__main__':
    main()