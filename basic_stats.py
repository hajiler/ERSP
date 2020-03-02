import pandas as pd
#open and read file into data frame
def convert_file_to_data_frame(file_name):
    f = open(file_name)
    data = pd.read_csv(f)
    f.close()
    return data
#print data contents row by row
def print_csv_contents(data_frame):
    #for every index in dataFrame
    for index in data_frame.index:
        #for ever column value in row
        for value in data_frame.loc[index]:
            print(value, end = " ")
        print("")
#check urgency data
def urgency_checks(urgency, data_values):
    if urgency == 1.0:
        data_values["Urgent : Hours"] += 1
    elif urgency == 2.0:
        data_values["Urgent : Minutes"] += 1
    else:
        data_values["Not Urgent or Null"] += 1

#check target data
def target_checks(targets, data_values):
    for target in targets:
            if target == "P":
                 data_values["People"] += 1
            if target == "R":
                data_values["Responders"] += 1
            if target == "O":
                data_values["Other"] += 1

#collect various information from data_frame
def get_csv_stats(data_frame,column, data_values):
    #declare counters for each population
    for index in data_frame.index:
        targets = data_frame.loc[index][column[1]].split(",")
        target_checks(targets, data_values)
        urgency = data_frame.loc[index][column[0]]
        urgency_checks(urgency, data_values)




file = input("Input file directory: ")
data = convert_file_to_data_frame(file)
#print_csv_contents(data)
data_values = {
    "People" : 0,
    "Responders" : 0,
    "Other" : 0,
    "Urgent : Minutes" : 0,
    "Urgent : Hours" : 0,
    "Not Urgent or Null": 0
}
desired_columns = [ 'urgency_level (0,1,2)', 'relevant_to? (R,P,O,N)']
#desired_columns = ["urgency_level"]
get_csv_stats(data, desired_columns, data_values)
values = data_values.keys()
print("Basic stats")
target_file = open("Basic Data" + ".txt", "a+")
target_file.write(file + "\n")
for value in values:
    line = value + " = " + str(data_values[value]) + "\n"
    target_file.write(line)
    print(value, " = ",data_values[value])
target_file.close()
