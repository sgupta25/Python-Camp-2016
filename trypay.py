try:
    hours=input('how many hours did you work')
    hour = float(hours)
    if hour > 40:
        overhr = hour - 40
    rate=input('how much do you get pay a hour')
    rates = float(rate)
    if hour <= 40:
        pay = hour * rate
    if hour  > 40:
        pay=40*rate+ overhr*(1.5*rate)

    print pay

except:
       print"Sorry,that's not a number!" 
