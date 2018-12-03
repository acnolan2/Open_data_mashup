
import csv
import spacy
nlp = spacy.load('en')

with open('opendata3.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)


    list_of_title = []
    for line in csv_reader:
        text = line[0]
        list_of_title.append(text)

print(list_of_title)

for eachtitle in list_of_title:
    str_eachtitle = str(eachtitle)
    doc = nlp(str_eachtitle)
    for entity in doc.ents:
        if entity.label_ == 'GPE':
            print(entity.text, entity.label_)

 #       list = []
 #       for entity in doc.ents:
 #          if entity.label_ == 'GPE':
 #           #print(entity.text, entity.label_) This line will print out all GPE label entities
 #           GPE = entity.text
 #           list.append(GPE)
 #   print(len(list))


            #with open('columnwentity.csv', 'w') as new_file:
                #csv_writer = csv.writer(new_file)

                #csv_writer.writerow(list)


        #for line in csv_reader:






