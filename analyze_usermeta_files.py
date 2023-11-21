import os
import sys
import pandas as pd

def find_usermeta_files(directory):
    usermeta_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv") and "usermeta_cleaned" in file:
                usermeta_files.append(os.path.join(root, file))
    return usermeta_files

def analyze_usermeta_files(files):
    column_counts = {}

    for file in files:
        df = pd.read_csv(file, encoding="utf-8", on_bad_lines='warn')
        columns_to_ignore = ['shipping', 'billing', 'first_name', 'last_name', 'email', 'twitter', 'facebook',
                             'google', 'linkedin', 'youtube', 'instagram', 'pinterest', 'vimeo', 'tumblr','name',
                             'username','password', 'user_login', 'user_pass', 'user_email', 'user_url',
                             'user_nicename','mobile', 'phone', 'address', 'city', 'state', 'country', 'zip',
                             'fullname', 'nickname', 'display_name', 'user_registered', 'user_activation_key', 'userid']
        valid_columns = [column for column in df.columns if all(ignore not in column.lower() for ignore in columns_to_ignore)]

        for column in valid_columns:
            if column in column_counts:
                column_counts[column] += 1
            else:
                column_counts[column] = 1

    return column_counts

def generate_report(column_counts):
    repeated_columns = {key: value for key, value in column_counts.items() if value > 1}

    if repeated_columns:
        print("Repeated columns in usermeta files:")
        for column, count in repeated_columns.items():
            print(f"Column '{column}' appears {count} times.")
    else:
        print("No repeating columns found. No pattern identified.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    usermeta_files = find_usermeta_files(directory_path)

    if not usermeta_files:
        print("No usermeta files found.")
    else:
        column_counts = analyze_usermeta_files(usermeta_files)
        generate_report(column_counts)
