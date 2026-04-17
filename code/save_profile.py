import sqlite3 as sql
import uuid 

def save_profile(name):
    conn = sql.connect('media_tracker.db')
    cursor = conn.cursor()

    new_uuid = str(uuid.uuid4())

    account = """
                INSERT INTO account (account_id, name)
                VALUES (?, ?)
                ON CONFLICT (account_id)
                DO UPDATE SET
                    name=excluded.name
                """

    entry_data = (new_uuid, name)

    cursor.execute(account, entry_data)
    conn.commit()
    conn.close()
