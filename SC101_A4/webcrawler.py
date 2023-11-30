"""
File: webcrawler.py
Name: 
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

        # 計算2010s, 2000s, 和 1900s的男女新生兒前200名的人數總和
        # 步驟1：用soup 拿 <tbody> 的物件
        # 步驟2：拿數字並且加總計算

        # 題目提示：直接對 soup 裡面的 <tbody> 物件取出文字:
        # 而 <tbody> 內有 <td> 跟 <tr> 組成：
        # <td> 為 Table Data, 為表格資料格的內容(欄位)
        # <tr> 為 Table row, 為表格的容器(container)
        tags = soup.find_all('td')

        # 拿數字並加總
        data = []   # 此列表是用來存網站上拿的資料
        for tag in tags:    # 遍歷所有 <td> 標籤
            tokens = tag.text.split()
            if len(tokens) == 1:    # 判斷split()後是否只有ㄧ個資料
                data.append(tokens[0])  # 是，只有ㄧ個資料，加到data列表當中

        text_count = 0  # 文字初始值
        m_sum = 0   # 男生名字數量初始值
        f_sum = 0   # 女生名字數量初始值


if __name__ == '__main__':
    main()
