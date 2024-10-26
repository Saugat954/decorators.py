# Decorators in python
#they are the tool in python which hepls to modify the functions

def greet(function):
    def modifyFunction(*args, **kwargs):
        print("Good Morning")
        function(*args, **kwargs)
        print("Thanks for using this function")
    return modifyFunction


@greet
def hello():
    print("Hello World")

hello()
def add(a,b):
    print(a+b)

greet (add)(3,5)