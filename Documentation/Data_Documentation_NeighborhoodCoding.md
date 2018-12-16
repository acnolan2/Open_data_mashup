Neighborhood Coding - Documentation
-----
###Data Cleaning Assessment

######Description of Cleaning Needs

- This portion of my data processing process will likely need significant cleaning. These columns will be using automated string detection in order to code each press release according to the neighborhood it refers to. 

######Programs Required

- Python 
- Open Refine (?)

######Time to Process File

- Unknown (Add later)

###Authorship, Attribution, or Provenance

- The data in these columns was created by using the program "___". Some handcoding of this data column was done by Aileen Nolan. 

###Semantic Contents

######What is Contained in this Dataset?

- This is not a dataset but documentation for two very specific data columns within the "PR Dataset." These two columns are titled "Neighborhood" and "Civic Issue."


###Collection Process

######Scripts used for Data Collection

- "Add script name here"

######Description of Data Collection

- These columns were collected using scripts that analyze the free text. The scripts analyzed the columns "text" to pick up on and hopefully assign each press release to a Chicago neighborhood and particular civic issue that it was written about.

######What do the 'Records' Represent?

-Each record represents either a Chicago neighborhood name that the press release was about and civic issue.

######Dimension of Data

- Same as the PR Dataset, please refer to the documentation for the PR Dataset. That can be found in the file titled "Data_Documentation_PRDataset."

######Data Types

-String

###Data Structure

######Data Format

-Columns within CSV file

###Variables

######Variable name: "neighborhood_body_scrapy"
- This column contains the name of a neighborhood within the City of Chicago that was mentioned in the press release. This was found through using the Python library Scrapy. Scrapy was used to process the text in the "body" variable. Scrapy pulled out any words that were identified as places.  
- Data type: String
- Missing: A missing value means no appropriate code could be assigned to the press release.

######Variable name: "neighborhood_body_findall"
- This column contains a type of neighborhood that was mentioned in the press releases. This was done by looping through the "body" variable and pulling out neighborhood names that were hardcoded in the script. The neighborhood names chosen as input derive from the format used in the Chicago Health Atlas data. This includes 50+ names and geographical identifiers for different neighborhoods within Chicago. 
- Data type: Categorical
- Missing: A missing value means no appropriate category could be assigned to the press release.
