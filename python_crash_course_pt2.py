print (1==2)

print( (1==1) and not (1==2))

if 1==2:
    print('hello')
elif 2==2:
    print('true')
else:
    print('if statement was not true')

seq = [1,2,3,4,5,6]

#loops
for item in seq:
    print(item)

for item in seq:
    print('hello')

for jelly in seq:
    print(jelly)

for jelly in seq:
    print(jelly**2)

#while loops
i = 1
while i < 5:
    print('i is currently {}'.format(i))
    i = i + 1

#range()

print(range(5))

for item in range(0,20,2):
    print (item)

#list
list(range(1,11))

#list comprehension
x = [1,2,3,4]

out = []
for num in x:
    out.append(num**2)
print(out)

print([num**2 for num in x])
