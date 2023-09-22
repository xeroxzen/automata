import os
import sys

def count_lines_of_code(directory):
    count = 0
    for dir_path in directory:
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.js' or '.css'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as f:
                        count += sum(1 for line in f if line.strip() and not line.startswith(('/', '/*', '*')))

    return count

def main():
    if len(sys.argv) < 2:
        print("Usage: python count_js_lines.py <directory>")
        sys.exit(1)

    directory = sys.argv[1:]
    total_lines = count_lines_of_code(directory)
    print(f'\nNumber of lines of code in .js files: {total_lines}')

if __name__ == '__main__':
    main()
