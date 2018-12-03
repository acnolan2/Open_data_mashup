#This script loops through the raw text files of the press releases that are created from the HTML and
#looks for the instance of a neighborhood name. This scrtipt counts all neighborhood names within these files
# and outputs a final count.


#Neighborhood that will be looked for within the press release .txt files

string1 = "Rogers Park"
string2 = "West Ridge"
string3 = "Uptown"
string4 = "Lincoln Square"
string5 = "North Center"
string6 = "Lakeview"
string7 = "Lincoln Park"
string8 = "Near North Side"
string9 = "Edison Park"
string10 = "Norwood Park"
string11 = "Jefferson Park"
string12 = "Forest Glen"
string13 = "North Park"
string14 = "Albany Park"
string15 = "Portage Park"
string16 = "Irving Park"
string17 = "Dunning"
string18 = "Montclare"
string19 = "Belmont Cragin"
string20 = "Hermosa"
string21 = "Avondale"
string22 = "Logan Square"
string23 = "Humboldt Park"
string24 = "West Town"
string25 = "Austin"
string26 = "West Garfield Park"
string27 = "East Garfield Park"
string28 = "Near West Side"
string29 = "North Lawndale"
string30 = "South Lawndale"
string31 = "Lower West Side"
string32 = "Loop"
string33 = "Near South Side"
string34 = "Chinatown" or "Armour Square" or "Chinatown" or "Bridgeport" # But if you put Chinatown first, it will count it.
string35 = "Douglas"
string36 = "Oakland"
string37 = "Fuller Park"
string38 = "Grand Boulevard"
string39 = "Kenwood"
string40 = "Washington Park"
string41 = "Hyde Park"
string42 = "Woodlawn"
string43 = "South Shore"
string44 = "Chatham"
string45 = "Avalon Park"
string46 = "South Chicago"
string47 = "Burnside"
string48 = "Calumet Heights"
string49 = "Roseland"
string50 = "Pullman"
string51 = "South Deering"
string52 = "East Side"
string53 = "West Pullman"
string54 = "Riverdale"
string55 = "Hegewisch"
string56 = "Garfield Ridge"
string57 = "Archer Heights"
string58 = "Brighton Park"
string59 = "McKinley Park"
string60 = "Bridgeport"
string61 = "New City"
string62 = "West Elsdon"
string63 = "Gage Park"
string64 = "Clearing"
string65 = "West Lawn"
string66 = "Chicago Lawn"
string67 = "West Englewood"
string68 = "Englewood"
string69 = "Greater Grand Crossing"
string70 = "Ashburn"
string71 = "Auburn Gresham"
string72 = "Beverly"
string73 = "Washington Heights"
string74 = "Mount Greenwood"
string75 = "Morgan Park"
string76 = "O'Hare"
string77 = "Edgewater"


#Initializes counters that represent the number of the instances of the neighborhood names in the .txt files
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count0 = 0
count11 = 0
count12 = 0
count13 = 0
count14 = 0
count15 = 0
count16 = 0
count17 = 0
count18 = 0
count19 = 0
count20 = 0
count21 = 0
count22 = 0
count23 = 0
count24 = 0
count25 = 0
count26 = 0
count27 = 0
count28 = 0
count29 = 0
count30 = 0
count31 = 0
count32 = 0
count33 = 0
count34 = 0
count35 = 0
count36 = 0
count37 = 0
count38 = 0
count39 = 0
count40 = 0
count41 = 0
count42 = 0
count43 = 0
count44 = 0
count45 = 0
count46 = 0
count47 = 0
count48 = 0
count49 = 0
count50 = 0
count51 = 0
count52 = 0
count53 = 0
count54 = 0
count55 = 0
count56 = 0
count57 = 0
count58 = 0
count59 = 0
count60 = 0
count61 = 0
count62 = 0
count63 = 0
count64 = 0
count65 = 0
count66 = 0
count67 = 0
count68 = 0
count69 = 0
count70 = 0
count71 = 0
count72 = 0
count73 = 0
count74 = 0
count75 = 0
count76 = 0
count77 = 0

#Starts a loop that opens individual .txt files named "pr_1..2...3.. etc.", reads the text of that file as one big string,
#searches for that string and finds count and adds it to the final count
for file in range(1, 3):
    infile = open("pr_" + str(file) + ".txt", "rb")
    pr_text = infile.read()


    ref1 = pr_text.count(string1)
    ref2 = pr_text.count(string2)
   #  ref3 = pr_text.count(string3)
   # # ref4 = pr_text.count(string4)
   #  ref5 = pr_text.count(string5)
   #  ref6 = pr_text.count(string6)
   #  ref7 = pr_text.count(string7)
   #  ref8 = pr_text.count(string8)
   #  ref9 = pr_text.count(string9)
   #  ref10 = pr_text.count(string10)


    count1 = count1 + ref1
    count2 = count2 + ref2
    #count3 = count3 + ref3
    #count4 = count4 + ref4
    #count5 = count5 + ref5
    #count6 = count6 + ref6
    #count7 = count7 + ref7
    #count8 = count8 + ref8
    #count9 = count9 + ref9
    #count10 = count10 + ref10

#Prints the final counter
print("Rogers Park:" + str(count1))
print("West Ridge:" + str(count2))
print("Uptown:" + str(count3))
print("Lincoln Square:" + str(count4))
print("West Ridge:" + str(count5))
print("West Ridge:" + str(count6))
print("West Ridge:" + str(count7))
print("West Ridge:" + str(count8))
print("West Ridge:" + str(count9))
print("West Ridge:" + str(count10))





