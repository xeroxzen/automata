import ipaddress

def intoTOIPaddress(IPint):
    if isinstance(IPint, str) and IPint.endswith(".0"):
        IPint = IPint.replace(".0", "")
    if isinstance(IPint, float):
        IPint = str(IPint).replace(".0", "")
    if isinstance(IPint, str) and "x" in IPint:
        IPint = int(IPint, 16)
    elif IPint.isdigit():
        IPint = int(IPint)
    
    if IPint < 0:
        IPint = IPint & 0xFFFFFFFF  # Convert negative to equivalent positive 32-bit integer
    
    try:
        ip = ipaddress.ip_address(IPint).exploded
    except ValueError:
        ip = IPint
    
    if str(ip) == "nan":
        ip = ""
    
    return ip

# Example usage:
result = intoTOIPaddress(-1019603951)
print(result)

