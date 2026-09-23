def change_string(str):
    str1=str[1:]
    str2="X"+ str1
    return str2
my_str=input("enter string")

print("before reassignment :", my_str)
reassign =change_string(my_str)
print("after reassignmnet:", reassign)    