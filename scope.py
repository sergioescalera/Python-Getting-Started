value = "this is a value"

def abc(x):
    n = 3
    print(value)
    print(x)
    print(n)


print("func abc")
abc(5)

print("global scope")

print(value)
#print(x)
#print(n)

def xyz(l):
    l.append(3)

m = [1, 2]

print(m)

xyz(m)

print(m)

def uv(i):
    i = i + 5
    print(i)
    return i

hh = 3

print (hh)

uv(hh)

print(uv(hh))

print(hh)

str_ = "this is "

def doSomethingCool(str1):
    str1 = str1 + "cool"
    print(str1)
    return str1

print(str_)
str_ = doSomethingCool(str_)
print(str_)




