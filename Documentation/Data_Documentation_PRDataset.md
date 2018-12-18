PR Dataset - Documentation
-----
### Data Cleaning Assessment

###### Description of Cleaning Needs

Once the data is webscraped, no post-processing is required for the columns though it would be helpful to have some. Since this is an intermediary dataset, however, this is not required. 

###### Programs Required

- Python

###### Time to Process File

- 5 minutes

### Authorship, Attribution, or Provenance

- This data was extracted from the press office of the Mayor's Office in the City of Chicago. The press releases were extracted from this website https://www.cityofchicago.org/city/en/depts/mayor/press_room/press_releases.html on October 28, 2018. This dataset was compilied by Aileen Nolan.


### Semantic Contents

###### What is Contained in this Dataset?

- This dataset contains press releases published by the Mayor's Office in the City of Chicago. Only press releases published from January 1, 2017 - December 31, 2017 were collected for this dataset. he data extracted includes Press Release titles, publication dates, and actual text of the press releases. 

### Collection Process

###### Scripts used for Data Collection

- "Webscraping_Script1_getstxtfiles.py" 
	- Uses "2017urls.txt"
- "Webscraping_Script2_usestxtfiles.py" 
 
###### Description of Data Collection

- The process used to collect this data includes, gathering the URLs into a .txt file titled "2017urls.txt." Then running the two web scraping files mentioned above in succession to extract out the data.  

###### What do the 'Records' Represent?

Each row in this dataset represents one instance of a press release published on a particular date. 


###### Dimension of Data

- There are approximately 1003 rows of data for this dataset and 4 columns.

###### Data Types

- This dataset contains datetime and string data types.


### Data Structure

###### Data Format

- CSV file

### Variables

###### Variable name: "pr_id"
- This is a unique identifier for each press release which corresponds with the incrementing number used in the file name for each webscraped press release.

###### Variable name: "Title"

- This column is the published title of the press release 
- Data type: String
- Missing values: There are no missing values in this column
 
###### Variable name: "Date"

- This column contains the date the press release was published.
- Data type: Datetime
- Missing values: There are no missing values in this column

###### Variable name: "Text"

- This column contains the actual press release body text.
- Datatype: String
- Missing values: There are no missing values in this column



