num=int(input("Enter No. Elements in List:"))
list1=[]
even=[]
fori in range(0,num):
    s=int(input("Enter Element in List : "))
list1.append(s)

fori in range(0,num):
    a=list1
if(a[i] % 2 == 0):
even.append(a[i])


print("Even Numbers in List: ",even)

