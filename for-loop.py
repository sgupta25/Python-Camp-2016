count = 0
sum = 0

small = 100
print 'Before', small, count, sum
for item in [1, 2, 3, 4, 5]:
    count = count +1
    sum = sum + item
    if item < small:
        small = item
    print small, count, sum, item

    print 'After', small, count, sum, sum/count

