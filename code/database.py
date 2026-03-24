import pandas as pd
import sqlite3 as sql

def netflix_table():
    #In this cell, we load the data.
    try:
        #load the csv data from github
        csv_data_c = pd.read_csv("https://raw.githubusercontent.com/sashaelle/media-tracker/refs/heads/main/code/netflix_titles.csv")

        #Connect to a database
        conn = sql.connect('media_tracker.db')

        #Load the csv data into a table using the connection to the db
        #that you just created in the previous line.
        csv_data_c.to_sql('netflix', conn, if_exists='replace', index = False)

        return csv_data_c
    

    except ValueError:
        print("""Table already exists or another ValueError occurred.""")
        return None

def tracker_table():
    #In this cell, we create a table to track the media that we have watched.
    try:
        print("Creating tracker table if it doesn't exist...")
        #Connect to a database
        conn = sql.connect('media_tracker.db')
        cursor = conn.cursor()

        #Create a table to track the media that we have watched.
        cursor.execute("""CREATE TABLE IF NOT EXISTS tracker (
                            tracker_id INTEGER PRIMARY KEY,
                            media_id INTEGER,
                            title TEXT,
                            status TEXT,
                            rating REAL,
                            review TEXT,
                            media_type TEXT,
                            date_added DATE
                        )""")
        conn.commit()
        conn.close()
        print("Tracker table created (if it didn't exist).")
    
    except ValueError:
        print("""Table already exists or another ValueError occurred.""")