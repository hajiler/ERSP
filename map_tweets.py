import pandas as pd
import csv
from bisect import bisect_left
def bin_search(tweets,tweet):
    index = bisect_left(tweets, tweet)
    if index != len(tweets) and tweets[index] == tweet:
        return index
    else:
        return -1

f = open("C:\\Users\\erodri90\\.PyCharmEdu2018.2\\config\\scratches\\movies\\Philipine_tweet_150_annotations.csv")
binary_urgency_data = pd.read_csv(f)
f.close()
f = open("C:\\Users\\erodri90\\.PyCharmEdu2018.2\\config\\scratches\\movies\\elijah_disaster_annotation.csv")
annotation_data = pd.read_csv(f)
f.close()
sorted_tweets, sorted_tweets_tweets, sorted_tweets_indices = [],[],[]
for binary_index in binary_urgency_data.index:
    values = [binary_urgency_data.loc[binary_index]["tweet"], binary_index]
    sorted_tweets.append(values)

sorted_tweets.sort(key = lambda t : t[0])

for tweet in sorted_tweets:
    sorted_tweets_tweets.append(tweet[0])
    sorted_tweets_indices.append(tweet[1])

with open("Mapped Tweets.csv", mode = "w") as mapped_data:
    data_writer = csv.writer(mapped_data, delimiter =",",quotechar='"', quoting=csv.QUOTE_MINIMAL)
    data_writer.writerow(["indexA","indexB","tweet", "info_type", "urgency_level"])
    for annotation_index in annotation_data.index:
        indexA = bin_search(sorted_tweets_tweets, annotation_data.loc[annotation_index]["tweet"])
        if indexA != -1:
            binary_index = sorted_tweets_indices[indexA]
            if binary_urgency_data.loc[binary_index]["tweet"] == annotation_data.loc[annotation_index]["tweet"]:
                row = [annotation_index, binary_index ,binary_urgency_data.loc[binary_index]["tweet"]]
                if isinstance(annotation_data.loc[annotation_index]["info_type"], list):
                    for info in annotation_data.loc[annotation_index]["info_type"].split(","):
                        row.append(info)
                else:
                    row.append(annotation_data.loc[annotation_index]["info_type"])

                row.append(binary_urgency_data.loc[binary_index]["urgency_level"])
                data_writer.writerow(row)


