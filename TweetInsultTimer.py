import random
import time
import yaml
from twython import Twython

# find insult list
config = yaml.load(open('')) # here you'll need to add the path to the yaml file

# twython setup. Add your key, token, and secrets here
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

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
             api.update_status(status=tweet)
             
             # waits between 3 and 12 hours to tweet again
             time.sleep(random.randint(60*60*3,60*60*12))
except:
    GPIO.cleanup()
