# Task 2 - What are you doing?


# Implementation of verbose decorator goes here...
def verbose(func):

    def wrapper(*args):

        a = args[0]
        b = args[1]
        return f"{func.__name__} invoked with ({a, b}) -> {func(*args)}"

    return wrapper

# Your code here

@verbose
def sum_two(a, b):
    return a + b


if __name__ == "__main__":

    print(sum_two(1, 3))
