"""
File: webcrawler.py
Name: Leticia
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        # Calculate the sum of the top 200 male and female newborn names
        # for the decades 2010s, 2000s, and 1990s.

        # Step 1: Use soup to grab <tbody> objects
        # Step 2: Retrieve and sum the numbers

        # Directly extract text from <tbody> in soup:
        # <tbody> consists of <td> and <tr>:
        # <td> stands for Table Data, containing data cells (columns)
        # <tr> stands for Table Row, serving as a container for rows
        tags = soup.find_all('td')

        # Retrieve numbers and calculate sums
        data = []   # This list stores data retrieved from the website
        for tag in tags:    # Iterate over all <td> tags
            tokens = tag.text.split()
            if len(tokens) == 1:    # Check if split() results in only one data item
                data.append(tokens[0])  # If yes, add it to the data list

        text_count = 0  # Initial value for text counter
        m_sum = 0   # Initial value for male names count
        f_sum = 0   # Initial value for female names count


if __name__ == '__main__':
    main()
