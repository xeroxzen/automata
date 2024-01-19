import os
import sys

def delete_empty_modified_csv(directory):
    # Iterate through files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".csv") and "modified" in filename.lower():
            file_path = os.path.join(directory, filename)

            # Check if the file has 0 bytes
            if os.path.getsize(file_path) == 0:
                print(f"Deleting {filename}")
                os.remove(file_path)

if __name__ == "__main__":
    target_directory = sys.argv[1]

    delete_empty_modified_csv(target_directory)

