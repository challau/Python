def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

'''
It replace the function say_hello with this:
def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper

'''
@repeat(7)
def say_hello(a):
    print(f"Hello {a}")

say_hello("uday")
