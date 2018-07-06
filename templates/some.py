import datetime
now = datetime.datetime.now()
print(now.year)
print(now.month)
if(1 <=now.month<=6):
    var = "Even"
else:
    var =  "Odd"
print(var)
