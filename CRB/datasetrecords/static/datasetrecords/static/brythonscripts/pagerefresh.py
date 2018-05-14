import time 
from broswer import document, alert 

def sendAlert(msg):
    if(msg):
        alert(msg)
    else:
        alert("Nothing has been sent yet")
