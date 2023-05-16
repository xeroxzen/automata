import os
import re
import csv
import sys
import PyPDF2


def extract_table_data(pdf_file):
    """
    Extracts table data from a PDF file and returns it as a list of lists
    """
    # Open the PDF file and read the text
    with open(pdf_file, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = '\n'.join([page.extract_text() for page in reader.pages])

    # Use regular expressions to extract table data
    table_pattern = r'((?:.*?\n)*?)' \
                    r'((?:\n[^\n]*)*)' \
                    r'(?:(?:\n-\n)|(?:\n(?=\d)))'
    row_pattern = r'(?:(?<=\n)|(?<=^))((?:".*?")|(?:\d+(?:\.\d+)?))'
    matches = re.findall(table_pattern, text, flags=re.DOTALL)

    tables = []
    for match in matches:
        header = [h.strip('"') for h in re.findall(row_pattern, match[0])]
        rows = [[c.strip('"') for c in re.findall(row_pattern, r)] for r in match[1].strip().split('\n')]
        tables.append([header] + rows)

    return tables


def write_to_csv(csv_file, data):
    """
    Writes a list of lists to a CSV file
    """
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)


if __name__ == '__main__':
    # Set the directory containing the PDF files
    pdf_dir = sys.argv[1]

    # Loop over all PDF files in the directory
    for pdf_file in os.listdir(pdf_dir):
        if pdf_file.endswith('.pdf'):
            # Extract table data from the PDF file
            tables = extract_table_data(os.path.join(pdf_dir, pdf_file))

            # Write the table data to CSV files
            for i, table in enumerate(tables):
                csv_file = os.path.splitext(pdf_file)[0] + f'_{i}.csv'
                write_to_csv(csv_file, table)
