# TwitterBot
This Twitter bot works by using a YAML list with four columns and selects a word at random from each column. The words from the first three columns are used to form the insult and the word from the last column is the Twitter handle of the user who is tweeted at. The two python files do the same thing but in a different way.

TweetInsultButton.py requires a button connected to a Raspberry Pi. It generates and tweets the insult whenever the button is pressed.

TweetInsultTime.py generates and tweets the insult then waits a random amount of time before tweeting again.

Insults.yml contains the words and twitter handles used to generate the insult

To set up the python programs, you'll need to add the path to the YAML file. You'll also need to set up a Twitter App and add the consumer key, consumer secret, access token, and access secret to the program. Link to Twitter Apps: https://apps.twitter.com/
