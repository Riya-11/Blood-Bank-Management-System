import webbrowser
from threading import Timer
import time 

def runner () :
    url = 'http://127.0.0.1:8000/stock/mail/'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

def run () :
    print (time.time())
    Timer(5, runner, ()).start()
    print ("It had entered this part ")
    print ("after below time period it will enter next iteration")
    runner()
    time.sleep(84600)  # sleep while time-delay events execute above time below-above time gap like after 86399 secs it will loop for now (one day )
while (True):
    run()
