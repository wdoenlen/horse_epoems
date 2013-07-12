horse_epoems is a series of scripts that makes "poems" based off of tweets from @horse_ebooks, a Twitter spam bot.

grammatical_horse_epoems.py takes a file full of tweets (such as tweets.txt, included here) and builds a poem using each tweet as one line. The script attempts to preserve grammatical structure from line to line so that the lines flow.

constants.py contains a dictionary that acts as a source for the grammar for grammatical_horse_epoems. Currently, it uses grammar taken from scanning the Book of Genesis in the King James Bible.

Tweets.txt is a file full of tweets taken from the @horse_ebooks Twitter page.
