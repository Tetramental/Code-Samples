listPrimes = []                                          # Create an empty list
isNumber = False                                         # User has not typed a valid integer yet
print("Welcome to Prime Generator")
while not isNumber:                                      # While user has not typed a valid integer
    try:                                                 # Check if user input is valid
        user_input = int(input("Enter a number:\n"))     # Check for user input and cast to integer data type
        isNumber = True                                  # If number is valid integer, exit out of while loop
    except ValueError as v:                              # If user_input is not a valid integer, cast an exception
        print("", end = "")                              # Print nothing

isPrime = True                                           # Create a check for each number

for numbers in range(2, (user_input + 1)):               # Run through every number from 2 to user input
    for numbersSmaller in range((numbers - 1), 1, -1):   # Run through every number below user input to 2
        if numbers % numbersSmaller == 0:                # If the remainder is EVER 0
            isPrime = False                              # The check is off
    if isPrime:                                          # If the check is on,
        listPrimes.append(numbers)                       # Add to empty list (because it's a prime number BECAUSE the check in on it)
    else:                                                # Otherwise,
        isPrime = True                                   # If the check if off, turn the check back on for the next round of numbers
        
listPrimes.sort()                                        # Sort the list of prime numbers from lowest to highest (just in case)
for i in listPrimes:                                     # For every element in the list of primes,
    print(i, "is a prime number.")                       # Print the prime number with a statement