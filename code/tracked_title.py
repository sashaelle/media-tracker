import sqlite3 as sql
import uuid

conn = sql.connect('media_tracker.db')
cursor = conn.cursor()

def track_title(media_ID, title, release_year, rating, review):
    new_uuid = str(uuid.uuid1()) # Generate a unique identifier

    tracked = "INSERT INTO tracker (tracker_id, media_ID, title, status, rating, review) " \
          "VALUES (?, ?, ?, ?, ?, ?)" \
          "ON CONFLICT (media_ID)" \
          "DO UPDATE SET " \
          "     status=excluded.status, rating=excluded.rating, review=excluded.review"
    entry_data = (new_uuid, media_ID, title, release_year, rating, review)

    cursor.execute(tracked, entry_data)
    conn.commit()

    conn.close()
