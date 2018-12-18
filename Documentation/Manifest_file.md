## Manifest File

Below are the folders that can be found in my GitHub directory. Below each folder name, I list the files that can be found inside and what they do.

GITHUB REPO: https://github.com/acnolan2/Open_data_mashup

#### Folder: Documentation

- Manifest_file.md
- Assessment_Report.pdf: Documentation describing results and doing initial analysis.
- Data\_Documentation\_HealthAtlas.md: Documentation for preperation of Chicago Health Atlas datasets.
- Data\_Documentation\_PRDataset: Documentation for the preperation of the Intermediate\_PR\_dataset.csv data set.
- Data\_Documentation\_ChicagoDataPortal.md: Documentation of the data collection for the geospatial data from the Chicago Data Portal.
- directions.txt: Directions on how to set-up virtual environment.
- requirements.txt: List of libraries and dependencies used within this project's code.
- Single_slide.pdf: One powerpoint slide deck that is a summary of the entire project.
- ResumeEntry_OpenDataMashup: Entry for this Open Data Mashup project to add to my resume, (personal information is taken out).


#### Folder: Datasets

##### Folder: Final_dataset
- Dictionary_script.py: Python script that creates the main dictionary used to create the final dataset. 
- Final_dataset.csv: The final dataset in CSV form.
- Final\_dataset\_JSON.json: The final dataset in JSON form.
- altnames_csv.csv: Intermediate dataset with alternative names of Chicago Community Areas and sub-neighborhood names.
- Intermediate\_PR\_dataset.csv: Intermediate dataset created from web scraping scripts. 
- Medianincome_ChiHealthAtlas.csv: Intermediate dataset that has been cleaned containing median income information. 
- Unemployment_ChiHealthAtlas.csv: Intermediate dataset that has been cleaned containing unemployment information. 
- Violent\_crime\_in\_public\_spaces\_ChiHealthAtlas.csv: Intermediate dataset that has been cleaned containing crime rate information. 
- Jupyter\_notebook_FinalDatasetCreation.ip: Documentation in jupyter notebook form that discusses in tutorial style how to create the final dataset from my intermediate files.

##### Folder: Intermediate_ChiHealthAtlas_dataset
- Median\_household\_income\_ChiHealthAtlas.xlsx: Original, raw dataset containing median income information downloaded from Chicago Health Atlas website.

- Unemployment_ChiHealthAtlas.xlsx: Original, raw dataset containing unemployment information that was downloaded from Chicago Health Atlas website.

- Violent\_crime\_in\_public\_spaces_ChiHealthAtlas.xlsx: Original, raw dataset containing crime information that was downloaded from Chicago Health Atlas website. 

##### Folder: Intermediate_PR_dataset
- Webscraping\_Script1\_getstxtfiles.py: Python script that hits the Chicago Mayor's Office website to download the HTML from each press release's website and save it as a .txt file.
- 2017urls.txt: Intermediate file that contains all URLs for press release websites. This is fed into the Webscraping_Script1_getstxtfiles.py script.

	##### Folder:pr1003
	- Webscraping\_Script2\_usestxtfiles.py: Second webscraping Python script that uses the files in this folder to create the dataset 'Intermediate_PR_dataset.csv.'
	- pr0-1003.txt: These are the individual HTML files for each press release.

##### Folder: Intermediate_spatial
- Contains all four spatial files required for visualization in Tableau

#### Folder: Failed_code
- Test_script_opentxtfindnamewritecounter.py: Failed counter script. 
- Textanalysis_csvlibrary.py: Failed CSV manipulation script.
- Textanalysis\_Spacy_test.py: Failed Spacy textual analysis script.
