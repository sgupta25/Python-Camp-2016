hours=raw_input("How many hours did you work?")
hours_float=float(hours)
payperhour=raw_input("How much money did you earn in 1 hour?")
payperhour_float=float(payperhour)
totalpay= hours_float * payperhour_float
print "You made", totalpay
