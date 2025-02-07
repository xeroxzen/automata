import os
import sys
import pandas as pd
import time
from tqdm import tqdm

def find_and_merge_coordinates(root_dir):
    processed_files = []
    file_list = []
    
    # Collect all CSV file paths
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".csv"):
                file_list.append(os.path.join(subdir, file))
    
    start_time = time.time()
    
    # Process files with a progress bar
    for file_path in tqdm(file_list, desc="Processing CSV files", unit="file"):
        try:
            # Load the CSV file with error handling
            df = pd.read_csv(file_path, dtype=object, engine="python", on_bad_lines="skip")
            
            # Find latitude and longitude columns
            lat_cols = [col for col in df.columns if col.lower() in ["latitude", "lat", "location_latitude", "location_lat", "geocord_lat", "geocordinate_lat", "source_lat", "destination_lat"]]
            lon_cols = [col for col in df.columns if col.lower() in ["longitude", "lon", "location_longitude", "location_lon", "geocord_lon", "geocordinate_lon", "source_lon", "destination_lon"]]  
            
            if lat_cols and lon_cols:
                lat_col = lat_cols[0]
                lon_col = lon_cols[0]
                
                # Merge latitude and longitude into 'latlan', keeping empty rows empty
                df["latlan"] = df[lat_col].fillna("").astype(str) + "," + df[lon_col].fillna("").astype(str)
                df["latlan"] = df["latlan"].str.strip(",")  # Remove trailing commas for empty rows
                
                # Drop original latitude and longitude columns
                df.drop(columns=[lat_col, lon_col], inplace=True)
                
                # Save back to the same file
                df.to_csv(file_path, index=False)
                processed_files.append(file_path)

        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    elapsed_time = time.time() - start_time
    
    # Generate report
    report_path = os.path.join(root_dir, "processed_files_report.txt")
    with open(report_path, "w") as report_file:
        report_file.write("Files processed:\n")
        for processed_file in processed_files:
            report_file.write(processed_file + "\n")
    
    print(f"Processing complete. Report saved at: {report_path}")
    print(f"Total processing time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python find_and_merge.py /path/to/the/files")
        sys.exit(1)
    
    root_directory = sys.argv[1]
    find_and_merge_coordinates(root_directory)
