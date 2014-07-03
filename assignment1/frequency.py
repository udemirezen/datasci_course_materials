# coding=utf-8
import sys
import json
import math
import re

reload(sys)
sys.setdefaultencoding('utf-8')


def main():
    tweet_file = open(sys.argv[1])

    tweets = []

    for line in tweet_file:
        try:
            tweets.append(json.loads(line))
        except:
            pass

    tweetsTexts = []

    for tweet in tweets:
        if "text" in tweet.keys():
            tweetsTexts.append(tweet['text'].encode('utf-8'))

    terms = []

    newTweetDictionaryCounter = {}
    totalTweetCounter = 0
    for tweet in tweetsTexts:
        #   tweet = tweetsTexts[i]
        pattern = re.compile('[\W_]+', re.UNICODE)
        tweet = str(pattern.sub(' ', tweet))
        tweet = tweet.replace("@", "", 100).replace("#", "", 100).lower().strip()
        # print tweet

        terms = tweet.split(" ")

        for term in terms:

            if term in newTweetDictionaryCounter.keys():
                newTweetDictionaryCounter[term] += 1
            else:
                newTweetDictionaryCounter[term] = 1


        #print newTweetDictionaryCounter

    for x in newTweetDictionaryCounter:
        totalTweetCounter += int(newTweetDictionaryCounter[x])
    #print totalTweetCounter

    for x in newTweetDictionaryCounter:
       print x.strip(), float(newTweetDictionaryCounter[x])/totalTweetCounter

if __name__ == '__main__':
    main()
