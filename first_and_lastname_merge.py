import pandas as pd
import sys

def merge_names(input_file):
    """Merges first_name and last_name columns into a fullname column, handling different cases.
    

    Args:
        input_file (str): Path to the CSV file
    """
    
    df = pd.read_csv(input_file, encoding="utf-8")
    
    # Check for relevant columns names in various possible cases
    first_name_cols = [col for col in df.columns if col.lower() in ["first_name", "firstname"]]
    last_name_cols = [col for col in df.columns if col.lower() in ["last_name", "lastname"]]
    
    # For billing
    billing_firstname_cols = [col for col in df.columns if col.lower() in ["billing_first_name", "billing_firstname"]]
    billing_lastname_cols = [col for col in df.columns if col.lower() in ["billing_last_name", "billing_lastname"]]
    
    # For shipping
    shipping_firstname_cols = [col for col in df.columns if col.lower() in ["shipping_first_name", "shipping_firstname"]]
    shipping_lastname_cols = [col for col in df.columns if col.lower() in ["shipping_last_name", "shipping_lastname"]]
    
    if first_name_cols and last_name_cols:
        df.insert(2, "fullname", df[first_name_cols[0]].str.cat(df[last_name_cols[0]], sep=" "))
        df.drop(first_name_cols + last_name_cols, axis=1, inplace=True)
        
    elif billing_firstname_cols and billing_lastname_cols:
        df["billing_fullname"] = df[billing_firstname_cols[0]].str.cat(df[billing_lastname_cols[0]], sep=" ")
        df.drop(billing_firstname_cols + billing_lastname_cols, axis = 1, inplace=True)
        
    elif shipping_firstname_cols and shipping_lastname_cols:
        df["shipping_fullname"]=df[shipping_firstname_cols[0]].str.cat(df[shipping_lastname_cols[0]], sep=" ")
        df.drop(shipping_firstname_cols + shipping_lastname_cols, axis=1,inplace=True)
        
    else:
        print("No columns matching your criteria found")
        
    df.to_csv(input_file, index=False)
    
if __name__ == "__main__":
    input_file = sys.argv[1]
    merge_names(input_file)