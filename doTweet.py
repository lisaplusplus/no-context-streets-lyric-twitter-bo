import tweepy
import random, os, json

import logging
SCRIPT_PARENT = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(filename=SCRIPT_PARENT + '/originalTweetsMaterialBot.log',format='%(asctime)s %(message)s',level=logging.INFO)

LYRIC_SOURCE_FILE= SCRIPT_PARENT + "/datasources/songLyrics.txt"
TWEET_RESERVOIR_FILE = SCRIPT_PARENT + "/tweetReservoir.txt"
SECRETS_FILE= SCRIPT_PARENT + "/secrets.json"

# Generate the tweet 'resoviour' from songLyrics.txt
#   generated in ./datasources/ (from the internet)
def initialiseLyricReservoir():
  logging.info("initialiseLyricReservoir()")
  with open(LYRIC_SOURCE_FILE) as lyricFile:
    lyricList = lyricFile.read().splitlines()
    logging.info("Got " + str(len(lyricList)) + " lines from the source file.")

    # Convert to the set structure to eliminate duplicates.
    lyricSet = set(lyricList)
    logging.info("Got " + str(len(lyricSet)) + " lyric lines after removing duplicates.")

    writeReservoirFile(lyricList)

  logging.info("Tweet reserviour file saved. ")

# Tweets are removed from the reservoir
#   before getting sent Twitter
def isTweetReservoirDepleted():
  return not os.path.isfile(TWEET_RESERVOIR_FILE) or os.stat(TWEET_RESERVOIR_FILE).st_size == 0

def readReservoirFile():
  logging.info("readReservoirList()")

  reservoirFileHandle = open(TWEET_RESERVOIR_FILE, "r")
  reservoirList = reservoirFileHandle.read().splitlines()
  reservoirFileHandle.close();

  logging.info("Loaded reservoir of size " + str(len(reservoirList)) + " into memory.")
  return reservoirList

def writeReservoirFile(tweetList):
  logging.info("writeReservoirList()")
  
  reservoirFileHandle = open(TWEET_RESERVOIR_FILE, "w")
  for tweet in tweetList:
    reservoirFileHandle.write(tweet + "\n")

def calculateRandomListIndex(targetList):
  logging.info(" * R O L L S    D I C E * ");
  
  secureRandom = random.SystemRandom()
  return random.randrange(0, len(targetList));

def popRandomReservoirEntry():
  logging.info("popRandomReservoirEntry()");
  
  reservoirList = readReservoirFile()
  
  randomTweetIndex = calculateRandomListIndex(reservoirList)
  logging.info("Rolled a " + str(randomTweetIndex) + ". That's certainly a large dice.");
  
  randomTweet = reservoirList.pop(randomTweetIndex)
  writeReservoirFile(reservoirList)

  return randomTweet

# Main

# Reset the reservoir when we run out of new things to tweet
if isTweetReservoirDepleted():
  logging.info("Depleted reserviour detected. Resetting")
  initialiseLyricReservoir()


# Load authentication keys
with open(SECRETS_FILE) as secretsFileHandle:
  globals().update(json.load(secretsFileHandle))

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
api.update_status(popRandomReservoirEntry());
