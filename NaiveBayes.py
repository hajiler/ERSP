import pandas as pd
from TweetClass import Tweet

#Open read and close file
f = open("C:\\Users\\erodri90\\.PyCharmEdu2018.2\\config\\scratches\\movies\\Mapped Tweets.csv")
mapped_tweets = pd.read_csv(f)
f.close()

#Develop training features and labels from 150 sampled tweets
features = []
labels = []
for index in mapped_tweets.index:
    #create tweet object
    val = Tweet(mapped_tweets.loc[index]["tweet"])
    #get and append feature tuple
    features.append(val.get_feat_vect())
    #append label
    if mapped_tweets.loc[index]["urgency_level"] > 0:
        labels.append(1)
    else:
        labels.append(0)

from sklearn.naive_bayes import GaussianNB
#train model
model = GaussianNB()
model.fit(features, labels)

#calculate accuracy
f = open("C:\\Users\\erodri90\\.PyCharmEdu2018.2\\config\\scratches\\movies\\angy_disaster_annotation.csv")
test_tweets = pd.read_csv(f)
f.close()
accurate = 0
inaccurate = 0
missed = []
for index in test_tweets.index:
    #create tweet objects and get feature vectors
    tweet = Tweet(test_tweets.loc[index]["tweet"])
    test_features = [list(tweet.get_feat_vect())]
    #get label prediction of current tweet
    prediction = model.predict(test_features)
    label = test_tweets.loc[index]["urgency_level"]
    if (prediction[0] == 1 and label > 0) or (prediction[0] == 0 and (label == 0 or label == "")):
        accurate+= 1
    else:
        inaccurate += 1
        # print(tweet.tweet)
        # print(prediction[0], test_tweets.loc[index]["urgency_level"])
print("Accurate predictions: ", accurate, ", ", accurate/len(test_tweets)*100, "%")
print("Inaccurate predictions: ", inaccurate, ", ", inaccurate/len(test_tweets)*100, "%")




