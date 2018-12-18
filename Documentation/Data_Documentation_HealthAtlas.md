Documentation - Chicago Health Atlas Dataset 
-----
### Data Cleaning Assessment

###### Description of Cleaning Needs
This document discusses how three intermediate datasets were cleaned for use in my Open Data Mashup project. The three intermediate datasets are: 

"Median_household_income_ChiHealthAtlas.xlsx,"
"Unemployment_ChiHealtAtlas.xlsx," and "Violent_crime_in_public_spaces_ChiHealthAtlas.xlsx."  

Each of these files only required minimal hand cleaning including the deletion of rows and extraneous text like quotation marks. The specific details of how each dataset was cleaned is below.

Each of the three datasets below were downloaded from specific webpages on the Chicago Health Atlas Website. These websites are listed in this document under the data collection header. Using those raw files, the only cleaning I did on each file was as follows.

"Median_household_income_ChiHealthAtlas.xlsx"

- Delete columns A, B, C, K-AA. 
- Delete rows 32-41, 119 - 272
- Removed hyphenation in Community Area name 

"Unemployment_ChiHealtAtlas.xlsx"

- Delete columns A, B, K-R, T-AA
- Delete rows 44-57, 135-288
- Removed hyphenation in Community Area name 

"Violent_crime_in_public_spaces.xlsx"

- Delete columns A, B, K-AA
- Delete rows 2-174
- Removed hyphenation in Community Area name 

###### Programs Required

- Microsoft Excel or Numbers
- Python Pycharm (optional)

###### Time to Process File

- 10 minutes per file

### Authorship, Attribution, or Provenance

###### What is Contained in this Dataset?

- This dataset was created by The Smart Chicago Collaborative and the Chicago Department of Public Health.

### Semantic Contents

###### What is Contained in this Dataset?

- This dataset will contain data on information regarding Chicago of Chicago "Community Areas." They contain data on community health indicators specifically median income, unemployment rate, and number of crimes committed in public. This data will aim to supplement the press release data.

### Collection Process

###### Scripts used for Data Collection

- None, N/A

###### Description of Data Collection

The data is freely available and downloaded from the Chicago Health Atlas website. Below I have provided the links of the webpages where I downloaded each of the three community health indicators. On each of these pages the download button is located on the top right corner.  
 
- Median Household Income: https://www.chicagohealthatlas.org/indicators/median-household-income
- Unemployment Rate: https://www.chicagohealthatlas.org/indicators/unemployment
- Crimes Committed in Public: https://www.chicagohealthatlas.org/indicators/violent-crime-in-public-spaces

###### What do the 'Records' Represent?

- Each record represents a City of Chicago Community Area which is a common division of neighborhoods used for research and urban planning purposes.

###### Dimension of Data
"Median_household_income_ChiHealthAtlas.xlsx" <br>
- Originally: 27 columns X 272 rows <br>
- After cleaning: 3 columns X 78 rows
 
"Unemployment_ChiHealtAtlas.xlsx" <br> 
- Originally: 27 columns C 288 rows <br>
- After cleaning: 3 columns X 78 rows

"Violent_crime_in_public_spaces_ChiHealthAtlas.xlsx" <br>
- Originally: 27 columns X 603 rows <br>
- After cleaning: 4 columns X 78 rows

###### Data Types

- String

### Data Structure

###### Data Format

- These files are all CSV files.

### Variables

###### Variable name: "Number"
- In each file this column name represents the health indicator of interest. It is either the amount of unemployment within subcategories of the population, it is the amount of crime committed within a neighborhood within a set period of time, or the median income of all residents.
- Data type: String
- Missing values: Unknown
