def add_entry(dic):
    dic["number"]=8765343
dic={}
n= int(input("enter number of entries:"))
for i in range(n):
    key=input("enter key")
    value=input("enter value")
    dic[key]=value
add_entry(dic)
print("appended dictionary is:",dic) 
def reassign(dic):
    dic["name"]="isha"
    print("updated dictionary is:", dic)
reassign(dic)    
