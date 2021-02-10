
import numpy as np
mylist = [2,4,6,8,10]
myarray = np.array(mylist)
# printing myarray
print("Before Deletion My Array :",myarray)
# printing the type of myarray
print(type(myarray))
#delete from any position
n = int(input("Enter Position from where u want to delete:"))
myarray = np.delete(myarray, n-1)
# printing the my_array
print("After Deletion My Array :",myarray)