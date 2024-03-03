"""
File: prime_checker.py
Name: Leticia
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
	"""
	This is a console program allows users to check for primality.
	"""
	print("Welcome to the prime checker!")

	while True:
		n = int(input("n: "))
		# Input number to check for primality
		if n == EXIT:
			print("Have a good one!")
			break
		else:
			a = 2
			# Divisor for checking primality of 'n'
			while n > a:
				if n % a == 0:
					break
				else:
					a += 1
			if a == n:
				print(str(n) + " is a prime number.")
			else:
				print(str(n) + " is not a prime number.")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
