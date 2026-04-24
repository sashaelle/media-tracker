import sqlite3 as sql
import uuid 

def save_profile(profile_name):
    new_uuid = str(uuid.uuid4())
    
    conn = sql.connect("media_tracker.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO account (account_id, name)
        VALUES (?, ?)
    """, (new_uuid, profile_name))

    conn.commit()
    conn.close()


def get_profiles():
    conn = sql.connect("media_tracker.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name
        FROM account
        ORDER BY name
    """)

    rows = cursor.fetchall()
    conn.close()

    return [row[0] for row in rows]