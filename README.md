Horse _ ePoems
==============

Horse _ ePoems is a series of scripts that makes "poems" based off of tweets from @horse _ ebooks (https://twitter.com/Horse _ ebooks), a Twitter spam bot.

Grammatical Horse _ ePoems
--------------------------

`grammatical_horse_epoems.py` takes a file full of tweets (such as `tweets.txt`, included here) and builds a poem using each tweet as one line. The script attempts to preserve grammatical structure from line to line so that the lines flow. In a nutshell, the program uses a bigram model of English grammar to predict which part of speech will follow another part of speech. The algorithm finds the last part of speech in a verse, randomly picks the next part of speech based on a probability distribution of bigrams, and then finds a verse in its database whose first word has the correct part of speech. The program includes functionality to inductively learn grammar from a given text. 

`constants.py` contains a dictionary that acts as a source for the grammar for `grammatical_horse_epoems`. Currently, it uses grammar taken from scanning the Book of Genesis in the King James Bible. Future versions will use a more reasonable corpus for learning English grammar.

`tweets.txt` is a file full of tweets taken from the @horse _ ebooks Twitter page.

To generate your very own grammatical Horse _ ePoem, do the following:

	python grammatical_horse_epoems.py

The default poem length is set to 10 lines and the only dictionary available is the KJV as mentioned. As a disclaimer, your poem may or may not make sense :-) There are a few bugs lurking that I haven't been able to reproduce yet, so if you find one, I'd love to hear about it!
