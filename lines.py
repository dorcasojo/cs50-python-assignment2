import sys


def get_filename():
    """Validate the command-line arguments and return the file name."""
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    filename = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")
    return filename


def is_code_line(line):
    """Return True if the line is neither blank nor a comment."""
    stripped = line.strip()
    return stripped != "" and not stripped.startswith("#")


def count_lines(filename):
    """Count the lines of code in the file."""
    try
        with open(filename) as file:
            return sum(1 for line in file if is_code_line(line))
    except FileNotFoundError:
        sys.exit("File does not exist")


def main():
    print(count_lines(get_filename()))


if __name__ == "__main__":
    main()
