def double_result(func):
    def wrapper():
        print("executiong before double")
        sum=func()
        print("after double:", 2*sum)
    return wrapper    
@double_result
def add():
    a=int(input("enter number"))
    b=int(input("enter number"))
    result=a+b
    print("sum is:", result)
    return result
add()    