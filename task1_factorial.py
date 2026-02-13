# Function to calculate factorial of a number
def factorial(n):
    
    result = 1         # initialize result

    # loop from 1 to n
    for i in range(1, n + 1):
        result *=i      # multiply each number
    return result       # return final factorial
    
# taking input from user    
num= int(input("Enter a number :"))

# calling the factorial function
fact = factorial(num)

# displaying the result 
print(f"Factorial of {num} is : {fact}")
