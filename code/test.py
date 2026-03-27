from tracked_title import track_title
import sqlite3 as sql

results = track_title("s12", "The Office", "Watched", "2", "Great show!")

conn = sql.connect('media_tracker.db')
cursor = conn.cursor()

cursor.execute(
    """
    SELECT *
    FROM tracker
    """,)
    
results = cursor.fetchall()

for row in results:
    print(row)