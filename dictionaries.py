d = {
    "m": 10,
    "x": 11
}

print(d)

d["m"] = 22
d["n"] = 5

print(d)

print(d.keys())
print(d.values())

d.pop("x")

print(d)

print(d.get("a"))
print(d.get("n"))

print(d["n"])

d.clear()

print(d)

z = d
print(id(d))
print(id(z))
