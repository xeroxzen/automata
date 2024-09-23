import pandas as pd
import os
import sys

def normalize_ip(hex_ip):
    # Convert the hex IP to an integer, then to a proper IPv4 address
    ip_int = int(hex_ip, 16)
    return f"{(ip_int >> 24) & 0xFF}.{(ip_int >> 16) & 0xFF}.{(ip_int >> 8) & 0xFF}.{ip_int & 0xFF}"

def normalize_ip_column(input_csv, ip_column):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(input_csv)
    
    # Normalize the IP addresses in the specified column
    df[ip_column] = df[ip_column].apply(normalize_ip)
    
    # Create the output filename
    base, ext = os.path.splitext(input_csv)
    output_csv = f"{base}_ip_normalized{ext}"
    
    # Save the DataFrame to the new CSV file
    df.to_csv(output_csv, index=False)
    print(f"Normalized IP addresses saved to {output_csv}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python normalize_hex_ip.py <input_csv>")
        sys.exit(1)
    input_csv = sys.argv[1]
    ip_column = input("Enter the name of the column containing the IP addresses: ")
    normalize_ip_column(input_csv, ip_column)
