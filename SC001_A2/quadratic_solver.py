"""
File: quadratic_solver.py
Name: Leticia
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	This is a console program for users to compute
	the roots of equation.
	"""
	print("stanCode Quadratic Solver!")
	a = float(input("Enter a: "))
	b = float(input("Enter b: "))
	c = float(input("Enter c: "))
	x = b ** 2 - 4 * a * c
	# x represents the root values

	if x > 0:
		y = math.sqrt(x)
		root_1 = (-b + y) / (2 * a)
		root_2 = (-b - y) / (2 * a)
		print("Two roots: " + str(root_1) + ", " + str(root_2))
	elif x == 0:
		root = -b / (2 * a)
		print("One root: " + str(root))
	else:
		# x < 0
		print("No real roots")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
