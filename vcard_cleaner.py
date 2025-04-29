import csv
import sys
import os
from collections import defaultdict
import time

# Mapping from VCF field to desired column name
FIELD_MAP = {
    "UID": "id",
    "N": "first_name",
    "FN": "name",
    "TEL": "phone",
    "ADR": "address",
    "EMAIL": "email",
    "ORG": "company",
    "NOTE": "note",
    "CATEGORIES": "category",
    "BDAY": "birth_date",
    "TITLE": "position",
    "URL": "url"
}

# Final columns in the output CSV
OUTPUT_COLUMNS = list(FIELD_MAP.values())

def extract_first_name(n_value):
    # Get the second field if present (First Name)
    parts = n_value.split(';')
    if len(parts) > 1:
        return parts[1].strip()
    return n_value.strip()

def parse_contacts(input_path):
    contacts = []
    current_contact = defaultdict(str)
    with open(input_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row['name']
            value = row['value']

            if name == "UID":
                if current_contact:
                    contacts.append(current_contact)
                    current_contact = defaultdict(str)
                current_contact[FIELD_MAP["UID"]] = value
            elif name in FIELD_MAP:
                mapped_field = FIELD_MAP[name]

                if name == "N":
                    current_contact[mapped_field] = extract_first_name(value)
                elif name == "TEL":
                    if current_contact[mapped_field]:
                        current_contact[mapped_field] += f";{value}"
                    else:
                        current_contact[mapped_field] = value
                else:
                    current_contact[mapped_field] = value

        if current_contact:
            contacts.append(current_contact)

    return contacts

def write_cleaned_csv(contacts, output_path):
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        for contact in contacts:
            writer.writerow({field: contact.get(field, '') for field in OUTPUT_COLUMNS})

def main():
    start_time = time.time()
    if len(sys.argv) != 2:
        print("Usage: python vcard_cleaner.py /path/to/file.csv")
        sys.exit(1)

    input_path = sys.argv[1]
    if not os.path.isfile(input_path):
        print(f"File not found: {input_path}")
        sys.exit(1)

    output_path = os.path.join(os.path.dirname(input_path), "synthentic_vcards+2.csv")

    contacts = parse_contacts(input_path)
    write_cleaned_csv(contacts, output_path)

    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.2f} seconds")
    print(f"✅ Cleaned CSV saved to: {output_path}")

if __name__ == "__main__":
    main()
