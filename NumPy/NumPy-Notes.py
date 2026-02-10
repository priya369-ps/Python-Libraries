import numpy as np
print("checking version of numpy:")
print(np.__version__)

#Printing 1D array and attributes
arr1=np.array([1,2,3])
print(arr1)
print(f"size of an array:{arr1.size}")
print(f"shape of an array:{arr1.shape}")
print(f"dimension of an array:{arr1.ndim}")
print(f"datatype of an array:{arr1.dtype}")

#Printing 2D array and attributes
arr2=np.array([[1,2,3],[4,5,6],[6,7,8]])
print(arr2)
print(f"size of an array:{arr2.size}")
print(f"shape of an array:{arr2.shape}")
print(f"dimension of an array:{arr2.ndim}")
print(f"datatype of an array:{arr2.dtype}")

#Printing 2D array and attributes
arr2=np.array([[1,2,3],[4,5,6],[6,7,8],[9,10,11],[12,13,14],[15,16,17]])
print(arr2)
print(f"size of an array:{arr2.size}")
print(f"shape of an array:{arr2.shape}")
print(f"dimension of an array:{arr2.ndim}")
print(f"datatype of an array:{arr2.dtype}")

#Printing 3D array and attributes
arr3=np.array([[[1,2,3],[4,5,6],[6,7,8]],[[9,10,11],[12,13,14],[15,16,17]]])
print(arr3)
print(f"size of an array:{arr3.size}")
print(f"shape of an array:{arr3.shape}")
print(f"dimension of an array:{arr3.ndim}")
print(f"datatype of an array:{arr3.dtype}")

#zeros
zero_arr=np.zeros((3,2))
print(zero_arr)
#ones
one_arr=np.ones((3,2))
print(one_arr)
#Full
full_arr=np.full((3,2),9)
print(full_arr)

#empty
emp=np.empty(3)
print(emp)

#range
ran=np.arange(2,20,5)
print(ran)
#linspace
lin=np.linspace(1,20,3)
print(lin)


#Printing random numbers
random=np.random.rand(1,10)
print(random)
print(random.size)

#Printing integer number
randomeint=np.random.randint(1,10,(3,3))
print(randomeint)

#Slicing
slice=np.array([1,2,3,4,5,6,7,8,9])
print(slice[2:6])
print(slice[:6])
print(slice[2:])
print(slice[::-1])
print(slice[2:6:2])
print(slice[0::3])
print(slice[-1::])

#2d slicing
print(arr2)
print(arr2[3][2])
print(arr2[:,2])
print(arr2[3,:])
print(arr2[::2,2])
print(arr2[::,1:2])

#Reshaping
print(arr1.reshape(3,1))
arr2=np.array([[1,2,3],[4,5,6],[6,7,8],[9,10,11],[12,13,14],[15,16,17]])
print(arr2.reshape((2,9)))


#Flattening
print(arr2.flatten())

#Stacking and Splitting
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.vstack((a,b)))  #row
print(np.hstack((a,b)))  #col

spli=np.hsplit(a,3)   #ValueError: array split does not result in an equal division if (a,2)
a1=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
spliv=np.vsplit(a1,2) 
print(spliv)


#MATHEMATICAL OPERATIONS
print(arr1+2)
print(arr1-2)
print(arr1*2)
print(arr1/2)
print(arr1//2)

print(np.sqrt(arr1))
print(np.square(arr1))
print(np.sin(arr1))

arrr2=np.array([4,5,6])
print(np.add(arr1,arrr2))
print(np.subtract(arr1,arrr2))
print(np.multiply(arr1,arrr2))
print(np.divide(arr1,arrr2))

#Dot
print(np.dot(arr1,arrr2))
print(np.transpose(arr2))

#statistical
print(np.mean(arr1))
print(np.median(arr1))
#print(np.mode(arr1))
print(np.std(arr1))

#comparison
print(arr1==arrr2)
print(np.array_equal(arr1,arrr2))


#handling nan and inf
handling=np.array([1,2,3,4,np.nan,5,6,7,np.inf,8,9,-np.nan,-np.inf])
print(handling)
print(np.isnan(handling))
print(np.isinf(handling))

print(np.nan_to_num(handling))

print(handling)
print(np.nan_to_num(handling,nan=0.0,posinf=1,neginf=-1))
#print(mask)

#saving
np.save("my_handling.npy",handling)

#loading
loaded=np.load('my_handling.npy')
print(loaded)