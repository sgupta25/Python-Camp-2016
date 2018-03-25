
def addtwo(a, b):
    added= a+b
    return added
try:
    a=input ('first number')
    b=input('2nd number')
    c=input('opperation 1= +     2= -      3= *   4=/ ')
    a=float(a)
    b=float(b)
    c=int(c)
    if c==1:
        x=addtwo(a,b)
        print (x)
    elif c==2:
        x=(a-b)
        print (x)
    elif c==3:
        x=(a*b)
        print (x)
    elif c==4:
        x=(a/b)
        print (x)
    else:
        print (a**b)

except:
    print ('enter number.NUMBER')

