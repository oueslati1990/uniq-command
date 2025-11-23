"""Implement muniq tests"""

import subprocess
import os

def read_file(filename):
    """Reading from file"""
    with open(filename, 'r') as f:
        return f.read()

def run_muniq(args, input_data=None):
    """
    Helper function to run muniq command with given arguments
    
    Args:
        args: list of command-line arguments
        input_data: optional string to pass as stdin

    Returns:
        tuple: (stdout, stderr, return_code)
    """
    cmd = ['muniq'] + args
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        input=input_data
    )

    return result.stdout, result.stderr.strip(), result.returncode
    
def test_display_unique_read_from_file():
    """Display in standard output unique lines when the input is a file"""
    print("\n[Test 1] Testing reading from file and displaying to standard output")
    stdout, stderr, returncode = run_muniq(['test.txt'])
    assert returncode == 0, f'Expected returncode = 0 , got {returncode}'
    assert stderr == "", f"Expected no errors , got {stderr}"
    lines = stdout.strip().split('\n')
    assert len(lines) == 6, f'Expected 6 lines , got {len(lines)}'

def test_display_unique_read_from_stdin():
    """Display in standard output when reading from standard input"""
    print("\n[Test 2] Testing reading from standard input and displaying to standard output")
    input_data = read_file("test.txt")
    stdout, stderr, returncode = run_muniq(['-'], input_data)
    assert returncode == 0, f'Expected returncode = 0 , got {returncode}'
    assert stderr == "", f"Expected no errors , got {stderr}"
    lines = stdout.strip().split('\n')
    assert len(lines) == 6, f'Expected 6 lines , got {len(lines)}'

def test_write_unique_lines_to_file():
    """Write the output to a file"""
    print("\n[Test 3] Write the output to a file")
    _, stderr, returncode = run_muniq(['test.txt', 'out.txt'])
    assert returncode == 0, f'Expected returncode = 0, got {returncode}'
    assert stderr == "", f'Expected no errors, got {stderr}'
    assert os.path.exists('out.txt') == True, f'Expected creation of a file out.txt'
    out_content = read_file('out.txt').strip().split('\n')
    assert len(out_content) == 6, f'Expected 6 lines in output, got {len(out_content)}'

def test_display_count_with_lines():
    """Display the number of line occurence together with the line"""
    print("\n[Test 4] Testing displaying the number of occurence of a line with the line")
    stdout, stderr, returncode = run_muniq(['test.txt', '-c'])
    assert returncode == 0, f'Expected returncode = 0, got {returncode}'
    assert stderr == "", f'Expected no errors, got {stderr}'
    lines = stdout.strip().split('\n')
    assert len(lines) == 7, f'Expected 7 lines , got {len(lines)}'
    first_line = lines[0].split()
    assert first_line[0].isdigit(), f'Expected the first part of the line to be an integer'

def test_diplsay_repeated_lines_only():
    """Display repeated lines only"""
    print('\n[Test 5] Testing displaying only the repeated lines')
    stdout, stderr, returncode = run_muniq(['test.txt', '-d'])
    assert returncode == 0, f'Expected returncode = 0, got {returncode}'
    assert stderr == "", f'Expected no errors, got {stderr}'
    lines = stdout.strip().split('\n')
    assert len(lines) == 1, f'Expected one line only, got {len(lines)}'

def test_display_unique_lines_only():
    """Display unique lines only"""
    print('\n[Test 6] Testing displaying only the unique lines')
    stdout, stderr, returncode = run_muniq(['test.txt', '-u'])
    assert returncode == 0, f'Expected returncode to be 0, got {returncode}'
    assert stderr == "", f'Expected there are no errors, got {stderr}'
    lines = stdout.strip().split('\n')
    assert len(lines) == 5, f'Expected 5 lines, got {len(lines)}'

def main():
    print("=" * 50)
    print("Testing muniq")
    print("=" * 50)

    try:
        test_display_unique_read_from_file()
        test_display_unique_read_from_stdin()
        test_write_unique_lines_to_file()
        test_display_count_with_lines()
        test_diplsay_repeated_lines_only()
        test_display_unique_lines_only()

        print("\n" + "=" * 50)
        print("✓ All tests passed!")
        print("=" * 50)
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        exit(1)


if __name__ == '__main__':
    main()