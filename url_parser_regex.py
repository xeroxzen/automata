import re
url = '.ru/mail/sofiya-032013'
match = re.search(r'\/([^\/]+)$', url)
if match:
    result = match.group(1)
    print(result)

