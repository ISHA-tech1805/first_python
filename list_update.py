l=[]
for i in range(5):
    item=input("enter element:")
    l.append(item)
print("second element is:",l[1])#display name at index 1 i.e.,2nd value
print("fourth element is:",l[3])#display name at index 3 i.e., 4th value
l[4]="mango"#update last index name to mango
print(l)#display the updated list
