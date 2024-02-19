import datetime
x = datetime.datetime.now()
yesterday = (x + datetime.timedelta(days=1)).strftime("%A")
tomorrow = (x -datetime.timedelta(days=1)).strftime("%A")
print (x.strftime("%A"))
print (yesterday)
print (tomorrow)