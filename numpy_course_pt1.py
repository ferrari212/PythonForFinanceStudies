import numpy as np

my_list = [1, 2, 3]
x = np.array(my_list)

print (type (x))

#Create a matrix
my_matrix = [[1,2,3], [4,5,6], [7,8,9]]
print (np.array(my_matrix))

#Create a range
list (range(0,5))
print (np.arange(0,5))
print (np.arange(1,11,2))

#create a matrix of zeros
print (np.zeros(3))
print (np.zeros((3, 2)))

#create a matrix of ones
print (np.ones(3))
print (np.ones((3, 2)))

#linspace
print (np.linspace(0, 10, 30))

#identity matrix: square matrix
print (np.eye(4))

#randon matrix
#same probability of getting a number
print (np.random.rand(1))
print (np.random.rand(5,5))
#normal distribution (gaussian distribution)
print (np.random.randn(5,5))
#randon int from a interval
print (np.random.randint(1,100))
print (np.random.randint(1,100,10))

#reshape array
arr = np.arange(25)
ranarr = np.random.randint(0,50,10)
print (arr)
print (arr.reshape(5,5))

#shape attribute
print (arr.shape)

#data type
print (arr.dtype)

#max number
print (ranarr.max())
#index location of maximum
print (ranarr.argmax())
#min number
print (ranarr.max())
#index location of min
print (ranarr.argmin())
