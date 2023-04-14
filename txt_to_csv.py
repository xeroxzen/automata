import os
import argparse

def txt_to_csv(txt_file):
    with open(txt_file, 'r', encoding='utf-8', errors='ignore') as f:
        csv_file = os.path.splitext(txt_file)[0] + '.csv'
        with open(csv_file, 'w', encoding='utf-8', newline='') as outfile:
            outfile.write(f.read().replace('\n', ','))

def main():
    parser = argparse.ArgumentParser(description='Convert txt files to csv files')
    parser.add_argument('path', help='Path to txt file or directory containing txt files')
    args = parser.parse_args()

    path = args.path

    if os.path.isfile(path):
        if os.path.splitext(path)[1].lower() == '.txt':
            txt_to_csv(path)
        else:
            print('Error: Path does not point to a .txt file')
            return
    elif os.path.isdir(path):
        num_files_converted = 0
        originals_dir = os.path.join(path, 'originals')
        os.makedirs(originals_dir, exist_ok=True)
        for filename in os.listdir(path):
            if os.path.splitext(filename)[1].lower() == '.txt':
                txt_file = os.path.join(path, filename)
                txt_to_csv(txt_file)
                os.rename(txt_file, os.path.join(originals_dir, filename))
                num_files_converted += 1
        print(f'Success: Converted {num_files_converted} files')
    else:
        print('Error: Invalid path')
        return

if __name__ == '__main__':
    main()
