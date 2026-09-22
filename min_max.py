l=[]
n=int(input("enter number of elements"))
for i in range(n):
    item=int(input("enter element"))
    l.append(item)
min=l[0]
max=l[0]
for i in range(len(l)):
    if(l[i]<min):
        min=l[i]
    if(l[i]>max):
        max=l[i]
print("min element is:",min)
print("max element is:",max)
