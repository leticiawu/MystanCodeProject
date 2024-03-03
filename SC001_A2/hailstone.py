"""
File: hailstone.py
Name: Leticia
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program generates a Hailstone sequence
    and counts the steps taken to reach the value 1.
    """
    print("This program computes Hailstone sequences.")
    print()
    n = int(input("Enter a number: "))
    steps = 0
    # steps: indicates operation counts from n to 1

    while n > 1:
        if n % 2 == 1:
            next_n = 3*n+1
            # next_n: the next value of n calculated by using the formula
            print(str(n) + " is odd, so I make 3n+1: " + str(next_n))
            n = next_n
        elif n % 2 == 0:
            next_n = n//2
            print(str(n) + " is even, so I take half: " + str(next_n))
            n = next_n
        steps += 1
    if steps > 0:
        print("It took " + str(steps) + " steps to reach 1.")
    if steps == 0:
        print("It took 0 steps to reach 1.")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
