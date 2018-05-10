import random
import time
import yaml
import RPi.GPIO as GPIO
from twython import Twython


# find insult list
config = yaml.load(open(' ')) # here you'll need to add the path to the yaml file

# twython setup. Add your key, token, and secrets here
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

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
