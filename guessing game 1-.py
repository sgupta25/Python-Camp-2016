try:
  n=5  
  while n >0:
    n = n -1  
    print "you have five tries to sink a battle ship"
    print " you have to guess 5 numbers between 1-20"
    print "if you hit a mine, the game is over"
    x = raw_input ("enter a number")
    x =  float (x)
    if x == 1:
        print 'no battle ship'
        print str(n) + ' more tries'
    if x == 2:
        print 'no battle ship'
        print str(n) + "more tries"
    if x == 3:
        print 'good job, battle ship found and sunk'
        print 'you win'
    if x == 4:
        print 'good job, battle ship found and sunk'
        print 'you win'
    if x == 5:
        print 'you hit a mine!'
        print 'game over!'
    if x == 6:
        print 'you hit a mine!'
        print 'game over!'
    if x == 7:
        print 'you hit a mine!'
        print 'game over!'
    if x == 8:
        print 'no battle ship'
        print str(n) + 'more tries'
    if x == 9:
        print 'no battle ship'
        print str(n) + ' more tries'
    if x == 10:
        print 'no battle ship'
        print str(n) + ' more tries'
    if x == 11:
        print 'you hit a mine!'
        print 'game over!'
    if x == 12:
        print 'good job, battle ship found and sunk'
        print 'you win'    
    if x == 13:
        print 'no battle ship'
        print str(n) + " more tries"
    if x == 14:
        print 'no battle ship'
        print str(n) + " more tries"
    if x == 15:
        print 'no battle ship'
        print str(n) + " more tries"
    if x == 16:
        print 'good job, battle ship found and sunk'
        print 'you win'
    if x == 17:
        print 'no battle ship'
        print str(n) + ' more tries'
    if x == 18:
        print 'no battle ship'
        print str(n) + ' more tries'
    if x == 19:
        print 'you hit a mine!'
        print 'game over!'
    if x == 20:
        print 'no battle ship'
        print str(n) + "more tries"
  
except:
    "error, type numeric values"
