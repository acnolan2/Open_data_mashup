import csv
import json

n_data = {} # This creates a dictionary object


#Here, I open my press release dataset (w. unique identifiers), read it in, move past problematic headers, and (put all of them in a list?)
f = open('Intermediate_PR_dataset.csv')
pr_text = csv.reader(f, delimiter=',', )
next(pr_text) # move past headers
next(pr_text) #move past headers
pr_list = [r for r in pr_text] # I have no idea what this line does. Does this make a list of each row in my dataset?

f2 = open('Unemployment_ChiHealthAtlas.csv')
unemployment_data = csv.reader(f2, delimiter=',', )
unemployment_list = [r for r in unemployment_data]


f3 = open('Violent_crime_in_public_spaces_ChiHealthAtlas.csv')
crime_data = csv.reader(f3, delimiter=',', )
crime_list = [r for r in crime_data]


f4 = open('Medianincome_ChiHealthAtlas.csv')
median_income_data = csv.reader(f4, delimiter=',', )
median_income_list = [r for r in median_income_data]



# for row in pr_text:
#     title = row[0]
#     text = row[1]
#     date = row[2]
#     pr_list.append(text)

#Here I'm opening a file with all the neighborhood names and their alternate names, read it in, create a list of lists
with open('altnames_csv.csv', 'r') as infile:
    csvin = csv.reader(infile)
    data = [r for r in csvin] #this is a list of lists

for nhood in data:
    std_name = nhood[0] #For each list in my list of lists of altnames, grab the first value
    n_data[std_name] = {"names" : nhood, "appears": 0, "pr_id": []} #Set the standard neighborhood name as the key and the alt names as the value of names, fills other values with empty data

for pr in pr_list:
    pr_id = pr[0]
    title = pr[1]
    text = pr[2]
    date = pr[3]
    for nid in n_data.keys(): #Looks up all the std names
        allnames = n_data[nid]["names"] #Gives a list of the names
        for name in allnames:
            if name in text:
                n_data[nid]["pr_id"].append(pr_id)
                n_data[nid]["appears"] += 1
                break

for column in unemployment_list:
    std_name = column[0]
    geo_id = column[1]
    percent = column[2]
    if "-" in std_name:
        std_name = std_name.split("-")[-1]
    n_data[std_name]["geo_id"]= geo_id
    n_data[std_name]["percent"]= percent


for item in crime_list:
    year = item[0]
    std_name = item[1]
    crime = item[3]
    if "-" in std_name:
        std_name = std_name.split("-")[-1]
    n_data[std_name]["crime"]= crime

for item4 in median_income_list:
    std_name = item4[0]
    geo_id = item4[1]
    median_income = item4[2]
    if "-" in std_name:
        std_name = std_name.split("-")[-1]
    n_data[std_name]["median income"]= median_income
    n_data[std_name]["geo_id"]= geo_id




for nid, vals in n_data.items():
    print(nid, vals)
    # print(nid, vals['appears'], vals['pr_id'], vals['unemployment'])

with open('nhooddata.json', 'w') as fout:
    json.dump(n_data, fout, indent = 4)





#Aileen attempting to write this JSON into a CSV
#n_data_parsed = json.loads()


outputfile = open('Final_dataset.csv', 'w')
csvwriter = csv.writer(outputfile)

columnTitleRow = "std_name, geo_id, percent_unemployment, crime, median_income, appears, pr_id \n"
outputfile.write(columnTitleRow)

for key in n_data.keys():
    std_name = key
    geo_id = str(n_data[key]["geo_id"])
    percent = str(n_data[key]["percent"])
    crime = str(n_data[key]["crime"])
    median_income = str(n_data[key]["median income"])
    appears = str(n_data[key]["appears"])
    pr_id = '"' + str(n_data[key]["pr_id"]) + '"'
    row = std_name + "," + geo_id + "," + percent + "," + crime + "," + median_income + "," + appears + "," + pr_id + "," + "\n"
    outputfile.write(row)

outputfile.close()

