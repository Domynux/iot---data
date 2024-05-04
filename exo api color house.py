import network   #import des fonction lier au wifi
import urequests	#import des fonction lier au requetes http
import utime	#import des fonction lier au temps
import ujson	#import des fonction lier aà la convertion en Json
from machine import Pin,PWM 

lesLed = [PWM(Pin(13,mode=Pin.OUT)) ,PWM(Pin(14,mode=Pin.OUT)) ,PWM(Pin(15,mode=Pin.OUT))]

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = ''
password = ''
wlan.connect(ssid, password) # connecte la raspi au réseau
url = ""

while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

def setColor(c):
    for i in range(0,3):
        lesLed[i].duty_u16(c[i])
        

dictColor = {
    'Slytherin' : [0,255,0],
    'Gryffindor' :  [255,0,0],
    'Ravenclaw' : [0,0,255],
    'Hufflepuff' : [255,200,0]
    }

while(True):
    try:
        print("GET")
        r = urequests.get(url) # lance une requete sur l'url
        print(r.json()['house']) # traite sa reponse en Json
        if r.json()['house'] == 'Gryffindor':
            setColor(dictColor['Gryffindor'])
            
        if r.json()['house'] == 'Slytherin':
            setColor(dictColor['Slytherin'])
            
        if r.json()['house'] == 'Ravenclaw':
            setColor(dictColor['Ravenclaw'])
            
        if r.json()['house'] == 'Hufflepuff':
            setColor(dictColor['Hufflepuff'])
            
        r.close() 
        utime.sleep(1)  
    except Exception as e:
        print(e)

