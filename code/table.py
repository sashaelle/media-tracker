from database import netflix_table, tracker_table

netflix_table() # load the data into the database
tracker_table() # create the tracker table if it doesn't exist

print("Data loaded and tracker table created (if it didn't exist).")

