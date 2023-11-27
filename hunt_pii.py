import os
import csv
import argparse
import json

def is_output_folder(folder_name):
    ignore_folders = ["originals", "badones", "complete", "sql_statements", "unable_to_parse", "wrong_length"]
    return folder_name == "output" and folder_name not in ignore_folders

def contains_pii(column_names):
    pii_keywords = ["userid","email", "firstname", "lastname", "first_name","last_name", "password", "ip_address", "city", "address", "phone",
                    "hashed_password", "created_at"]
    for keyword in pii_keywords:
        if any(keyword in col.lower() for col in column_names):
            return True
    return False

def analyze_csv(csv_file):
    with open(csv_file, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        column_names = next(reader)
        pii_found = contains_pii(column_names)
        useless_columns = [col for col in column_names if col.lower() not in ["id", "name", "description", "userid",
                                                                              "username", "user_login", "user_pass",
                                                                              "firstname", "lastname", "email",
                                                                              "password","nickname", "display_name",
                                                                              "twitter", "facebook", "google",
                                                                              "fullname","linkedin", "youtube",
                                                                              "registered", "instagram", "pinterest",
                                                                              "ip_address", "vimeo", "tumblr",
                                                                              "ipv4_addresses", "ipv6_addresses",
                                                                              "password", "hashed_password", "skype",
                                                                              "googleplus", "usernicename", "mobile",
                                                                              "homepage", "comment_author",
                                                                              "comment_author_email",
                                                                              "comment_author_url","birthday",
                                                                              "address", "gender", "phone", "city",
                                                                              "work_position", "work_phone",
                                                                              "work_fax","work_www", "work_address",
                                                                              "work_company", "birthdate",
                                                                              "full_name", "activation_key",
                                                                              "first_name", "last_name",
                                                                              "user_email", "comment_author_ip",
                                                                              ]]

    return pii_found, useless_columns

def analyze_directory(directory):
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    report = {'directory': directory, 'csv_count': len(csv_files), 'csv_details': []}

    for csv_file in csv_files:
        file_path = os.path.join(directory, csv_file)
        pii_found, useless_columns = analyze_csv(file_path)
        report['csv_details'].append({'file': csv_file, 'pii_found': pii_found, 'useless_columns': useless_columns})

    return report

# Save reports to a text and json file. Save these files in the root directory of the CSV files, which is passed in as the input_directory argument.
def save_report(reports, output_file):
    with open(output_file, 'w') as file:
        for report in reports:
            file.write(f"Directory: {report['directory']}\n")
            file.write(f"CSV Files Found: {report['csv_count']}\n")
            for csv_detail in report['csv_details']:
                file.write(f"  File: {csv_detail['file']}\n")
                file.write(f"    PII Found: {csv_detail['pii_found']}\n")
                file.write(f"    Useless Columns: {csv_detail['useless_columns']}\n")

    json_file = output_file.replace('.txt', '.json')
    with open(json_file, 'w') as file:
        json.dump(reports, file)
    

def main():
    parser = argparse.ArgumentParser(description='CSV PII Analyzer')
    parser.add_argument('input_directory', help='Input directory containing nested CSV files')
    parser.add_argument('--output_file', default='analysis_report.txt', help='Output file for the analysis report')
    args = parser.parse_args()

    if not os.path.exists(args.input_directory):
        print(f"Error: The specified directory '{args.input_directory}' does not exist.")
        return

    reports = []
    for root, dirs, files in os.walk(args.input_directory):
        for dir_name in dirs:
            if is_output_folder(dir_name):
                directory_path = os.path.join(root, dir_name)
                report = analyze_directory(directory_path)
                reports.append(report)

    for report in reports:
        print(f"\nDirectory: {report['directory']}")
        print(f"CSV Files Found: {report['csv_count']}")
        for csv_detail in report['csv_details']:
            print(f"\n  File: {csv_detail['file']}")
            print(f"    PII Found: {csv_detail['pii_found']}")
            print(f"    Useless Columns: {csv_detail['useless_columns']}")

    save_report(reports, args.output_file)
    print(f"\nAnalysis report saved to: {args.output_file}")

if __name__ == "__main__":
    main()
