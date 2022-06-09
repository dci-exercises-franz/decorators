
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


if __name__ == '__main__':

    greeting = input("How do you want to be greeted? ")
    print(greetings(greeting))

