from database import load_data, tracker_table

load_data() # load the data into the database
tracker_table() # create the tracker table if it doesn't exist

print("Data loaded and tracker table created (if it didn't exist).")

