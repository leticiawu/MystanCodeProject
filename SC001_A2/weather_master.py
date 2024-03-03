"""
File: weather_master.py
Name: Leticia
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# Constant representing the user inputs to exit the temperature input loop
QUIT = -1


def main():
	"""
	This program processes weather data to calculate:
	(1) highest temperature
	(2) lowest temperature
	(3) average temperature
	(4) the number of days with a cold alert
	"""
	print("stanCode \"Weather Master 4.0\"!")
	data = int(input("Next Temperature: (or -1 to quit)? "))

	if data == QUIT:
		print("No temperatures were entered.")
	else:
		# Set initial values
		highest_temp = data
		lowest_temp = data
		total = data
		# total: the sum of all temperature data entered
		num_data = 1
		# num_data: the count of temperature data entered

		# Check if the first data is a 'cold day'
		if data < 16:
			cold_day = 1
		else:
			cold_day = 0

		while data != QUIT:
			data = int(input('Next Temperature: (or -1 to quit)? '))
			if data == QUIT:
				break
			if data > highest_temp: 	# Update highest_temp if the current data is higher
				highest_temp = data
			if data < lowest_temp: 		# Update lowest_temp if the current data is lower
				lowest_temp = data
			if data < 16:				# Check if the data indicates a cold day and increment cold_day if true
				cold_day += 1
			total += data
			num_data += 1 				# Accumulate the total data for later calculations

		average = total / num_data
		print("Highest temperature = " + str(highest_temp))
		print("Lowest temperature = " + str(lowest_temp))
		print("Average = " + str(average))
		print(str(cold_day) + " cold day(s)")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
