def addtwo(a, b):
    added = a + b
    return added
try:
    a = raw_input ('Enter your First number')   
    a = float(a)
    b = raw_input ('Enter your Second number')
    b = float(b)
    x = addtwo(a , b)
    print x
except: print ('Please Enter a Numeric Value')

       
def subtwo (a, b):
    subtracted = a - b
    return subtracted
try:
    a = raw_input ('Enter your First number')
    a = float(a)
    b = raw_input ('Enter your Second number')
    b = float(b)
    x = subtwo (a , b)
    print x
except: print ('Please Enter a Numeric Value')


def multitwo (a, b):
    multiplied= a * b
    return multiplied
try:
    a = raw_input ('Enter your First number')
    a = float(a)
    b = raw_input ('Enter your Second number')
    b = float(b)
    x = multitwo (a , b)
    print x
except: print ('Please Enter a Numeric Value')


def dividetwo (a, b):
    divieded= a / b
    return divieded
try:
    a = raw_input ('Enter your First number')
    a = float(a)
    b = raw_input ('Enter your Second number')
    b = float(b)
    x = dividetwo (a , b)
    print x
except: print ('Please Enter a Numeric Value')


def exponenttwo (a, b):
    exponent= a ** b
    return exponent
try:
    a = raw_input ('Enter your First number')
    a = float(a)
    b = raw_input ('Enter your Second number')
    b = float(b)
    x = exponenttwo (a , b)
    print x
except: print 'Please Enter a Numeric Value'
