'''A while loop that takes numbers and calculates their average.'''
while True:
	'''Ask for the numbers to find the average of.'''
	numbers = input("Enter the numbers to average.\nEnter 'q' to quit. ")
	if numbers.lower() == 'q':
		break
	else:	
		'''convert input string to list of strings.'''
		numbers = numbers.split()

		'''convert list of strings to list of floats.'''
		lst = [float(x) for x in numbers]
		'''use input to formulate the average of the given numbers.'''

		total = sum(lst)
		div = len(lst)
		ave = total/div

		'''Print the result.'''
		print(f"The average of your numbers is: {ave}")
