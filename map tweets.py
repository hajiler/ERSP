import pandas as pd
import csv

binary_urgency_data = pd.read_csv("C:\\Users\\erodri90\\Downloads\\Philipine_tweet_150_annotations.csv")
f = open("C:\\Users\\erodri90\\.PyCharmEdu2018.2\\config\\scratches\\movies\\philippines_disaster_annotation.csv")
annotation_data = pd.read_csv(f)
f.close()

with open("Mapped Tweets.csv", mode = "w") as mapped_data:
    data_writer = csv.writer(mapped_data, delimiter =",",quotechar='"', quoting=csv.QUOTE_MINIMAL)
    data_writer.writerow(["tweet", "info_type", "urgency"])
    for annotation_index in annotation_data.index:
        for binary_index in binary_urgency_data.index:
            if binary_urgency_data.loc[binary_index]["tweet"] == annotation_data.loc[annotation_index]["tweet"]:
                row = [binary_urgency_data.loc[binary_index]["tweet"]]
                if isinstance(annotation_data.loc[annotation_index]["type_of_information"], list):
                    for info in annotation_data.loc[annotation_index]["type_of_information"].split(","):
                        row.append(info)
                else:
                    row.append(annotation_data.loc[annotation_index]["type_of_information"])

                row.append(binary_urgency_data.loc[binary_index]["urgency_level"])
                data_writer.writerow(row)


