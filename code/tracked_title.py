import sqlite3 as sql
import uuid

def track_title(profile, media_id, title, status, rating, review, media_type):
    conn = sql.connect('media_tracker.db')
    cursor = conn.cursor()

    new_uuid = str(uuid.uuid4())

    tracked = """
    INSERT INTO tracker (tracker_id, profile, media_id, title, status, rating, review, media_type)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT (profile, media_id)
    DO UPDATE SET
        status=excluded.status,
        rating=excluded.rating,
        review=excluded.review
    """

    entry_data = (new_uuid, profile, media_id, title, status, rating, review, media_type)

    cursor.execute(tracked, entry_data)
    conn.commit()
    conn.close()

def get_tracked_titles(profile):
    conn = sql.connect('media_tracker.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT title
        FROM tracker
        WHERE profile = ?
        ORDER BY title
    """, (profile,))

    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]

def modify_tracked_title(): 
    return 0