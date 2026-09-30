# string formatting

template = "Dear {}, You are awesome. Take this {}$ bag"
a = "Jhon"
a1 = 10000
b = "Jack"
b1 = 1000
c = "Marie"
c2 = "300"

s1 = template.format(a,a1)
print(s1)

print(f"{a} you are awesome and take this {a1}$ bag")


# ord() and chr() => character Encoding

print(ord('A'))
print(chr(65))
print(ord('c'))
print(chr(98))
