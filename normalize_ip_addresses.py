import pandas as pd
import ipaddress
import sys

def normalize_ip_addresses(csv_file_path):
    """Normalizes the IP addresses in a CSV file.

    Args:
        csv_file_path (str): The path to the CSV file.

    Returns:
        None. The normalized IP addresses are saved to a new CSV file in the same directory as the original CSV file.
    """

    df = pd.read_csv(csv_file_path)

    if "ip" in df.columns or "ip_address" or "ipv4_addresses" in df.columns:
        ip_column = df.loc[:, "ip" or "ip_address" or "ipv4_addresses"]
    else:
        raise ValueError("The CSV file does not contain a column named ip or ip_address.")

    # Normalize the IP addresses.
    for index, row in df.iterrows():
        ip = row[ip_column]
        try:
            df.loc[index, ip_column] = ipaddress.ip_address(ip)._get_address()
        except Exception as e:
            print(f"Error processing IP address: {ip} - {e}")

    # Save the normalized IP addresses to a new CSV file.
    new_csv_file_path = f"{csv_file_path}_ip_normalized.csv"
    df.to_csv(new_csv_file_path, index=False)

if __name__ == "__main__":
    csv_file_path = sys.argv[1]
    normalize_ip_addresses(csv_file_path)
