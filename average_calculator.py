'''Ask for the numbers to find the average of'''
numbers = input("What are the numbers to calculate?")

'''convert input string to list of strings.'''
numbers = numbers.split()

'''convert list of strings to list of floats.'''
lst = [float(x) for x in numbers]

'''use input to formulate the average of the given numbers.'''

total = sum(lst)
div = len(lst)
ave = total/div

print(f"The average of your numbers is: {ave}")