##Odd Magic Square Solving
from array import *
def add_list(a,b):
    out=[]
    for i in range(len(a)):
        out.append(a[i]+b[i])
    return out
def transpose(lst1):
    temp_lst=[]
    t_lst=[]
    for i in range(len(lst1)):
        for item in lst1:
            temp_lst.append(item[i])
        t_lst.append(temp_lst)
        temp_lst=[]
    return t_lst
dim=int(input("Enter the size: ")) 
length=len(str(dim*dim))
dim=dim-1
arr=[]
for i in range(0,dim*2+1):
    arr.append([])
    for j in range(0,dim*2+1):
        arr[i].append(0)
subt_var=0
x=0
y=0
while x!=dim+1:
        arr[(dim*2)-x][dim+x]=x+1
        x=x+1
subt_var=1
x=x+1
while subt_var<=dim:
    while y!=(dim+1):
        arr[(dim*2)-subt_var-y][(dim-subt_var)+y]=x
        y=y+1
        x=x+1
    subt_var=subt_var+1
    y=0
slice_1=int((dim+1)-(dim/2))
slice_2=int((dim+1)+(dim/2))

def rolling(arr):
    index_row=0
    for items in arr:
        if arr.index(items)<=int(dim/2-1):
            x=arr.index(items)
            arr[x+dim+1]=add_list(arr[x+dim+1],items)
        elif arr.index(items)>slice_2-1:
            x=arr.index(items)
            arr[x-dim-1]=add_list(arr[x-dim-1],items)
        else:
            continue
    return arr

arr1=rolling(arr)
arr2=transpose(arr1)
arr3=rolling(arr2)
arr4=transpose(arr3)
new_arr=[]
new_arr=[]
for items in arr4:
    if arr4.index(items)+1>=slice_1 and arr4.index(items)+1<=slice_2:
        new_arr.append(items[int(slice_1)-1:int(slice_2)])
for items in new_arr:
    for item in items:
        print(str(item).zfill(length),end="  ")
    print()
    
