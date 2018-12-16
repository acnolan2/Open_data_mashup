
#This script takes a list of URLs of 2017 Mayor press releases as an input and loops through this list.
#This loop gets the HTML source code for each of those pages that is associated with those URLs and saves them as an individual .txt file
import urllib.request
import time

#Opens list of 2017 URLs and reads them into a list
infile = open("2017urls.txt", "r")
url_list = infile.readlines()

#Loops through URLS, fetching the HTML for each and writing to a .txt file which is numbered and written incrementally
i=0
for each_url in url_list:
    urllib.request.urlretrieve(each_url, "pr" + str(i) + ".txt")
    i = i + 1
    time.sleep(3)
    print("Sleeping for 3 seconds....")





