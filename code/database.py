import sqlite3 as sql
import pandas as pd

#this is a comment

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
                            tracker_id TEXT PRIMARY KEY,
                            profile TEXT NOT NULL,
                            media_id TEXT NOT NULL,
                            title TEXT NOT NULL,
                            status TEXT,
                            rating INTEGER,
                            review TEXT,
                            media_type TEXT,
                            date_added DATE,
                            UNIQUE(profile, media_id)
                       )""")
        conn.commit()
        conn.close()
        print("Tracker table created (if it didn't exist).")
    
    except ValueError:
        print("""Table already exists or another ValueError occurred.""")

def account_table():
    try:
        print("Creating accounts table if it doesn't exist...")
        #Connect to a database
        conn = sql.connect('media_tracker.db')
        cursor = conn.cursor()

        #Create a table to track the media that we have watched.
        cursor.execute("""CREATE TABLE IF NOT EXISTS account (
                            account_id TEXT PRIMARY KEY,
                            name TEXT
                        )""")
        conn.commit()
        conn.close()
        print("Accounts table created (if it didn't exist).")
    
    except ValueError:
        print("""Table already exists or another ValueError occurred.""")

#------------------------Database Creation------------------------#
netflix_table() # load the data into the database
tracker_table() # create the tracker table if it doesn't exist
account_table() # create the accounts table if it doesn't exist

print("Data loaded and tracker table created (if it didn't exist).")
