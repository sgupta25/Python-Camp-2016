def addtwo (a, b):
    added = a + b
    return added
def subtracttwo (c,d):
    subtracted = c - d
    return subtracted
def multtwo (e,f):
    multed = e * f
    return multed
def divtwo (g,h):
    dived = g / h
    return multed

try:
    z = raw_input ("what operation would you like(use first two letters of the operation)")   
    if 'ad':
        a = raw_input ('enter first number')
        a = float (a)
        b = raw_input ('enter second number')
        b = float (b)
        x = addtwo (a,b)
        print x

    if 'su':
        c = raw_input ('enter firct number')
        c = float (c)
        d = raw_input ('enter second number')
        d = float (d)
        y = subtracttwo (c,d)
        print y

    if 'mu':
        e = raw_input ('enter first number')
        e = float (e)
        f = raw_input ('enter second number')
        f = float (f)
        w = multtwo (e,f)
        print w

    if 'di':
        g = raw_input ('enter first number')
        g = float (g)
        h = raw_input ('enter second number')
        h = float (h)
        v = divtwo (g,h)
        print v

except: print("error, enter numeric value")

 
