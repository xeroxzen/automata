'''
@author: Andile Jaden Mbele
@date: Monday 20th February 2023
@description: This file contains the clean_email function which is used to clean the email address
'''

import re

def clean_email(val: str) -> str:
    '''
    This function cleans the email address by removing all extra characters and quotes from the email address.
    '''
    # remove all extra characters from the email address
    # pattern = u'[\u0424\u0435\u0434\u043e\u0440]+'
    res = re.sub('(.*<|>])', '', val)
    return res

if __name__ == '__main__':
    print(clean_email('[\u0437\u0456\\u0430\u0457\u0434\u0430 <Lisc@i.ua>]'))
                      