import datetime
d = str(datetime.datetime.now())[0:-10].replace(':','-') + '.txt'
print(d)
dd = datetime.datetime.now().timestamp()
print(dd)
print(datetime.datetime.now())