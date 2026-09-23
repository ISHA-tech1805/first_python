def fact(n):
    fact=1
    for i in range(1, n+1):
        fact=fact*i
    print("factorial of n is:", fact)
n =int(input("enter number "))
fact(n)   