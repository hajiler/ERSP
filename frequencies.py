import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


mapped_tweets = pd.read_csv("C:\\Users\\erodri90\\.PyCharmEdu2018.2\\config\\scratches\\Mapped Tweets.csv")
#get frequency of information types
information_types = {}
for index in mapped_tweets.index:
    if isinstance(mapped_tweets.loc[index]["info_type"], str):
        for designated_type in mapped_tweets.loc[index]["info_type"].split(","):
            if not information_types.get(designated_type):
                new_type = {designated_type : [1, mapped_tweets.loc[index]["urgency_level"]]}
                information_types.update( new_type )
            else:
                information_types[designated_type][0]+=1
                if mapped_tweets.loc[index]["urgency_level"] == 1.0:
                    information_types[designated_type][1]+=1

sorted_frequencies = sorted(information_types.items(), key = lambda x:x[1][1], reverse= True)

for type in sorted_frequencies:
    print(type[0], ":\n        appears ", type[1][0], "times;", type[1][1], "of which are urgent")

import pandas as pd


comment_words = ' '

# iterate through the csv file
for index in mapped_tweets.index:
    if mapped_tweets.loc[index]["urgency_level"] > 0:
        val = mapped_tweets.loc[index]["tweet"]

        # split the value
        tokens = val.split()

        # Converts each token into lowercase
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()

        for words in tokens:
            comment_words = comment_words + words + ' '

#print wordCloud
wc = WordCloud(width = 800, height = 600,
                background_color ='white',
                min_font_size = 5).generate(comment_words)

#plot the WordCloud image
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wc)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()
