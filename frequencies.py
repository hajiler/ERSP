import pandas as pd

mapped_tweets = pd.read_csv("C:\\Users\\erodri90\\.PyCharmEdu2018.2\\config\\scratches\\Mapped Tweets.csv")
information_types = {}
for index in mapped_tweets.index:
    if isinstance(mapped_tweets.loc[index]["info_type"], str):
        for designated_type in mapped_tweets.loc[index]["info_type"].split(","):
            if not information_types.get(designated_type):
                new_type = {designated_type : [1, mapped_tweets.loc[index]["urgency"]]}
                information_types.update( new_type )
            else:
                information_types[designated_type][0]+=1
                if mapped_tweets.loc[index]["urgency"] == 1.0:
                    information_types[designated_type][1]+=1

sorted_frequencies = sorted(information_types.items(), key = lambda x:x[1][1], reverse= True)

for type in sorted_frequencies:
    print(type[0], ":\n        appears ", type[1][0], "times;", type[1][1], "of which are urgent")

