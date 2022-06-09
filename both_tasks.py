
# Task 1 - The Annoying Decorator


def annoying_decorator(func):

    def wrapper(*args, **kwargs):

        greeting = args[0]

        if greeting == "Hi":
            greeting_str = func("Don't use Hi! with me, please!")
        else:
            greeting_str = func(f"{greeting}, Sir.")
        return greeting_str

    return wrapper


@annoying_decorator
def greetings(greeting):
    return f"{greeting}"


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
def verbose_test(test_object):
    return test_object


if __name__ == '__main__':

    greeting = input("How do you want to be greeted? ")
    test_object = greetings(greeting)
    print(test_object)
    print(sum_two(1, 3))
    print(verbose_test(test_object))
