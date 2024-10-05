Name: Vivek Jitendra Bhole

#Project Discription
We have to fethc the data from a given url to a pdf file.
We then extract the fields from the pdf file and format the data so as to insert it into a database.
Create a database named normanpd.db and a table called incidents to store the data
We populate the table using the extracted data
Query the table to get a list of the nature of incidents and the number of times they have occured

#How to install
pipenv install

##How to run
pipenv run python project0/main.py --incidents <url>

#video/gif


##Functions
####main.py
fetchPDFData(url): This function takes the url as a parameter and fetches the pdf data from the url link as a stream
extractPDFData(data): This function takes the above fetched data and extracts it to raw string format and then formats the data so that it can be inserted into a database table
createdb(): This function created a database named normanpd.db and established a connection to that database and also created a table named 'incidents' in the database
populatedb(data,db): This function takes the formatted data and db connection as parameters and populates the table 'incidents' with the provided data
status(db): This function takes db connection as parameter and queries the 'incident' table to get a list of the nature of incidents and the number of times they have occured

####test_download.py
test_fetchPDFData(): This data checks if the fetchPDFData function in main.py is able to fetch data from the provided url
test_extractPDFData(): This data checks if the extractPDFData function return any data and if yes it also cheks if the data returned is in correct format
test_createdb(): This function checks if the database 'normanpd.db' is created and if a connection is established to the database. It also checks if a table named 'incidents' is created in the database
test_populatedb(): This function checks if the table 'incidents' is populated with the formatted data or not.
test_status(): This function checks if anything is being outputted into the stdout.

##Database Development
Created a Database named 'normanpd.db' with the following fields : incident_time, incident_number, incident_location, nature, incident_ori

##Assumptions
It is assumed that the nature field in the dataset is not multi-line.
