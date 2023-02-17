import re

# define characters you want to remove in first inside the brackets of pattern variable
# e.g. 
#      to remove characters 'a', 'f' and 'e'
#      pattern = u'[afe]'
#
pattern = u'[\u0410\u0439]+'
x = re.sub(pattern, '', '[\u0410\u0439\u3493 example@gmail.com]')

print(x)