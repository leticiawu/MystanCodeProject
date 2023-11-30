"""
File: milestone1.py
Name: 
-----------------------
This file tests the milestone 1 for
our babyname.py project
"""

import sys

# The file name of our target text files
# FILE = 'baby-1900.txt', 'baby-1910.txt', 'baby-1920.txt', 'baby-1930.txt', 'baby-1940.txt', 'baby-1950.txt', \
#        'baby-1960.txt', 'baby-1970.txt', 'baby-1980.txt', 'baby-1990.txt', 'baby-2000.txt', 'baby-2010.txt'


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any value.
    """
    # 三功能：未存過、已存在、重複名稱的話存排名靠前的排名
    # [ 未存過 ] 判斷當前名字有沒有在name data
    if name in name_data:
        # [ 已存在 ] 判斷當前名字的year是否存在name_data
        if year in name_data[name]:
            # 以名字為創建的基礎，將男生和女生的相同名稱合併，之後查詢其名稱，透過同ㄧ個名字皆可找到男生和女生的排名
            # 判斷當前排名是否比現有排名靠前，如果有比較靠前，更新為「排名靠前的排名」
            if int(rank) < int(name_data[name][year]):
                name_data[name][year] = rank
        else:
            # 當前名字的year「沒有」存在name_data，因此新增當前名稱year的key
            name_data[name][year] = rank
    else:
        # 當前名字「沒有」在name data，新增在name_data的字典裡
        name_data[name] = {year: rank}


# ------------- DO NOT EDIT THE CODE BELOW THIS LINE ---------------- #


def test1():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    print('--------------------test1----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test2():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('--------------------test2----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test3():
    name_data = {'Kylie': {'2010': '57'}, 'Sammy': {'1980': '451', '1990': '200'}, 'Kate': {'2000': '100'}}
    add_data_for_name(name_data, '1990', '900', 'Sammy')
    add_data_for_name(name_data, '2010', '400', 'Kylie')
    add_data_for_name(name_data, '2000', '20', 'Kate')
    print('-------------------test3-----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test4():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    add_data_for_name(name_data, '2000', '108', 'Kate')
    add_data_for_name(name_data, '1990', '200', 'Sammy')
    add_data_for_name(name_data, '1990', '90', 'Sammy')
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('--------------------test4----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def main():
    args = sys.argv[1:]
    if len(args) == 1 and args[0] == 'test1':
        test1()
    elif len(args) == 1 and args[0] == 'test2':
        test2()
    elif len(args) == 1 and args[0] == 'test3':
        test3()
    elif len(args) == 1 and args[0] == 'test4':
        test4()


if __name__ == "__main__":
    main()
