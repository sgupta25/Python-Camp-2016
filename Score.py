try:
    score= raw_input("Please enter your score.")
    score=float(score)
    if score >= .9:
        print "A"
    elif score >= .8:
        print "B"
    elif score >= .7:
        print "C"
    elif score >= .6:
        print "D"
    else:
        print "F"
except:
    print "please enter a number"
