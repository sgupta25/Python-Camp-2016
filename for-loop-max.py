a = raw_input("Enter a number.")
a = float(a)

b = raw_input("Enter a number.")
b = float(b)

c = raw_input("Enter a number.")
c = float(c)

d = raw_input("Enter a number.")
d = float(d)

e = raw_input("Enter a number.")
e = float(e)












large = -1
print 'Before', large
for item in [a, b, c, d, e]:
    if item > large:
        large = item
    print large, item

    print 'After', large

