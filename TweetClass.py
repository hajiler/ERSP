import nltk as nltk
from nltk.stem import WordNetLemmatizer
from bisect import bisect_left

def bin_search(bag,word):
    index = bisect_left(bag, word)
    if index != len(bag) and bag[index] == word:
        return index
    else:
        return -1

class Tweet:
    tweet = ""
    #Bag of Words
    bag_of_words = {
        0 : [' family', ' patient', ' people', ' staff'],
        1 : [' floor', ' house', ' st'],
        2 : [' reliefph',' rescueph'],
        3 : [' food', ' generator', ' help', ' rescue', ' water'],
        4 : [' philippine capital', ' philippine',' manila'],
        5: [' volunteer',' donation',]
    }
    def __init__(self, input_tweet):
        self.tweet = input_tweet
        self.tweet.lower()
    def token_total(self):
        words = nltk.word_tokenize(self.tweet)
        return len(words)

    def slang_to_word(self, word):
        if word == "pls":
            return "please"
        if word == "rt":
            return "retweet"
        if word == "ppl":
            return "people"
        return  word

    def lemma_phrases(self):
        words = nltk.word_tokenize(self.tweet)
        tagged_words = nltk.pos_tag(words)
        phrases = []
        phrase = ""
        for tag in tagged_words:
            word = self.slang_to_word(tag[0])
            if word.isalpha():
                lem = WordNetLemmatizer()
                if tag[1] == 'JJ':
                    phrase = phrase + " " + lem.lemmatize(word)
                if tag[1][0:2] == 'NN':
                    phrase = phrase + " " + lem.lemmatize(word)
                    phrases.append(phrase)
                    phrase = ""
        return phrases
    def get_feat_vect(self):
        extracted = self.lemma_phrases()
        vector = [0] * len(self.bag_of_words.keys())
        for phrase in extracted:
            for i in self.bag_of_words.keys():
                if bin_search(self.bag_of_words.get(i), phrase) != -1:
                    vector[i] += 1
        return tuple(vector)

