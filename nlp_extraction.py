import pandas as pd
from TweetClass import Tweet

mapped_tweets = []
#Open read and close file
f = open("C:\\Users\\erodri90\\.PyCharmEdu2018.2\\config\\scratches\\movies\\Mapped Tweets.csv")
mapped_tweets.append(pd.read_csv(f))
f.close()
f = open("C:\\Users\\erodri90\\.PyCharmEdu2018.2\\config\\scratches\\movies\\philipines_150_Tweet_Data-Arpita-1.csv")
mapped_tweets.append(pd.read_csv(f))
f.close()
f = open("C:\\Users\\erodri90\\.PyCharmEdu2018.2\\config\\scratches\\movies\\angy_disaster_annotation.csv")
mapped_tweets.append(pd.read_csv(f))
f.close()


features = {}
token_total = 0
phrase_total = 0

agreement = 0;
# iterate through the csv file
for index in mapped_tweets[0].index:
    token_strings = ''
    if (mapped_tweets[0].loc[index]["urgency_level"] > 0) and (mapped_tweets[1].loc[mapped_tweets[0].loc[index]["indexB"]]["urgency_level"] > 0) and (mapped_tweets[2].loc[mapped_tweets[0].loc[index]["indexA"] ]["urgency_level"] > 0):
    #if not (mapped_tweets[0].loc[index]["urgency_level"] > 0) and not (mapped_tweets[1].loc[mapped_tweets[0].loc[index]["indexB"]]["urgency_level"] > 0) and not (mapped_tweets[2].loc[mapped_tweets[0].loc[index]["indexA"] ]["urgency_level"] > 0):
        agreement += 1
        val = Tweet(mapped_tweets[0].loc[index]["tweet"])
        token_total += val.token_total()

        for phrase in val.lemma_phrases():
            phrase_total += 1
            if not phrase in features:
                features[phrase] = 1
            else:
                features[phrase] += 1

#print("Common features out of", agreement, "agreed upon tweets:")
phrase_features = []
for phrase in sorted(features.items(), key= lambda x: (x[1], x[0])):
    if phrase[1] > 3:
        phrase_features.append(phrase[0])
        print(phrase,
              "\n    frequencey of phrase       ", phrase[1]/phrase_total * 100, "%",
              "\n    frequency of urgent tweets " ,phrase[1]*(len(phrase[0].split()))/agreement * 100, "%")

