import sqlite3 as sql

def search(title):
    conn = sql.connect('media_tracker.db')
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT title, release_year
        FROM netflix
        WHERE title LIKE ?
        ORDER BY release_year DESC
        LIMIT 10
        """, 
        (f"% {title} %",)
        )
    
    results = cursor.fetchall()
    
    conn.close()
    return results