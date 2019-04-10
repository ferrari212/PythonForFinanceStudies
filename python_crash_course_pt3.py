def my_func(param = 'default'):
    """
    docstrings goes here!
    """
    return param*5

x = my_func(5)
print(x)

# lambda var: var*2

seq = [1,2,3,4,5]

print (list(map(lambda var:var*2, seq)))

# lambda num: num%2 == 0

print (list(filter(lambda num: num % 2 == 0, seq)))


#methods
st = 'hello my name is Sam'

print(st.lower())
print(st.upper())

tweet = "Go Sports! #cool"

print(tweet.split('#'))

d = {'key':10, 'key2':'seccond types'}

print(d)
print(d.keys())
print(d.items())

my_list = [1,2,3]
my_list.append(4)
print(my_list)

my_list.pop()
print(my_list)

print (1 in my_list)
