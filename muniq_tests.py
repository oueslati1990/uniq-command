"""Implement muniq tests"""

import subprocess

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

def main():
    print("=" * 50)
    print("Testing muniq")
    print("=" * 50)

    try:
        test_display_unique_read_from_file()

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