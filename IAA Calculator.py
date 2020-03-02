import pandas as pd

def write_IAA_info(file1, file2, agreed, data_one_values, data_two_values, iaa):
    f = open("C:\\Users\\erodri90\\.PyCharmEdu2018.2\\config\\scratches\\IAA\\IAA.txt", "a")
    f.write("Annotation info between:\n    " + "File 1: "+ file1 + "\n    " + "File 2 " + file2 + "\n")
    f.write("Agreed: \n")
    for value in agreed:
        line = "    " + value + " : " + str(agreed[value]) + "\n"
        f.write(line)
    f.write("File 1: \n")
    for value in data_one_values:
        line = "    " + value + " : " + str(data_one_values[value]) + "\n"
        f.write(line)
    f.write("File 2: \n")
    for value in data_two_values:
        line = "    " + value + " : " + str(data_two_values[value]) + "\n"
        f.write(line)

    line = "IAA : " + str(iaa) + "\n"
    f.write(line)
    f.write("\n\n\n")


def calculate(agreed, data_one_values, data_two_values, total):
    #proportion agreed
    prop_o = (agreed["urgent"] + agreed["not urgent/null"]) / total
    #proportion of urgent
    prop_u = (data_one_values["urgent"] / total) * (data_two_values["urgent"] / total)
    #proportion of not urgent/null
    prop_n = (data_one_values["not urgent/null"] / total) * (data_one_values["not urgent/null"] / total)
    #proportion of random agreement
    prop_e = prop_u + prop_n
    k = (prop_o - prop_e) / (1 - prop_e)
    return k


def cohen_kapp(file1, file2, urgency_col):
    data_one = pd.read_csv(file1)
    f = open (file2)
    data_two = pd.read_csv(f)
    f.close()
    agreed = {"urgent" : 0,"not urgent/null" : 0, "total" : 0}
    data_one_values,data_two_values = {"urgent" : 0,"not urgent/null" : 0},{"urgent" : 0,"not urgent/null" : 0}
    total = 0
    for index in data_one.index:
        total += 1
        #update agreed frequencies
        if data_one.loc[index][urgency_col] == 0 and  data_two.loc[index][urgency_col] == 0:
            agreed["total"] += 1
            agreed["not urgent/null"] += 1
        elif data_one.loc[index][urgency_col] == 1 * data_one.loc[index][urgency_col] > 0:
            agreed["total"] += 1
            agreed["urgent"] += 1
        else
            print(data_one.loc[index][""])
        #update individual
        #data_one
        if data_one.loc[index][urgency_col] == 1 or data_one.loc[index][urgency_col] == 2:
            data_one_values["urgent"] += 1
        else:
            data_one_values["not urgent/null"] += 1
        #data_two
        if data_two.loc[index][urgency_col] == 1 or data_two.loc[index][urgency_col] == 2:
            data_two_values["urgent"] += 1
        else:
            data_two_values["not urgent/null"] += 1
    iaa = calculate(agreed, data_one_values, data_two_values, total)
    write_IAA_info(file1, file2, agreed, data_one_values, data_two_values, iaa)

f1 = "C:\\Users\\erodri90\\.PyCharmEdu2018.2\\config\\scratches\\movies\\Philipine_tweet_150_annotations.csv"
f2 = "C:\\Users\\erodri90\\.PyCharmEdu2018.2\\config\\scratches\\movies\\philipines_150_Tweet_Data-Arpita.csv"
cohen_kapp(f1, f2, "urgency_level")

f1 = "C:\\Users\\erodri90\\.PyCharmEdu2018.2\\config\\scratches\\movies\\angy_disaster_annotation.csv"
f2 = "C:\\Users\\erodri90\\.PyCharmEdu2018.2\\config\\scratches\\movies\\elijah_disaster_annotation.csv"
cohen_kapp(f1, f2, "urgency_level (0,1,2)")
