import turtle
import json
import requests
from datetime import datetime

url= "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m" #URL API meteodata
data = requests.get(url)          #http status code opvragen 


# print(data)                     #print status code
# print(data.text)                #data in een string

# tt=json.loads(data.text)        #string omzetten naar dictionary
# print(type(tt))                   #type is een dictionary

# pp=json.dumps(tt,indent=2)      #dictionary omzetten naar string
# print(type(pp))                  #type is een string


tt=data.json()           # geeft hetzelfde resultaat als json.loads
print(tt)                #type is een dictionary




listtijd = tt['hourly']['time']
listtemp = (tt['hourly']['temperature_2m'])

now = (datetime.now())
print(now)
timestamp_einde = int(now.timestamp())
tijd_begin = tijd[0]


# print (max(temp))
# print (min(temp))

for i in range(len(tt['hourly']['temperature_2m']):
    pen goto(x[i],y[i])



# for time in tt.items():
#     print(time)

# print(tt["hourly"]["temperature_2m"])

    