import os
import sys
import shutil
import zipfile

def move_sql_files(source_dir, destination_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Iterate through the source directory and its subdirectories
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".sql"):
                # Construct the source and destination file paths
                source_file = os.path.join(root, file)
                destination_file = os.path.join(destination_dir, file)

                # Move the .sql file to the destination directory
                shutil.move(source_file, destination_file)
                print(f"Moved: {source_file} -> {destination_file}")

def compress_directory(directory):
    # Create a zip file with the same name as the directory
    zip_file = directory + ".zip"

    # Compress the directory into the zip file
    with zipfile.ZipFile(zip_file, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, directory)
                zf.write(file_path, arcname)

    print(f"Compressed directory: {directory} -> {zip_file}")

if __name__ == "__main__":
    # Check if the command-line argument is provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_directory>")
        sys.exit(1)

    # Get the source directory from the command-line argument
    source_directory = sys.argv[1]

    # Specify the destination directory for .sql files
    destination_directory = "SQL_Files"

    # Move .sql files to the destination directory
    move_sql_files(source_directory, destination_directory)

    # Compress the destination directory
    compress_directory(destination_directory)
