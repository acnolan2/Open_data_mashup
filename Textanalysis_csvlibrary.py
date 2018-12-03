import csv

f = open('Final_dataset_DRAFT2.csv')
csv_f = csv.reader(f, delimiter=',', )
next(csv_f) # move past headers
next(csv_f) # move past broken header thing that I don't understand where it came from
# this will put the cursor at the start of line 3

attendees1=[1]

string2= "52 lieutenants"

for row in csv_f:
    title = row[0]
    text = row[1]
    date = row[2]

f.close()
