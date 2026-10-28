# write a decorators logger that prints fuction is being called before the function runs use it to decorate a fuction say_hello() that prints "Hello"
def logger(func):
    def wrapper():
        print("Fuction is being called!")
        func()
    print("fuction is being called")
    func()

@logger
def say_hello():
    print("Hello")

say_hello