"""
@author: Andile Jaden Mbele
@date: 7 May 2023
@Description: This method unzips all compressed files in nested directories.
"""

import os
import sys
import zipfile
import tarfile
import gzip
import rarfile
import shutil


def unzip_files(directory):
    total_unzipped = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            if file.endswith('.gz'):
                try:
                    with gzip.open(file_path, 'rb') as f_in:
                        unzipped_file_path = os.path.splitext(file_path)[0]
                        with open(unzipped_file_path, 'wb') as f_out:
                            f_out.write(f_in.read())
                        total_unzipped += 1
                except Exception as e:
                    print(f"Error unzipping file: {file_path}")
                    print(f"Error message: {str(e)}")
                    print()

            elif file.endswith('.zip'):
                try:
                    with zipfile.ZipFile(file_path, 'r') as zip_ref:
                        zip_ref.extractall(root)
                        total_unzipped += len(zip_ref.namelist())
                except Exception as e:
                    print(f"Error unzipping file: {file_path}")
                    print(f"Error message: {str(e)}")
                    print()

            elif file.endswith('.tar'):
                try:
                    with tarfile.open(file_path, 'r') as tar_ref:
                        tar_ref.extractall(root)
                        total_unzipped += len(tar_ref.getnames())
                except Exception as e:
                    print(f"Error unzipping file: {file_path}")
                    print(f"Error message: {str(e)}")
                    print()

            elif file.endswith('.rar'):
                try:
                    with rarfile.RarFile(file_path, 'r') as rar_ref:
                        rar_ref.extractall(root)
                        total_unzipped += len(rar_ref.namelist())
                except Exception as e:
                    print(f"Error unzipping file: {file_path}")
                    print(f"Error message: {str(e)}")
                    print()

            elif file.endswith('.7z'):
                try:
                    shutil.unpack_archive(file_path, root)
                    total_unzipped += 1
                except Exception as e:
                    print(f"Error unzipping file: {file_path}")
                    print(f"Error message: {str(e)}")
                    print()

    print(f"Total files unzipped: {total_unzipped}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the directory path as an argument.")
        sys.exit(1)

    directory = sys.argv[1]
    unzip_files(directory)


