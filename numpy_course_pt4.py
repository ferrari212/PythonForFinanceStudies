# 1)
# Arrays
import numpy as np

# 2)
print (np.zeros(10))

# 3)
print (np.ones(10))

# 4)
print (np.ones(10)*5)

# 5)
print (np.arange(10,51))

# 6)
print (np.arange(10,51,2))

# 7)
print (np.arange(0,9).reshape(3,3))

# 8)
print (np.eye(3))

# 9)
print (np.random.rand(1))

# 10)
print (np.random.rand(5,5))

# 11)
print (np.linspace(0.01, 1, 100))

# Matrixes
# 12)
mat1 = np.arange(1,26).reshape(5,5)
print (mat1)

# 13)
mat2 = mat1
mat2 = np.delete(mat2, 0, 1)
mat2 = np.delete(mat2, 0, 0)
mat2 = np.delete(mat2, 0, 0)
print (mat2)

# 14)
print(mat1[3,4])

# 15)
mat3 = mat1
mat3 = [mat1[0][1], mat1[2][1], mat1[3][1]]
mat3 = np.array(mat3)
print (mat3)

# 16)
print (mat1[4,:])

# distribution
# 17)
print (mat1.sum())
print (mat1.size)

# 18)
avg_matrix = np.ones((5,5))*mat1.sum()/mat1.size
deviation = (avg_matrix-mat1)**2
deviation = deviation.sum()/mat1.size
deviation = deviation**(0.5)
print (avg_matrix)
print (deviation)
#easy way is using the function
print (mat1.std())


# 19)
print (mat1.sum(axis=0))
