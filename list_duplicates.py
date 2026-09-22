#input list and remove duplicates
l=[]
k=[]
n=int(input("enter number of elements"))
for i in range(n):
    item=int(input("enter element:"))
    l.append(item)
unique_list=set(l)
for item in unique_list:
    print(item)
    
    
