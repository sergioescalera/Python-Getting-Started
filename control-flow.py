z = 1 + 1j

while abs(z) < 100:
    z = z**2 + 1

print(z)

print(range(5))

r = range(4)
a = reversed(r)
print(type(r))
print(type(a))
print(a)

for i in a:
    print(i)

for word in ('cool', 'powerful', 'readable'):
    print('Python is %s' % word)

for j in [1, 1, 2, 2]:
    print(j)

dict = {
"a": 1,
"b": 2,
"c": 3
}

for k in dict:
    print(k)

print(type([]) is list)

