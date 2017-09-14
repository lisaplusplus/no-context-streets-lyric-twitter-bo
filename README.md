# no-context-streets-lyric-twitter-bo
Tweets random lyrics from The Streets with no context. Includes data scraper.

doTweet.py creates a reservior the first time it's ran.
The reservior is a text file containing 1 candidate tweet
per line. This reservior does not contain any duplicates.
Once doTweet.py creates or finds an existing reservior, it
loads it into memory, pops (get + delete) a random element
from the list, overwrites the reservior file with the in-
memory copy (making it one line shorter) and then tweets
the selected tweet text.

Designed to be executed by crontab.

# Requires
python 3x
tweepy
secrets.json file with Twitter API auth data

# Running
$ python doTweet.py


