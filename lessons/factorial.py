# Recursive implementation of n! (n-factorial) calculation
def factorial(n):
    # Base case: n = 0 or 1
    if n <= 1:
        return 1

    # Recursive case: n! = n * (n - 1)!
    return n * factorial(n - 1)

print(factorial(5))


# uncomment to see the recursive steps printed out
""" # Recursive implementation of n! (n-factorial) calculation
def factorial(n):
    # Print the current value of n
    print(f"Entering factorial({n})")
    
    # Base case: n = 0 or 1
    if n <= 1:
        print(f"Base case reached: factorial({n}) = 1")
        return n

    # Recursive case: n! = n * (n - 1)!
    result = n * factorial(n - 1)
    print(f"Returning: factorial({n}) = {result}")
    return result

# Print the result of factorial(5)
print("Final result:", factorial(5)) """