import sqlite3 as sql
import re

def get_filtered_media(title=None, media_type=None, sort_by="newest", limit=15):
    conn = sql.connect('media_tracker.db')
    cursor = conn.cursor()

    # Enable REGEXP support
    conn.create_function(
        "REGEXP", 2,
        lambda pattern, text: 1 if text and re.search(pattern, text, re.IGNORECASE) else 0
    )

    # Base Query
    query = "SELECT title, release_year, type FROM netflix WHERE 1=1"
    params = []

    # Apply Filters
    if title:
        query += " AND title REGEXP ?"
        params.append(rf"\b{re.escape(title)}\b")
    
    if media_type and media_type != "All":
        query += " AND type = ?"
        params.append(media_type)

    # Apply Sorting logic
    sort_map = {
        "Newest": "release_year DESC",
        "Oldest": "release_year ASC",
        "A-Z": "title ASC"
    }
    selected_sort = sort_map.get(sort_by, "release_year DESC")
    
    query += f" ORDER BY {selected_sort} LIMIT ?"
    params.append(limit)

    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results