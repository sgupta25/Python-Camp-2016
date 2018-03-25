try:
    found = False
    print  'before', found
    x = raw_input("Enter a number. 9,41,12,3,74,15")
    x = int (x)
    for value in [ 9,41,12,3,74,15]:
        if value == x:
            found = True
            print found, value
    print 'after', found
except:
 print 'please enter a number'

