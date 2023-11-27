"""
File: class_reviews.py
Name: 吳宇韻
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

EXIT = -1   # The number will stop user entering or show 'No class scores were entered' at first


def main():
    """
    This program help stanCode to compute the highest,
    lowest and average scores in class SC001 and SC101
    for users' inputs.
    """
    class_name = (input("Which class? "))

    if class_name == str(EXIT):
        print("No class scores were entered")
    else:
        class_name_upper = class_name.upper()

        max_001 = 0
        min_001 = 0
        count_001 = 0
        total_001 = 0

        max_101 = 0
        min_101 = 0
        count_101 = 0
        total_101 = 0

        if class_name_upper == "SC001":
            score_001 = int(input("Score: "))
            max_001 = score_001
            min_001 = score_001
            count_001 += 1
            total_001 += score_001

        if class_name_upper == "SC101":
            score_101 = int(input("Score: "))
            max_101 = score_101
            min_101 = score_101
            count_101 += 1
            total_101 += score_101

        while True:
            class_name = (input("Which class? "))
            if class_name == str(EXIT):
                break
            else:
                if class_name_upper == "SC001":
                    score_001 = int(input("Score: "))
                    if score_001 > max_001:
                        max_001 = score_001
                    if score_001 < min_001:
                        min_001 = score_001

                    count_001 += 1
                    total_001 += score_001

                if class_name_upper == "SC101":
                    score_101 = int(input("Score: "))
                    if score_101 > max_101:
                        max_101 = score_101
                    if score_101 < min_101:
                        min_101 = score_101

                    count_101 += 1
                    total_101 += score_101

        if count_001 == 0:
            print("=============SC001=============")
            print("No score for SC101")

        if count_001 >= 1:
            avg_001 = total_001 / count_001
            print("=============SC001=============")
            print("Max (001): " + str(max_001))
            print("Min (001): " + str(min_001))
            print("Avg (001): " + str(avg_001))

        if count_101 == 0:
            print("=============SC101=============")
            print("No score for SC101")

        if count_101 >= 1:
            avg_101 = total_101 / count_101
            print("=============SC001=============")
            print("Max (101): " + str(max_101))
            print("Min (101): " + str(min_101))
            print("Avg (101): " + str(avg_101))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
