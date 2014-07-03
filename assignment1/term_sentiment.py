# coding=utf-8
import sys
import json
import math
import re

reload(sys)
sys.setdefaultencoding('utf-8')


def hw():
    print 'Hello, world!'


def lines(fp):
    print str(len(fp.readlines()))


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # hw()
    # lines(sent_file)
    # lines(tweet_file)
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term.lower()] = int(score)  # Convert the score to an integer.

    #   print scores.items()  # Print every (term, score) pair in the dictionary
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
    temp = {}
    result = []
    newDict = {}
    sc = int(0)

    newTweetDictionary = {}
    newTweetDictionaryCounter = {}

    for tweet in tweetsTexts:
        #   tweet = tweetsTexts[i]
        pattern = re.compile('[\W_]+', re.UNICODE)
        tweet = str(pattern.sub(' ', tweet))
        tweet = tweet.replace("@", "", 100).replace("#", "", 100).lower().strip()
       #   print tweet
        terms = tweet.split(" ")
        sc = int(0)
        tempTweetList = []

        for term in terms:

            tweetscore = int(scores.get(term, 0))
            sc += tweetscore

            if tweetscore == 0:
                tempTweetList.append(term)
         #   print term, int(scores.get(term, 0))

        #  print tempTweetList
        for tt in tempTweetList:
            if tt in newTweetDictionary.keys():
                newTweetDictionary[tt] += float(sc)
                newTweetDictionaryCounter[tt] += 1
            else:
                newTweetDictionary[tt] = float(sc)
                newTweetDictionaryCounter[tt] = 1

        #print newTweetDictionary
        #print newTweetDictionaryCounter
        #temp[tweet] = sc
        result.append(sc)

    # for t in temp:
    #    print t, "--> ", temp[t]
    #    print temp[t]

    # Sonuç Yazdırma Kısmı
    # for r in result:
    #    print r
    # print newTweetDictionary
    # print newTweetDictionaryCounter

    delkeys= []
    for x in newTweetDictionary:
        newTweetDictionary[x] /= newTweetDictionaryCounter[x]
        if newTweetDictionary[x] == 0:
            delkeys.append(x)

    # for d in delkeys:
    #     del(newTweetDictionary[d])

    for x in newTweetDictionary:
       print x.strip(), newTweetDictionary[x]

if __name__ == '__main__':
    main()
