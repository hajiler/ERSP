import pandas as pd
from nltk import sent_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt

file = input("File name: ")
f = open(file)
mapped_tweets = pd.read_csv(f)
f.close()
#get frequency of information types
information_types = {}
#index through csv
for index in mapped_tweets.index:
    #confirms tweet is a string
    if isinstance(mapped_tweets.loc[index]["info_type"], str):
        # split information types
        for designated_type in mapped_tweets.loc[index]["info_type"].split(","):
            #if information type hasn't been accounted for yet
            if not information_types.get(designated_type):
                new_type = {designated_type : [1, mapped_tweets.loc[index]["urgency_level"]]}
                information_types.update( new_type )
            #update frequency for information type
            else:
                information_types[designated_type][0]+=1
                if mapped_tweets.loc[index]["urgency_level"] == 1.0:
                    information_types[designated_type][1]+=1

## Print information
# sorted_frequencies = sorted(information_types.items(), key = lambda x:x[1][1], reverse= True)
# print(file)
# for type in sorted_frequencies:
#     if type[1][1] > 0:
#         print(type[0], ":  appears ", type[1][0], "times;", type[1][1], "of which are urgent")


#wordo
comment_words = ' '
file = "start"
while file != "#":
    file = input("File name: ")
    if file == "#":
        break
    f = open(file)
    mapped_tweets = pd.read_csv(f)
    f.close()
    # iterate through the csv file
    for index in mapped_tweets.index:
        if mapped_tweets.loc[index]["urgency_level"] > 0:
            val = mapped_tweets.loc[index]["tweet"]
            print(sent_tokenize(val))

            # split the value
            tokens = val.split()

            # Converts each token into lowercase
            for i in range(len(tokens)):
                tokens[i] = tokens[i].lower()

            for word in val:
                comment_words = comment_words + word + ' '


#print wordCloud
wc = WordCloud(width = 800, height = 600,
                background_color ='white',
                min_font_size = 5).generate(comment_words)

#plot the WordCloud image
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wc)
plt.axis("off")
plt.tight_layout(pad = 0)

#plt.show()
