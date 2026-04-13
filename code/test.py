#import uuid
#from tracked_title import track_title
import sqlite3 as sql

#results = track_title("s12", "The Office", "Watched", "2", "Great show!")

#new_uuid = str(uuid.uuid1()) # Generate a unique identifier

#tracked = "INSERT INTO account (account_id, name) " \
#          "VALUES (?, ?)" \
#          "ON CONFLICT (account_id)" \
#          "DO UPDATE SET " \
#          "     name=excluded.name"
#entry_data = (new_uuid, "Crawford")

conn = sql.connect('media_tracker.db')
cursor = conn.cursor()

#cursor.execute(tracked, entry_data)


cursor.execute(
    """
    SELECT *
    FROM tracker
    """,)
    
results = cursor.fetchall()

for row in results:
    print(row)