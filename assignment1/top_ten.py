__author__ = 'UMUT'
import sys
import json
import re
import operator

hashCount = {}

def parse_hash_count(tweet_file):
    global hashCount

    for line in tweet_file.readlines():
        tweet = json.loads(line)
        tweet_entities = tweet.get("entities")
        if tweet_entities != None:
            tags = tweet_entities.get("hashtags")
            if tags != None:
                for tag in tags:
                    hashtag = tag["text"]
                    count = hashCount.get(hashtag)
                    if count == None:
                        count = 0
                    count += 1
                    hashCount[hashtag] = count

def printTopTen():

    sorted_hash_count = sorted(hashCount.iteritems(), key=operator.itemgetter(1), reverse = True)
    for (hashtag, count) in sorted_hash_count[:10]:
         print hashtag.encode("utf-8") + " " + str(count)

def main():
    tweetFile = open(sys.argv[1])
    parse_hash_count(tweetFile)
    printTopTen()

if __name__ == '__main__':
    main()