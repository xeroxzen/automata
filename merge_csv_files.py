import os
import csv
import argparse

def merge_csv_files(input_directory):
    # Step 1: Identify CSV files in the specified directory
    csv_files = [f for f in os.listdir(input_directory) if f.endswith('.csv')]
    
    if len(csv_files) < 2:
        print("There are not enough CSV files to merge.")
        return

    # Step 2: Read the first CSV file to determine the common column name
    first_file_path = os.path.join(input_directory, csv_files[0])
    with open(first_file_path, 'r', newline='') as first_file:
        first_reader = csv.DictReader(first_file)
        common_column = None

        if len(first_reader.fieldnames) == 1:
            # If there's only one column, assume it as the common column
            common_column = first_reader.fieldnames[0]
        else:
            # Prompt the user to select a common column
            print("Please select a common column from the list:")
            for idx, col in enumerate(first_reader.fieldnames):
                print(f"{idx + 1}. {col}")
            selection = int(input("Enter the number of the common column: ")) - 1
            if selection >= 0 and selection < len(first_reader.fieldnames):
                common_column = first_reader.fieldnames[selection]
            else:
                print("Invalid selection. Exiting.")
                return

    # Step 3: Create a dictionary to store data using the common column as the key
    merged_data = {}

    # Step 4: Iterate through CSV files and merge data into the dictionary
    all_columns_names = set(first_reader.fieldnames)
    for file_name in csv_files:
        file_path = os.path.join(input_directory, file_name)
        with open(file_path, 'r', newline='', encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            all_columns_names.update(reader.fieldnames)
            for row in reader:
                common_value = row[common_column]
                if common_value not in merged_data:
                    merged_data[common_value] = row
                else:
                    # Merge data from the current row into the existing row
                    merged_data[common_value].update(row)

    # Step 5: Write the merged data into a new CSV file
    output_file_name = os.path.basename(input_directory) + "_merged.csv"
    output_file_path = os.path.join(input_directory, output_file_name)
    with open(output_file_path, 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=list(all_columns_names))
        writer.writeheader()
        for common_value, merged_row in merged_data.items():
            writer.writerow(merged_row)

    print(f"Merged data saved to {output_file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge CSV files based on a common column.")
    parser.add_argument("input_directory", help="Directory containing CSV files to be merged.")
    args = parser.parse_args()

    if os.path.isdir(args.input_directory):
        merge_csv_files(args.input_directory)
    else:
        print("Invalid directory path. Please provide a valid directory.")
