# This is the recursive implementation to calculate the n-th Fibonacci Number
def fibonacci(n):
	# base case: n=0 or n=1
	if n <= 1:
		return n
		
	# recursive case: fib(n) = fib(n-1) + fib(n-2)
	return fibonacci(n-1) + fibonacci(n-2)

