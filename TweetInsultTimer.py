import random
import time
import yaml
from twython import Twython

# find insult list
config = yaml.load(open('/home/pi/Desktop/insults.yml'))

# twython setup
CONSUMER_KEY = 'gnCkYsszqPSx25rHhpQmTiUn5'
CONSUMER_SECRET = 'vTKVZawmoZdrKEX6ibxpmnf1F3vqiI4WAWvmHnAf6hpX2blcdv'
ACCESS_TOKEN = '968602481608527879-O1J1epzMZJqmTsvHWho7o1dnjmIcS9Z'
ACCESS_SECRET = 'hhen4jv6XSaz9k12PVeJRjeKP8nyX9yEFnNeIgAyIwf98'

api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

try:
    while True:
             # generates the insult by selecting 3 words and a twitter handle from insult list
             pref = 'Thou'
             col1 = random.choice(config['column1'])
             col2 = random.choice(config['column2'])
             col3 = random.choice(config['column3'])
             col4 = random.choice(config['column4'])
             
             tweet = ( pref + ' ' + col1 + ' ' + col2 + ' ' + col3 + '. ' + '@' + col4 )
             print (tweet)
             #api.update_status(status=tweet)
             
             # waits between 3 and 12 hours to tweet again
             time.sleep(random.randint(60*60*3,60*60*12))
except:
    GPIO.cleanup()