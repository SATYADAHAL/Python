''''                    SEND
                        MORE                i.e    SEND + MORE = MONEY
                       ------
                        MONEY
                        
Every alphabet is assigned a inque number form 0-9, find the values for above alphabets that satisfy the above condition. '''
from IPython.display import clear_output
from itertools import permutations
str_1=input("Enter first string to add:  ")
str_2=input("Enter second string to add: ")
str_3=input ("Enter third string to add: ")
lst=[]
m=0
key_dict={}
def compare(d_c,str_):
    z=''
    for items in str_:
       z=z+d_c[items]
    return z
for i in str_1:
    if i not in lst:
        lst.append(i)
for j in str_2:
    if j not in lst:
        lst.append(j)
for k in str_3:
    if k not in lst:
        lst.append(k)
perm = permutations([1,2,3,4,0,5,6,7,8,9],len(lst))
for i in list(perm):
    for j in i:
        key_dict[lst[m]]=str(j)
        m=m+1
    if int(compare(key_dict,str_1))+int(compare(key_dict,str_2))==int(compare(key_dict,str_3)):
        print(str_1+"       ",compare(key_dict,str_1))
        print(str_2+"       ",compare(key_dict,str_2))
        print('-------')
        print (str_3+"       ",compare(key_dict,str_3))
        print()
        break
    m=0
    key_dict={}
