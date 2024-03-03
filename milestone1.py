"""
File: milestone1.py
Name: Leticia
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
    # Not stored: Check if the current name exists in name data
    if name in name_data:
        # Already exists: Check if the current name's year exists in name_data
        if year in name_data[name]:
            # Merge the same names for males and females based on the name
            # If the name is repeated, store the higher ranking
            if int(rank) < int(name_data[name][year]):
                name_data[name][year] = rank
        else:
            # If the current name's year does "not" exist in name_data, so add the current name-year as a key
            name_data[name][year] = rank
    else:
        # If the current name does "not" exist in name data, add it to the name_data dictionary
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
