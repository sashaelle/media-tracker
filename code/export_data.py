import sqlite3 as sql
import csv
from tkinter import filedialog, messagebox

def export_tracked_titles(profile):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")],
        initialfile=f"{profile}_tracked_titles.csv"
    )

    if not file_path:
        return

    conn = sql.connect("media_tracker.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            profile,
            title,
            media_type,
            status,
            rating,
            review,
            date_added
        FROM tracker
        WHERE profile = ?
        ORDER BY title
    """, (profile,))

    tracked_titles = cursor.fetchall()
    conn.close()

    if not tracked_titles:
        messagebox.showwarning("No Data", "No tracked titles to export.")
        return

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Profile",
            "Title",
            "Media Type",
            "Status",
            "Rating",
            "Review",
            "Date Added"
        ])

        writer.writerows(tracked_titles)

    messagebox.showinfo("Export Complete", f"Exported to:\n{file_path}")