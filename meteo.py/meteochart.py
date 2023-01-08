import requests
import json
import turtle
from datetime import datetime

# def input_gebruiker(plaats):
    # dictionary coordinaten 3 plaatsen 
    # coord{
    #     "Antwerpen": {"latitude":51.22,"longitude": 4.40},
    #     "Londen" : {"latitude":51.251,"longitude": -0.13},
    #     "New-York" : {"latitude": 40.71,"longitude": -74.01}
    #     }
    

def meteodata():

    url= "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m" #URL API meteodata
    data = requests.get(url)          #http status code opvragen 


    print(data)                     #print status code
    print(data.text)                #data in een string

    tt=json.loads(data.text)        #string omzetten naar dictionary
    print(type(tt))                   #type is een dictionary

    pp=json.dumps(tt,indent=2)      #dictionary omzetten naar string
    print(type(pp))                  #type is een string


    tt=data.json()           # geeft hetzelfde resultaat als json.loads
    print(tt)                #type is een dictionary

    listtijd = tt['hourly']['time']
    listtemp = tt['hourly']['temperature_2m']

    now = (datetime.now())
    print(now)
    timestamp_einde = int(now.timestamp())
    

    # print (max(temp))
    # print (min(temp))

    # for i in range(len(tt['hourly']['temperature_2m']):
    #     pen goto(x[i],y[i])



    # for time in tt.items():
    #     print(time)

    # print(tt["hourly"]["temperature_2m"])

    # def tekenen_scherm():

def X_as():

    turtle.setup (width=500, height=500, startx=0, starty=-1)
    turtle.getscreen()
    t = turtle.Turtle()

    for i in range (10):
        t.fd(5)
        t.rt(90)
        t.fd(10)
        t.bk(10)
        t.lt(90)
        for i in range (5):
            t.forward(5)
            t.right(90)
            t.forward(5)
            t.backward(5)
            t.left(90)


def Y_as():

    scrn=turtle.Screen()
    t = turtle.Turtle()

    t.setheading(90)
    for i in range (10):
        t.fd(5)
        t.lt(90)
        t.fd(10)
        t.bk(10)
        t.rt(90)
        for i in range (4):
            t.fd(5)
            t.lt(90)
            t.fd(5)
            t.bk(5)
            t.rt(90)


meteodata()
X_as()
Y_as()

plaats=input("Kies een stad waarvan je de weersvoorspelling wil zien : typ A voor Antwerpen, L voor London of N voor New-York")


turtle.done()





