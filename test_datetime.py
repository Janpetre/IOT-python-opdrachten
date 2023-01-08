from datetime import datetime
now=datetime.now()          # store current date + time in variable now
print(now.isoweekday())     # print the number of this day in a week
print(now)                  # print datetime object (it is automatically converted to a string)
print (int(now.timestamp()))      # convert to timestamp and print

ts = 1638529647
moment = datetime.fromtimestamp(ts)
print(moment.strftime('%Y-%m-%d')) # print as YYYY-mm-dd
                                   # see https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes