def my_decorator(func):
    def wrapper():
        print("calling function")
        func()
        print("after calling")
    return wrapper
    

@my_decorator
def square():
    num=int(input("enter number"))
    print("square is:", num*num)
square()    