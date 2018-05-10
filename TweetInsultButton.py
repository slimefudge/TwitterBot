import random
import time
import yaml
import RPi.GPIO as GPIO
from twython import Twython


# find insult list
config = yaml.load(open('/home/pi/Desktop/insults.yml'))

# twython setup
CONSUMER_KEY = 'gnCkYsszqPSx25rHhpQmTiUn5'
CONSUMER_SECRET = 'vTKVZawmoZdrKEX6ibxpmnf1F3vqiI4WAWvmHnAf6hpX2blcdv'
ACCESS_TOKEN = '968602481608527879-O1J1epzMZJqmTsvHWho7o1dnjmIcS9Z'
ACCESS_SECRET = 'hhen4jv6XSaz9k12PVeJRjeKP8nyX9yEFnNeIgAyIwf98'

api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

#button setup
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23

try:
    while True:
        button_state = GPIO.input(23)
        if button_state == False:
            # algorithm simply makes a random choice from three different columns and concatenates them.
            pref = 'Thou'
            col1 = random.choice(config['column1'])
            col2 = random.choice(config['column2'])
            col3 = random.choice(config['column3'])
            col4 = random.choice(config['column4'])
          
            tweet = ( pref + ' ' + col1 + ' ' + col2 + ' ' + col3 + '. ' + '@' + col4 )
            
            print (tweet)
            api.update_status(status=tweet)
            time.sleep(1)
except:
    GPIO.cleanup()