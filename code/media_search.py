import sqlite3 as sql
import re

def search(title):
    conn = sql.connect('media_tracker.db')
    cursor = conn.cursor()

    conn.create_function(
        "REGEXP", 2,
        lambda pattern, text: 1 if text and re.search(pattern, text, re.IGNORECASE) else 0
    )

    cursor.execute(
        """
        SELECT title, release_year
        FROM netflix
        WHERE title REGEXP ?
        ORDER BY release_year DESC
        LIMIT 15
        """, 
        [rf"\b{re.escape(title)}\b"]
        )
    
    results = cursor.fetchall()
    
    conn.close()
    return results