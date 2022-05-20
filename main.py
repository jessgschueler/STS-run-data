import pandas as pd
import datetime
from google.cloud import bigquery
import pandas as pd


def panda_clean():
    """
    Import our CSV's and write them into pandas dataframes.

    Returns:
        Dataframe: Returns a data 
    """
    #set the columns that we want to use
    cols = ['floor_reached','playtime','items_purged','score','local_time','campfire_choices','master_deck','relics','character_chosen','victory','boss_relics','killed_by','ascension_level']
    #read four CSV's into dataframes
    defect = pd.read_csv('CSVData/defect.csv', usecols=cols)
    watcher = pd.read_csv('CSVData/watcher.csv', usecols=cols)
    silent= pd.read_csv('CSVData/silent.csv', usecols=cols)
    ironclad = pd.read_csv('CSVData/ironclad.csv', usecols=cols)

    #concat all dfs into large df with all characters
    all_char = pd.concat([defect,watcher,silent,ironclad])
    all_char.drop_duplicates(inplace=True)
    #drop rows with repeated header data, and rows where run was abandoned
    completed_run_df = all_char[all_char.floor_reached != 0]
    completed_run_df = all_char[all_char.floor_reached != 'floor_reached']
    #set datatypes
    completed_run_df = completed_run_df.astype({"floor_reached": int, "playtime": int})

    return completed_run_df

def tobig_query():
    """
    Writes our pandas dataframe to BigQuery
    """
    #call pandas_clean function to access df
    completed_run_df = panda_clean()
    #set client object with project id
    client = bigquery.Client(project= 'deb-01-346001')
    #set project dataset and destination table name
    table = 'STS_run_data.april_runs'
    #enter partial schema 
    job_config = bigquery.LoadJobConfig(schema = [
        bigquery.SchemaField("floor_reached", bigquery.enums.SqlTypeNames.INTEGER),
        bigquery.SchemaField("playtime", bigquery.enums.SqlTypeNames.INTEGER)])
    #load df into table
    job = client.load_table_from_dataframe(completed_run_df, table, job_config=job_config)

tobig_query()