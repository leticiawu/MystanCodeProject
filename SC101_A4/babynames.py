"""
File: babynames.py
Name: 
--------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import sys


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
    # [ 未存過 ] 判斷當前名字有沒有在name data
    if name in name_data:
        # [ 已存在 ] 判斷當前名字的year是否存在name_data
        if year in name_data[name]:
            # 判斷當前排名是否比現有排名靠前，如果有比較靠前，更新為「排名靠前的排名」
            if rank.isdigit() and int(rank) < int(name_data[name][year]):
                name_data[name][year] = rank
        else:
            # 當前名字的year「沒有」存在name_data，因此新增當前名稱year的key
            name_data[name][year] = rank
    else:
        # 當前名字「沒有」在name data，新增在name_data的字典裡
        name_data[name] = {year: rank}


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.
    """
    with open(filename, 'r') as f:
        for line in f:
            tokens = line.split(',')
            # 年份拿出來單獨處理：
            if len(tokens) == 1:
                year = tokens[0].strip()    # 刪除字串的頭尾空格 和 換行
            # tokenization
            else:
                rank = tokens[0].strip()    # 要加strip()不然排行的字串還是會處理不到頭尾空格
                m_name = tokens[1].strip()   # baby male name
                f_name = tokens[2].strip()   # baby female name

                # 增加男嬰兒的data
                add_data_for_name(name_data, year, rank, m_name)
                # 增加女嬰兒的data
                add_data_for_name(name_data, year, rank, f_name)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    # 設定 name_data 初始值為空字典
    name_data = {}
    for filename in filenames:
        add_file(name_data, filename)

    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string
    """
    # 設 names 初始值為空的列表
    names = []
    for name in name_data:
        if target.lower() in name.lower():  # 兩邊都要加上lower()使其ㄧ致才可以在搜尋名字時找到 A 和 a
            names.append(name)

    return names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
