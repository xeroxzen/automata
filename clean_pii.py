import sys
import re
import json

def clean_php_array(string):
  """
  Cleans the serialized PHP array stored as a string.

  Args:
      string: The serialized PHP array.

  Returns:
      A dictionary containing the extracted PII.
  """
  pii = {}
  for match in re.finditer(r'{.*?}', string):
    try:
      data = json.loads(match.group(0))
      for key, value in data.items():
        if "PHONE" in value["TYPE_ID"] or "EMAIL" in value["TYPE_ID"]:
          if key not in pii:
            pii[key] = []
          pii[key].append(value["VALUE"]["VALUE"])
    except:
      pass
  return pii

def main():
  """
  Reads the CSV file and extracts the PII.

  Args:
      argv: The command line arguments.
  """
  if len(sys.argv) < 2:
    print("Usage: python script.py <csv_file>")
    sys.exit(1)

  csv_file = sys.argv[1]
  with open(csv_file, "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
      value_id, data = line.strip().split(",", 1)
      pii = clean_php_array(data)
      for key, values in pii.items():
        for value in values:
          print(f"{value_id},{key},{value}")

if __name__ == "__main__":
  main()
