# decorators

Exercises
1. The Annoying Decorator
Suppose you have the following function:

def greetings():
    return "Hi"
Create the annoying_decorator that will print the greeting returned by the decorated function and check if the returned greeting starts with Hi, if yes it will print Don't use Hi! with me, please!. If you use any other greeting, it will print Hello, Sir..

Use the code bellow as a starting point:

def annoying_decorator(func):
    def wrapper():

    # Your code here...

    return wrapper


@annoying_decorator
def greetings():
    return "Hi"


if __name__ == '__main__':
    greetings()
When running the finished program above, you must see the following in the screen:

Hi!
Don't use Hi! with me, please!
If greetings return something like hello, the program must print:

Hello!
Hello, Sir!


2. What are you doing?
Create a decorator that prints the arguments passed to the function and the returned value on the screen. This could be useful for debugging purposes if you want to look at the values handled by a function. You decorate the function you want to expect, and you will have the input and output values from the function printed out on the screen.

If I have the function:

def sum_two(a, b):
    return a + b
when we use the decorator on that function and invoke it, it must print:

# Implementation of verbose decorator goes here...
def verbose(func):


# Your code here

@verbose
def sum_two(a, b):
    return a + b


if __name__ == "__main__":
    sum_two(1, 3)
The program above must print on the screen:

sum_two invodek with (1, 3) -> 4
Implement the verbose decorator.
