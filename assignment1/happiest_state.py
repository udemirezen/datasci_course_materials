import sys
import json
import re
import operator


sentimentDict = None
stateScore = {}

def loadSentimentDict(sent_file):
    rows = ( line.split('\t') for line in sent_file.read().splitlines() )
    global sentimentDict
    sentimentDict = {row[0]:int(row[1]) for row in rows}

def calculateSentiment(tweet_file):
    global stateScore
    for line in tweet_file.readlines():
        tweet = json.loads(line)
        tweetText = tweet.get("text")
        tweetPlace=tweet.get("place")
        if tweetText != None:
            sumSentimentScore = 0
            for word in re.findall(r'[a-z\']+', tweetText.lower(), re.I):
                sentimentScore = sentimentDict.get(word)
                if sentimentScore != None:
                    sumSentimentScore += sentimentScore
        if tweetPlace != None and tweetPlace.get("place_type") == 'city' and tweetPlace.get("country_code") == 'US':
            state = tweetPlace.get("full_name").split(", ")[1]
            score = stateScore.get(state)
            if score == None:
                score = 0
            score += sumSentimentScore
            stateScore[state] = score

def showResults():
    sortedState = sorted(stateScore.iteritems(),key=operator.itemgetter(1), reverse=True)
    print sortedState[0][0]

def main():
    #print "******************************************************************"
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    loadSentimentDict(sent_file)
    calculateSentiment(tweet_file)
    showResults()

if __name__ == '__main__':
    main()