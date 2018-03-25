def computepay(hour, rates):
    if hour > 40:
        overhr = hour - 40
    if hour <= 40:
        pay = hour * rate
    if hour  > 40:
        pay=40*rate+ overhr*(1.5*rate)

    return pay

hours=input('how many hours did you work')
hour = float(hours)

rate=input('how much do you get pay a hour')
rates = float(rate)

x = computepay(hour, rates)
print x

