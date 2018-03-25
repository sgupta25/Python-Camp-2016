def addtwo(a,b):
    added = a + b
    return added
try:
    y=raw_input("What is your name?")
    n1=raw_input("What is your 1st number?")
    n2=raw_input("What is your 2nd number?")
    print "Those are the numbers I was thinking of too, "+y+"!"
    n1=float(n1)
    n2=float(n2)
    x = addtwo(n1,n2)
    print x
except:
    print "Please enter numbers only!"
