PR Dataset - Documentation
-----
###Data Cleaning Assessment

######Description of Cleaning Needs

- Once the data is webscraped, post-processing is required for the columns. In the web scraping script, all commas are replaced with pipes (|) and need to be re-replaced using another Python script, titled "__Addinlater__."  

######Programs Required

- Python
- Open Refine (?)

######Time to Process File

- 30-45 minutes

###Authorship, Attribution, or Provenance

- This data was extracted from the press office of the Mayor's Office in the City of Chicago. The press releases were extracted from this website https://www.cityofchicago.org/city/en/depts/mayor/press_room/press_releases.html on October 28, 2018 (?). This dataset was compilied by Aileen Nolan.


###Semantic Contents

######What is Contained in this Dataset?

- This dataset contains press releases published by the Mayor's Office in the City of Chicago. Only press releases published from January 1, 2017 - December 31, 2017 were collected for this dataset. he data extracted includes Press Release titles, publication dates, and actual text of the press releases. 

###Collection Process

######Scripts used for Data Collection

- "Add file name here" 
- "Add file name here" 
 
######Description of Data Collection

- The process used to collect this data includes, gathering the URLs into a .txt file titled "2017urls.txt." Then running the webscraping file titled "___", to extract out the data. Finally, another script is run to get a cleaned version of this dataset which is the final version, titled "Add title here." 

######What do the 'Records' Represent?

Each row in this dataset represents one instance of a press release, published on a particular date. 


######Dimension of Data

- There are approximately 1000 rows of data for this dataset and 3 columns.

######Data Types

- This dataset contains datetime and string data types.


###Data Structure

######Data Format

- CSV file

###Variables

######Variable name: "Title"

- This column is the published title of the press release 
- Data type: String
- Missing values: There are no missing values in this column
 
######Variable name: "Date"

- This column contains the date the press release was published.
- Data type: Datetime
- Missing values: There are no missing values in this column

######Variable name: "Text"

- This column contains the actual press release body text.
- Datatype: String
- Missing values: There are no missing values in this column



