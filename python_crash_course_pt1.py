# python
print (10)
print (2*3)
print (1/8)
print (4%2)
print (2+3*5+5)
print ((2+3)*(5+5))

name_of_var  = 2

x  = 1
y = 2

z = x + y

print(z)

print(" I don't care")


name = 'Felipe'
print ("Hello my name is {}".format(name))

number = 12

print("Hi my name is {x} and my number is {y}".format(x=name, y=number))

#LIST
my_list = ['hi', 2, 3]
my_list.append(4)

print(my_list[0])

my_list = ['a','b','c']
#starts up to not included to
print (my_list[0:2])
print (my_list[2:])

nested = [1,2,['a','b']]
print(nested[2][0])

#dictionary
d = {'key':10, 'key2':'seccond types'}
print(d['key2'])

#tooples symilar to arrays
t = (1,2,3)
my_list = [1,2,3]
#tooples are unchangeble
my_list[0] = 'new'
print(my_list)
# The following gives error
# t[0] = 'new'
# print(t)


my_list = set([1,1,1,1,2,2,2,2,3,3,3])
print(my_list)
print(1 < 2)
