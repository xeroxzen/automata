"""
@author: Andile Mbele
@program: clean_url.py
"""

import pandas as pd
import re
import sys


def clean_url(filename):
    """
    I have a CSV file with a url column that contains some strings before the actual url.

    An example of a url in the column is: "[align=center][img]http://i.imgur.com/88g2N.png[/img]rn[
    url=http://www.loungeboard.net/showthread.php?tid=232]Lounge Board Rules & Etiquette[/url] | [
    url=http://www.loungeboard.net/showthread.php?tid=36]Premium Upgrade Information[/url] [/align]"

    The solution: Clear string that comes before the valid url
    """

    try:
        df = pd.read_csv(filename, encoding='utf-8')

        # Define a regular expression to match URLs
        url_regex = r'(https?://[^\s<>"]+|www\.[^\s<>"]+)'

        # Use the str.extract method to extract the valid parts of the URLs
        df['detail'] = df['detail'].str.extract(url_regex, expand=False) 

        # Print the cleaned URLs
        print(df['detail'])

        # save to csv
        df.to_csv(filename[:-4] + '_modified.csv', index=False)
    except Exception as e:
        print(e)


def main():
    """
    Main function.
    """
    clean_url(sys.argv[1])


if __name__ == '__main__':
    main()
