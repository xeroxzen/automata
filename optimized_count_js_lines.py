import glob
import os
import re
import sys


def count_lines_of_code(directory):
    count = 0
    comment_pattern = re.compile(r"^(//|/\*|\*)")

    for dir_path in directory:
        for file_path in glob.iglob(os.path.join(dir_path, "**/*.js")):
            with open(file_path, "r") as file:
                while True:
                    chunk = file.read(4096)
                    if not chunk:
                        break
                    count += sum(
                        1
                        for line in chunk.splitlines()
                        if line.strip() and not comment_pattern.match(line)
                    )

    return count


def main():
    if len(sys.argv) < 2:
        print("Usage: python optimized_count_js_lines.py <directory>")
        sys.exit(1)

    directory = sys.argv[1:]
    print(count_lines_of_code(directory))


if __name__ == "__main__":
    main()
