import numpy as np

myarr = np.array([1,2,3],np.int8)
#print(myarr,myarr.shape)
#print(type(myarr))
#print(myarr.shape)

myarr2= np.array([[1,2,3]],np.int16)
#print(myarr2[0,1])
#print(myarr2.shape)
#print(myarr2.dtype)

#CREATION OF AN ARRAY
#OPTION 1-CONVERSION FROM OTHER PYTHON STRUCTURES
'''
listarray=np.array([[1,2,3],[2,3,4],[5,4,3]])
print(listarray[0][1])
print(listarray.dtype,listarray.size)
'''
'''
lst=np.array(( (1,2,3),(4,5,6) ))
#print(lst[0][1],lst.size,lst.T)
#print(lst.dtype)
'''

'''
#arange works same as range function at the time of working with for loop
x1=np.arange(0,15)
x2=np.arange(1,16)
print(x1,x2)
'''
#lspace= np.linspace(1,10,3) #1 is the inital point 10 is the final point 3 is the total data it should render to reach 10 (all data should be at equal distance)
#print(lspace)

#AXIS
# 1D only have axis=0
example2=np.array([5,2,3])
print(example2.sum(axis=0)) #10
#axis=0 2D STATEMENT-stands for 1st element / every 0th index at every dimension
example=np.array([[1,2,3], #1 is on  axis 0
                [1,2,4], #1 is on  axis 0
                [1,4,2]])#1 is on axis 0
print(example.sum(axis=0)) #[3 8 9]
#axis=1 2D STATEMENT-stands for the objects inside the datatype
print(example.sum(axis=1)) #[6 7 7]
