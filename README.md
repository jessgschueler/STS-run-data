# Slay the Spire run data pipeline using Big Query 

### by Jess Schueler

#### *Using Python, pandas, and big query to explore three months worth of personal Slay the Spire runs*

## Technologies Used
* Python
* Pandas
* GCP
* BigQuery
* SQL
* Jupyter Notebook

## Description 
A data pipeline that intakes raw .run files from the Mega Crit Studios game Slay the Spire and transforms it into usable data for Big Query data analytics. Runs basic transformations of the files, converts them to CSV files, and then inputs those CSV files into pandas dataframes. These dataframes undergo some more data cleaning, and then are read to BigQuery. This is a passion project of mine and I look forward to continuing to improve it, and would hope to be able to include larger amounts of data in the future. 

## Setup/Installation Requirements
* In the terminal, clone github repository using the following command;
    ```
    $ git clone https://github.com/jessgschueler/STS-run-data
    ```
* In a venv, Pip install requirements.txt file
* Add data into directory, I used separate directories for each character. 
* Run data through functions in dataprep.ipynb, which should ghive you four CSV files.
* Run main.py file.
* Sample queries are in sts.sql file. 

## Known Bugs
* The run_totsv() function in dataprep.ipynb currently gives an error.
* The dataset has low usability, and needs more cleaning before it can be properly analyzed. 

## License
MIT

Copyright (c) 5/20/22 Jess Schueler
