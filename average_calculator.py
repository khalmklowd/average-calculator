'''A while loop that takes numbers and calculates the average.'''
while True:
    # Ask for the numbers to find the average of.
   
   
    numbers = input("Enter the numbers to average.\nEnter 'q' to quit. ")
    if numbers.lower() == 'q':
        break

    # Convert input string to list of strings.
    numbers = numbers.split()

    # Convert list of strings to list of floats.
    try:
        lst = [float(x) for x in numbers]


        # Use input to formulate the average of the given numbers.
        total = sum(lst)
        div = len(lst)
        avg = total/div

        # Print the result.
        print(f"The average of your numbers is: {avg}")

    except ValueError:
        print("please type only numbers.")
    

    
