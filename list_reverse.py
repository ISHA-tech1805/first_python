l=[]
n=int(input("enter number of elements"))
for i in range(n):
    item=int(input("enter element:"))
    l.append(item)
print("reversed list:")    
for i in range(n//2):
    temp=l[i]
    l[i]=l[n-i-1]
    l[n-i-1]=temp
    
for item in l:
    print(item)
    
