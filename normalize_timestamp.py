import csv
from datetime import datetime
import sys

# Function to convert Unix timestamp to human-readable date
def normalize_timestamp(unix_timestamp):
    # Convert the timestamp to a float to handle microseconds
    unix_timestamp = float(unix_timestamp)
    # Convert to a readable format
    return datetime.fromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')

# Function to normalize the CSV file
def normalize_date_column(input_csv, output_csv, date_column_name):
    # Open the input CSV file
    with open(input_csv, 'r', newline='', encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        # Open the output CSV file to write the normalized data
        with open(output_csv, 'w', newline='', encoding="utf-8") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            
            # Process each row
            for row in reader:
                # Normalize the date column
                if row[date_column_name]:
                    try:
                        row[date_column_name] = normalize_timestamp(row[date_column_name])
                    except ValueError:
                        print(f"Error converting timestamp: {row[date_column_name]}")
                
                # Write the updated row to the new file
                writer.writerow(row)
                
def main():
    if len(sys.argv) != 4:
        print("Usage: python normalize_timestamp.py <input_csv> <output_csv> <date_column_name>")
        sys.exit(1)
    
    input_csv = sys.argv[1]
    output_csv = sys.argv[2]
    date_column_name = sys.argv[3]
    
    normalize_date_column(input_csv, output_csv, date_column_name)
    
if __name__ == "__main__":
    main()
