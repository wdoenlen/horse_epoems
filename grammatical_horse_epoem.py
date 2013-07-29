from __future__ import division
from constants import *
import random, nltk

def get_tweets_from_HTML(filename, target):
    '''
    Function to get Tweets out of an html copy
    of a Twitter page and save it to a file.
    '''
    #first, extract the tweets from the file
    tweetlist = []
    rawhtml = open(filename, "r+")
    for line in rawhtml:
        if "js-tweet-text tweet-text" in line:
            line = line.strip()
            start = line.find(">")
            end = line.find("<", 1, -1)
            tweet = line[start + 1:end]
            tweetlist.append(tweet)

    #save the list of tweets into a new file
    targetfile = open(target, 'r+')
    targettweets = targetfile.readline()
    for tweet in tweetlist:
        if tweet not in targettweets:
            targetfile.write(tweet + "\n")

def tokenize_verse(verse):
    '''
    Returns tokens of a verse.
    '''
    return nltk.word_tokenize(verse)


def tokenize_file(filename):
    '''
    Returns a list of all the verses in a file tokenized.
    '''
    f = open(filename, 'r+')
    master_list = []
    for line in f:
        master_list.append(tokenize_verse(line))
    return master_list

def choose_verses(verses, N, repeats=False):
    '''
    Return a list of N random verses, possibly repeating.
    '''
    random_verses = []
    
    if repeats == True:
        for i in range(N):
            random_verses.append(random.choice(verses))
    else:
        for i in range(N):
            line = random.choice(verses)
            if line not in random_verses:
                random_verses.append(line)
                
    return random_verses

def pos_tag_verses(verses):
    '''
    Tag verses with parts of speech (assuming verses tokenized)
    '''
    pos_list = []
    for verse in verses:
        pos_list.append(nltk.pos_tag(verse))
    return pos_list

def build_pos_fdist(tokens):
    '''
    Builds a probability distribution from a text
    that one POS follows another
    '''
    #returns a list that replaces the tokens
    #with their parts of speech
    tokens_tagged = nltk.pos_tag(tokens)
    tag_list = []
    for word in tokens_tagged:
        tag_list.append(word[1])

    #builds a frequency distribution of pairs
    # of parts of speech that occured in the text
    
    bigrams = nltk.bigrams(tag_list)
    fd = nltk.FreqDist(bigrams)
    freq_dict = {}
    
    for term in pos:
        temp = []
        total = 0
        for key in fd.keys():
            if key[0] == term:
                total += fd[key]
        for key in fd.keys():
            if key[0] == term:
                temp.append((key[1], fd[key] / total))
        freq_dict[term] = temp[:]
            
    return freq_dict

def weighted_choice(prob_dist):
    '''
    Function that takes in a probability distribution
    and returns a random choice based on it.
    Assumes probability distribution is a list of tuples
    (item, p), where p is the probability item occurs.
    Based off of an approach from
    http://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python/
    '''
    totals = []
    running_total = 0

    try:
        for i in range(len(prob_dist)):
            running_total += prob_dist[i][1]
            totals.append((prob_dist[i][0], running_total))

        rnd = random.random()
        for item, weight in totals:
            if rnd < weight:
                return item
    except IndexError:
        return random.choice(["NN", "VB", "JJ"])

def make_grammatical_poem(verses, N=10, grammar=kjvdict):
    '''
    Make a poem N lines long that attempts to be
    grammatically correct given a list of verses
    and a "grammar" which is a frequency distribution
    of POS bigrams. The verses are assumed to be already
    tokenized.
    '''
    
    initial = random.choice(verses)
    poem = [initial]
    i = 0

    while i < N:
        
        initial_tags = nltk.pos_tag(initial)
        final_tag = initial_tags[-1][1]
        next_tag = weighted_choice(grammar.get(final_tag, 'NN'))
        random.shuffle(verses)
        
        for j in range(len(verses)):
            next_verse = verses[j]
            if nltk.pos_tag(next_verse)[0][1] == next_tag:
                poem.append(next_verse)
                initial = next_verse
                i += 1
                break
        else:
            print "Could not find matching lines to finish poem."
        
    return poem

def read_poem(verses):
    '''
    Print out a human-readable poem from a list of verses.
    '''
    for verse in verses:
        readable = ''
        for word in verse:
            readable += word + " "
        print readable

if __name__ == "__main__":
    tweets = tokenize_file("tweets.txt")
    poem = make_grammatical_poem(tweets)
    read_poem(poem)
