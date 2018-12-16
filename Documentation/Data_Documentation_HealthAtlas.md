Documentation - Chicago Health Atlas Dataset 
-----
###Data Cleaning Assessment

######Description of Cleaning Needs

- Each Excel workbook will only require minimal hand cleaning. This will involve the deletion of rows and extraneous text like quotation marks. 

PHASE 2 - Create the ChiHealthAtlas_dataset.csv

The next phase in this project is to create the files for the second dataset, ChiHealthAtlas_dataset. This requires hand cleaning which I will describe here for the original three ChiHealthAtlas data files. These three original files are called: "Median_household_income_ChiHealthAtlas.xlsx", "Unemployment_ChiHealtAtlas.xlsx", and "Violent_crime_in_public_spaces.xlsx." 

"Median_household_income_ChiHealthAtlas.xlsx"

-Delete columns A, B, C, K-AA. 
-Delete rows 32-41, 119 - 272

"Unemployment_ChiHealtAtlas.xlsx"

-Delete columns A, B, K-R, T-AA
-Delete rows 44-57, 135-288

"Violent_crime_in_public_spaces.xlsx"

-Delete columns A, B, K-AA
-Delete rows 2-174

######Programs Required

- Microsoft Excel or Numbers
- Python Pycharm (optional)

######Time to Process File

- 10 minutes per file

###Authorship, Attribution, or Provenance

######What is Contained in this Dataset?

- This dataset was created by The Smart Chicago Collaborative and the Chicago Department of Public Health.

###Semantic Contents

######What is Contained in this Dataset?

- This dataset will contain data on information regarding Chicago of Chicago "Community Areas." They contain data on community health indicators specifically median income, unemployment rate, and number of crimes committed in public. This data will aim to supplement the press release data.

###Collection Process

######Scripts used for Data Collection

- None, N/A

######Description of Data Collection

- The data is freely available and downloaded from the Chicago Health Atlas website. Below I have provided the links of the webpages where I downloaded each of the three community health  

######What do the 'Records' Represent?

- Each record represents a City of Chicago neighborhood.

######Dimension of Data

- Unknown

######Data Types

- String

###Data Structure

######Data Format

- This will be likely a CSV file.

###Variables

######Variable name: "Neighborhood"
- This column is the name of a neighborhood in the City of Chicago 
- Data type: String
- Missing values: Unknown

######Variable name: "Median Income"
- This column represents the median income represented in the this neighborhood
- Data type: String
- Missing values: Unknown

######Variable name: "Placehold"
- Unknown
- Data type: String
- Missing values: Unknown
