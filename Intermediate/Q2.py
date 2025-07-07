def read_lines(filename: str) -> list[str]:
    """
    Reads and returns lines from a file.
    """
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

def main():
    filename = input("Enter the file name: ")
    lines = read_lines(filename)
    print(f"Total lines: {len(lines)}")

if __name__ == "__main__":
    main()
