def remove_last(lst):
    lst.pop()
l=[]
n=int(input("enter number of elements"))
for i in range(n):
    item=int(input("enter element:"))
    l.append(item)
print("before elimination:", l)
remove_last(l)
print("after elimination:", l)    