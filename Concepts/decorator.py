def my_deco(func):
    def wrapper():
        print("Decorator before calling function")
        func()
        print("Decorator after calling function")
    return wrapper


@my_deco
def hello():
    print("Hello world!")

@my_deco
def greet():
    print("Greetings from above!")


hello()
greet()
