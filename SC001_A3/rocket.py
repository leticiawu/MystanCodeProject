"""
File: rocket.py
Name: Leticia
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 10


def main():
    """
    This is a console program that draws ASCII art - a rocket.
    The size of rocket is determined by a constant defined as
    SIZE at top of the file.
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    for i in range(SIZE):
        space = " " * (SIZE - i)
        slash = "/" * (i + 1) + "\\" * (i + 1)
        result = space + slash + space
        print(result)
    #  問：請教寫法：spaces, slash + spaces已是文字串，那我是否可以直接用 +）
    #  問：spaces = " " * (SIZE - i)? 文字串的表達方式是否正確，還是有更好的style


def belt():
    result = "+"
    for i in range(SIZE):
        equal = "=" * 2
        result += equal
    result += "+"
    print(result)


def upper():
    for i in range(SIZE):
        result = "|"
        dot = "." * (SIZE - i - 1)
        slash = "/\\" * (i + 1)
        result += dot + slash + dot
        result += "|"
        print(result)


def lower():
    for i in range(SIZE):
        result = "|"
        dot = "." * i
        slash = "\\/" * (SIZE - i)
        result += dot + slash + dot
        result += "|"
        print(result)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
