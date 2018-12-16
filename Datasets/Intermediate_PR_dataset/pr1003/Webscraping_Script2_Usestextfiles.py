#This updated version of my script extracts the necessary data from the press releases and writes it to a CSV file.
#This update version uses .txt files saved to a local drive instead of directly hitting websites and then extracting.


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup



import csv



#from time import sleep
#from random import randint



# names csv file, gives it headers
filename = "Intermediate_PR_dataset.csv"
f = open(filename, "w", encoding="utf-8")
headers = "pr_id, title, body, date_published\n"
f.write(headers)

#Starts a loop to loop through names of files saved on local drive, turns each file into soup object, parses those files

for files in range(0,1003):

    infile = open("pr" + str(files) + ".txt", "rb")
    page_html = infile.read()
    pr_id = str(files)
    print(pr_id)

    page_soup = soup(page_html, "html.parser")





#Finds title, subtitle, date, and body elements
    title = page_soup.find("h1",{"class":"bottom-spacing page-heading"}).contents[0]

    #this will need an if else statement to capture the pr without subtitles
    #subtitles = []
    #for subtitle in page_soup.find("div", {"class": "bottom-spacing black-normal-title"}).contents[0]:
    #    subtitles.append(subtitle.text)
    #    if subtitle is None:
    #        print("None")

    body_of_pr = page_soup.find("div",{"class":"container-fluid page-full-description"}).find('p').text
    str_body_of_pr = str(body_of_pr)

    date_published = page_soup.find("div",{"class":"black-medium-high-title"}).contents[0]




    #Writes these elements to a csv file and replaces all commas with other characters, because csv are comma delimited.
    f.write(pr_id + "," + title.replace(",", "|") + "," + str_body_of_pr.replace(",", "|") + "," + date_published.replace(",", "|") + "\n")

f.close()
