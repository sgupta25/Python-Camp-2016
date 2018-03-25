n = 5
while n > 0:
    x = raw_input ('enter number')
    x = float (x)
    y = raw_input ('enter another number')
    y = float (y)
    z = raw_input ('enter another number')
    z = float (z)
    W = raw_input ('enter another number')
    W = float (W)
    v = raw_input ('enter another number')
    v = float (v)
    a = raw_input('what operation would you like (lo = 1,gr = 2,avg = 3,rg = 4)')
    a = int (a)
    if a == 1:
        Smallest = 3000
        for the_num in [x,y,z,W,v]:
            if the_num < Smallest:
                Smallest = the_num
            print Smallest, the_num
            print 'The smallest number is', Smallest
    if a == 2:
        Largest = -1
        for the_num in [x,y,z,W,v]:
            if the_num > Largest:
                Largest= the_num
            print Largest, the_num
            print 'The largest number is', Largest      
    if a == 3:
        count = 0
        total = 0
        print 'before', count
        print 'before', total
        for the_num in [x, y , z , W, v]:
            total = total + the_num
            count = count + 1
            total= float (total)
        average = total/count
        print total
        print count
        print ("the average is"), average
    if a == 4:
        Smallest = 3000
        for the_num in [x,y,z,W,v]:
            if the_num < Smallest:
                Smallest = the_num
        Largest = -1000
        for the_nums in [x,y,z,W,v]:
            if the_nums > Largest:
                Largest = the_nums
        Range = Largest - Smallest
        print 'the range is', Range
    



    
