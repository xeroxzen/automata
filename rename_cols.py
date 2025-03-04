import os
import sys
import pandas as pd
from tqdm import tqdm

def find_csv_files(root_dir):
    """Recursively find all CSV files in the given directory and subdirectories, ignoring specified folders."""
    excluded_dirs = {"originals", "badones", "wrong_length", "sql_statements", "unable_to_parse", "complete", "files_that_were_combined"}
    csv_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if any(excluded in dirpath.split(os.sep) for excluded in excluded_dirs):
            continue
        for file in filenames:
            if file.endswith(".csv"):
                csv_files.append(os.path.join(dirpath, file))
    return csv_files

def rename_columns(df, mapping):
    """Rename columns in a DataFrame based on the mapping dictionary."""
    column_mapping = {}
    for new_name, old_names in mapping.items():
        for old_name in old_names:
            if old_name in df.columns:
                column_mapping[old_name] = new_name
    df.rename(columns=column_mapping, inplace=True)
    return df, column_mapping

def process_csv_files(root_dir, mapping):
    """Process all CSV files, renaming columns and saving changes with a progress bar. Write changes to a log file."""
    csv_files = find_csv_files(root_dir)
    log_file = os.path.join(root_dir, "column_changes_log.txt")
    
    if not csv_files:
        print("No CSV files found in the given directory.")
        return
    
    with open(log_file, "w") as log:
        log.write("Column Rename Log\n")
        log.write("=================\n\n")
        
        for file in tqdm(csv_files, desc="Processing CSV files", unit="file"):
            try:
                df = pd.read_csv(file, dtype=str, low_memory=False)
                df, changes = rename_columns(df, mapping)
                df.to_csv(file, index=False)
                
                if changes:
                    log.write(f"File: {file}\n")
                    for old_col, new_col in changes.items():
                        log.write(f"  {old_col} -> {new_col}\n")
                    log.write("\n")
            except Exception as e:
                print(f"Error processing {file}: {e}")
    
    with open(log_file, "r") as log:
        print("\nChanges logged in column_changes_log.txt:\n")
        print(log.read())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rename_columns.py \"path/to/directory\"")
        sys.exit(1)
    
    directory = sys.argv[1]
    mappingkeys = {"address": ["address", "location", "contact", "postal address", "address1", "address2", "customeraddress", "address, city, county_name, st, zip", "address,city,county_name,st,zip"],
                   "company": ['azienda', "company", "corporation", 'organization_name', "organization", "companyname", "company_name"],
                   "creditcard": ["creditcard", "creditcardnumber", "ccnumber"],
                   "unknown_userid": ["unknownuserid", "unknown_userid"],
                   "unknown_username": ["unknown_username", "unknown_username"],
                   "ssn": ["ssn", "socialsecuritynumber"],
                   "name": ["aka1fullname", "aka2fullname", "aka3fullname", "patient", "nombre", "given_name", "givenname", "customer name", "customername", "name", "fullname", "profname", "display_name", "displayname", "nome", 'Navn', 'Telefon', 'client_fullname', "comment_author", "author_name"],
                   "hashed_password": ['members_pass_hash', 'clave', "pwd", "newpasswd", "password_hash", "hashed_password", "senha", "passwordx", "passwordy", "user_pass", "password", "hashedpassword", "encryptedpassword", "passwd", "userpass", "secondpassword", "thirdpassword", "passwordhash", "pass", "user_pass"],
                   "password": ["passwordplain", "plaintextpassword", "plainpassword", "passwordplaintext", "passwordplain1"],
                   "ipv4_addresses": ['ipregistrationnewsletter', 'ip_registration_newsletter', 'createip', 'lastloginip', 'regip', 'remote_ip', 'ip_user', "ipaddr", "last_ip", "ip_addr", "ipaddress", "loginip", "ipaddress", "ip", "lastip", "firstip", "currentsigninip", "lastsigninip", "loginip", "author_ip", "latestip", "ipv4_addresses", "comment_author_ip"],
                   "email": ['email_id', 'adressee-mail', 'adresseemail', 'indirizzoemail', 'correo', 'adressee-mail', 'adressee-mail', 'primaryemail', "personal_emails", "personalemails", "emails", "direccióndecorreoelectrónico", "e_mail", "customer email", "mail", "customeremail", "email", "emailaddress", "emails", "emailcontact", "user_email", "e-mail", "author_email", "author_email", "comment_author_email", "from_email", "to_email", "patient_email", "doctoremail", "cc_email", "bc_email", "sys_email_address", "contact_email"],
                   "username": ['loginname', "usernames", "username", "usuario", "alias", "nickname", "screenname", "login", "user_login", "nick"],
                   "userid": ['id_member', 'usr_id', "idmembro", "userid", "uid", "useridstr", "memberid", 'pwsid', 'individual_h_hid'],
                   "phone":['telephonenumber','primary_mobile_no','full_phone_number','fullphonenumber','billing_phone','billingphone','telephone_no','phone1','phonenumbers','dayphone','eveningphone','altmobile','telefone','telefone1','telefone2','telefone4','telefone3','móvil','MOBILE_PHONE'.lower(),"phones","cellnumber","fone","fax_number","celular","phone_cell","phonecell","home_phone","phonehome","phonecell","work_phone","homephone","workphone","SmsPhone".lower(),"hometelephone","tele","fone","customerphone","phone1","phone2","phone3","phonemobile","cellphonenumber",'contactnumber','mobilenumber','telefone',"phone_home","mobileno","mobilenumber",'cellulare',"telephone","mobile","phone","cellular","fax","faxnumber","mobilephone","tel","phonenumber","workphone","homephone","homephoneno","workphoneno","mobilephoneno","primaryphoneno","PHONE_NO".lower(),"phoneno","cellphone","telefono","mobileno","phone_mobile","voip_no",'voipno','client_phone_number', 'telefon','phone_number'],
                   "createdat": ["createdat", "created_at", "datecreated", "datecreatedat", "datecreatedat", "datecreated"],
                   "updatedat": ["updatedat", "updated_at", "dateupdated", "dateupdatedat", "dateupdatedat", "dateupdated", "modified", "datemodified", "datemodifiedat", "datemodifiedat"],  
                   }
    
    process_csv_files(directory, mappingkeys)
