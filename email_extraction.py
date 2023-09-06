import re
import pandas as pd
import sys

def clean_email(text):
  email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
  email = email_pattern.findall(text)
  return email

def main():
  csv_file = sys.argv[1]
  df = pd.read_csv(csv_file)

  df["email"] = df["message"].apply(clean_email)

  output_file = csv_file + "_email_address_extracted.csv"
  df.to_csv(output_file, index=False)

if __name__ == "__main__":
  main()
