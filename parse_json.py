import csv
import json
import pandas as pd
import sys

def clean_csv(input_file):
    # Generate output filename by inserting '_json_parsed' before the extension
    output_file = input_file.rsplit('.', 1)[0] + '_json_parsed.' + input_file.rsplit('.', 1)[1]
    
    # Read the input CSV file into a Pandas DataFrame
    df = pd.read_csv(input_file)
    
    # Placeholder for all rows including expanded JSON entries
    all_rows = []
    
    for index, row in df.iterrows():
        try:
            raw_data = row[column_name]
            
            # Skip processing but keep row if empty/NaN
            if pd.isna(raw_data):
                row_dict = row.to_dict()
                row_dict.update({'nom': '', 'lien': '', 'telephone': '', 'cin': ''})
                all_rows.append(row_dict)
                continue
                
            # Skip processing but keep row if float
            if isinstance(raw_data, float):
                print(f"Skipping JSON parsing for row {index}: Found float value instead of JSON string")
                row_dict = row.to_dict()
                row_dict.update({'nom': '', 'lien': '', 'telephone': '', 'cin': ''})
                all_rows.append(row_dict)
                continue
            
            # Handle double-quoted JSON strings
            if raw_data.startswith('"[') and raw_data.endswith(']"'):
                raw_data = raw_data[1:-1].replace('""', '"')
                
            parsed_data = json.loads(raw_data.replace("'", "\""))
            
            # If no entries, add row with empty values
            if not parsed_data:
                row_dict = row.to_dict()
                row_dict.update({'nom': '', 'lien': '', 'telephone': '', 'cin': ''})
                all_rows.append(row_dict)
                continue
                
            # Create a new row for each person in the JSON
            for entry in parsed_data:
                row_dict = row.to_dict()
                row_dict.update({
                    'nom': str(entry.get("nom", "")).strip() if entry.get("nom") is not None else "",
                    'lien': str(entry.get("lien", "")).strip() if entry.get("lien") is not None else "",
                    'telephone': str(entry.get("telephone", "")).strip() if entry.get("telephone") is not None else "",
                    'cin': str(entry.get("cin", "")).strip() if entry.get("cin") is not None else ""
                })
                all_rows.append(row_dict)
                
        except (json.JSONDecodeError, AttributeError) as e:
            print(f"Error parsing JSON in row {index}: {e}")
            # Keep the original row with empty values for the JSON fields
            row_dict = row.to_dict()
            row_dict.update({'nom': '', 'lien': '', 'telephone': '', 'cin': ''})
            all_rows.append(row_dict)
            continue

    # Convert all rows to a new DataFrame
    result_df = pd.DataFrame(all_rows)
    
    # Write the modified DataFrame to a new CSV file
    result_df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")

# Update the usage section
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_json.py <input_file>")
        sys.exit(1)
        
    input_file = sys.argv[1]
    column_name = "personnes_autorisees"
    
    clean_csv(input_file)
