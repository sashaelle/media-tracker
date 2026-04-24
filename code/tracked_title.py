import sqlite3 as sql
import uuid
from datetime import date

def track_title(profile, media_id, title, status, rating, review, media_type):
    conn = sql.connect('media_tracker.db')
    cursor = conn.cursor()

    new_uuid = str(uuid.uuid4())
    date_added = date.today().isoformat()

    tracked = """
    INSERT INTO tracker (
        tracker_id, profile, media_id, title, status, rating, review, media_type, date_added)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT (profile, media_id)
    DO UPDATE SET
        status=excluded.status,
        rating=excluded.rating,
        review=excluded.review
    """

    entry_data = (
        new_uuid, profile, media_id, title, status, rating, review, media_type, date_added
    )

    cursor.execute(tracked, entry_data)
    conn.commit()
    conn.close()

def get_tracked_titles(profile):
    conn = sql.connect('media_tracker.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            t.title,
            n.release_year,
            t.status,
            t.media_id
        FROM tracker t
        JOIN netflix n ON t.media_id = n.show_id
        WHERE t.profile = ?
    """, (profile,))

    rows = cursor.fetchall()
    conn.close()

<<<<<<< HEAD
<<<<<<< Updated upstream
def modify_tracked_title(): 
    return 0
=======
=======
>>>>>>> 18c7fc43475a6189860392df56282a3de404eeea
    return [
        {
            "title": row[0],
            "release_year": row[1],
            "status": row[2],
            "media_id": row[3]
        }
        for row in rows
    ]

def modify_tracked_title(profile, media_id):
    conn = sql.connect('media_tracker.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            t.media_id,
            t.title,
            n.release_year,
            t.status,
            t.rating,
            t.review,
            t.media_type
        FROM tracker t
        JOIN netflix n ON t.media_id = n.show_id
        WHERE t.profile = ? AND t.media_id = ?
    """, (profile, media_id))

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None

    return {
        "media_id": row[0],
        "title": row[1],
        "release_year": row[2],
        "status": row[3],
        "rating": row[4],
        "review": row[5],
        "media_type": row[6]
<<<<<<< HEAD
    }

def delete_tracked_title(profile, media_id):
    conn = sql.connect("media_tracker.db")
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM tracker
        WHERE profile = ? AND media_id = ?
    """, (profile, media_id))

    conn.commit()
    conn.close()
>>>>>>> Stashed changes
=======
    }
>>>>>>> 18c7fc43475a6189860392df56282a3de404eeea
