
# Task 2 - What are you doing?

# Implementation of verbose decorator goes here...
def verbose(func):

    def wrapper(*args, **kwargs):

        if args and kwargs:
            arguments = args, kwargs
        elif kwargs:
            arguments = kwargs
        else:
            arguments = args

        return f"{func.__name__} invoked with {arguments} -> {func(*args, **kwargs)}"

    return wrapper

# Your code here

@verbose
def sum_two(a, b):
    return a + b

@verbose
def some_stuff(a, city):
    return f"The zip code of {city} is {a}"


if __name__ == "__main__":

    print(sum_two(1, 8))
    print(some_stuff(17489, city="Greifswald"))
