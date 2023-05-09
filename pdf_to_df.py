''''
@author: Andile Jaden Mbele
'''

import os
import PyPDF2
import pandas as pd

# Function to extract data from a PDF file and convert it to a DataFrame
def pdf_to_df(pdf_file):
    # Read the PDF file
    with open(pdf_file, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        
        # Extract the text from the PDF file
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
            
        # Split the text into rows and columns
        rows = text.strip().split('\n')
        columns = rows[0].split('\t')
        
        # Create a DataFrame from the rows and columns
        data = [row.split('\t') for row in rows[1:]]
        df = pd.DataFrame(data, columns=columns)
        
        return df

# Loop through all PDF files in the directory
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        # Extract the data from the PDF file and save it as a CSV file
        df = pdf_to_df(filename)
        csv_filename = os.path.splitext(filename)[0] + '.csv'
        df.to_csv(csv_filename, index=False)
