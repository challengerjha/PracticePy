# Print FizzBuzz (Classic Amazon Question)

# Problem
# Print numbers from 1 to n:

# "Fizz" if divisible by 3

# "Buzz" if divisible by 5

# "FizzBuzz" if divisible by both

def fizzBuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
            