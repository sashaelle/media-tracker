import pandas as pd
import sqlite3 as sql

def load_data():
    #In this cell, we load the data.
    try:
        #load the csv data from github
        csv_data_c = pd.read_csv("https://raw.githubusercontent.com/sashaelle/media-tracker/refs/heads/main/code/netflix_titles.csv")

        #Connect to a database
        conn = sql.connect('netflix.db')

        #Load the csv data into a table using the connection to the db
        #that you just created in the previous line.
        csv_data_c.to_sql('netflix', conn, if_exists='replace', index = False)

        return csv_data_c
    

    except ValueError:
        print("""Table already exists or another ValueError occurred.""")
        return None