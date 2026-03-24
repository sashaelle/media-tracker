import sqlite3 as sql

def search(title):
    conn = sql.connect('media_tracker.db')
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * 
        FROM netflix
        WHERE title LIKE ?
        ORDER BY release_year DESC
        """, 
        (f"%{title}%",)
        )
    
    results = cursor.fetchall()
    
    conn.close()
    return results