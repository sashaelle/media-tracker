from tkinter import *
from tkinter.ttk import Combobox
from tracked_title import get_tracked_titles, modify_tracked_title
from sort_filter import get_filtered_media
from open_title_window import open_title_window
from export_data import export_tracked_titles

def open_profile_window(profile_name):
    #---------------------------------------------------------Set Up---------------------------------------------------------------#
    profile_window = Toplevel()
    profile_window.title("Personal Media Tracker")

    profile_window.geometry("1000x900")

    #Welcome Header
    welcomeLabel = Label(profile_window, text=f"Welcome, {profile_name}!")
    welcomeLabel.pack(padx=10,pady=10,anchor="center")

    #--------------------------------------------------Search Feature Frame--------------------------------------------------------#
    search_results = [] # Store search results for later use
    
    #Search for title from database and display results in listbox
    def query():
        searchListbox.delete(0, END)

        nonlocal search_results # Declare search_results as nonlocal to modify it within the function
        search_results.clear() # Clear previous search results

        userSearchedTitle = searchTextField.get()
        selectedType = typeFilterVar.get()
        selectedSort = sortFilterVar.get()

        
        print(f"Searching for... {userSearchedTitle}")  # Debugging print statement
        
        results = get_filtered_media(
            title=userSearchedTitle if userSearchedTitle else None,
            media_type=selectedType if selectedType != "All" else None,
            sort_by=selectedSort
        )

        search_results = results # Store results for later use

        for row in results:
            display_text = f"{row[0]} ({row[1]}) - {row[2]}"
            searchListbox.insert(END, display_text)
        print("Search Complete\n")

    searchFrame = Frame(profile_window, width=1000, height=100)

    #Variable for search box and filter box
    searchBoxVar = StringVar()
    typeFilterVar = StringVar(value="All")
    sortFilterVar = StringVar(value="Newest")

    #Widgets for search feature
    searchTextField = Entry(searchFrame, width=30,textvariable=searchBoxVar, text="Enter Title or Keyword")
    searchButton = Button(searchFrame, text="Search", command=query)

    #Widgets for sort and filter feature
    typeCombo = Combobox(searchFrame, textvariable=typeFilterVar, width=10, state="readonly")
    typeCombo['values'] = ("All", "Movie", "TV Show")
    sortCombo = Combobox(searchFrame, textvariable=sortFilterVar, width=10, state="readonly")
    sortCombo['values'] = ("Newest", "Oldest", "A-Z")

    #Positioning the widgets
    searchFrame.pack(padx=10,pady=10,anchor="center")
    searchTextField.grid(row=1, column=0, padx=5)
    typeCombo.grid(row=1, column=1, padx=5)
    sortCombo.grid(row=1, column=2, padx=5)
    searchButton.grid(row=1, column=3, padx=10)

    #-------------------------------------------------Search Results Frame----------------------------------------------------------#
    #Selecting an item from the listbox
    def on_search_select(event):
        widget = event.widget
        selection = widget.curselection()

        if selection:
            index = selection[0]
            row =  search_results[index]  # Get the corresponding row from search results

            print(f"You selected (search): {row[0]}")  # Debugging print statement
           
            title = row[0]
            release_year = row[1]
            media_id = row[3]
            media_type = row[2]

            profile_window.withdraw()

            title_window = open_title_window(
                title,
                release_year,
                media_id,
                profile_window,
                profile_name,
                media_type
            )

            profile_window.wait_window(title_window)

            profile_window.deiconify()
            load_titles(profile_name)

    searchResultsFrame = Frame(profile_window, width=1000, height=100)

    #Widgets for Search Results Frame
    searchResultsLabel = Label(searchResultsFrame, text = "Search Results:") 
    searchListbox = Listbox(searchResultsFrame, height = 10, 
                    width = 100, 
                    #bg = "grey",
                    activestyle = 'dotbox', 
                    #font = "Helvetica",
                    #fg = "yellow"
                    )

    searchListbox.bind("<<ListboxSelect>>", on_search_select)

    # Format the widgets
    searchResultsFrame.pack(padx=10,pady=10,anchor="center")
    searchResultsLabel.grid(row=2, column=1)
    searchListbox.grid(row=3, column=1, columnspan=23, padx=10, sticky="snew")

    #-------------------------------------------------Account Tracked Title Frame----------------------------------------------------------#
    def on_account_select(event):
        widget = event.widget
        selection = widget.curselection()

        if selection:
            index = selection[0]
            selected_media_id = widget.media_map[index]

            print(f"You selected {profile_name}: {selected_media_id}")

            entry = modify_tracked_title(profile_name, selected_media_id)

            if entry:
                profile_window.withdraw()  # 👈 hide profile/search window

                title_window = open_title_window(
                    entry["title"],
                    entry["release_year"],
                    entry["media_id"],
                    profile_window,
                    profile_name,
                    entry["media_type"],
                    entry
                )

                profile_window.wait_window(title_window)  

                profile_window.deiconify()  
                load_titles(profile_name)  

    def load_titles(profile):
        accountListbox.media_map.clear()
        accountListbox.delete(0, END)

        titles = get_tracked_titles(profile)

        for i, row in enumerate(titles):
            display = f"{row['title']} ({row['release_year']}) - {row['status']}"
            accountListbox.insert(END, display)
            accountListbox.media_map[i] = row["media_id"]

    trackedTitleFrame = Frame(profile_window, width=1000, height=100)

    accountTitleLabel = Label(trackedTitleFrame, text="Your Tracked Titles:")

    accountListbox = Listbox(trackedTitleFrame, height=10, width=100)
    accountListbox.bind("<<ListboxSelect>>", on_account_select)
    accountListbox.media_map = {}

    refreshButton = Button(
        trackedTitleFrame,
        text="Refresh",
        command=lambda: load_titles(profile_name)
    )

    trackedTitleFrame.pack(padx=10, pady=10, anchor="center")

    accountTitleLabel.grid(row=2, column=1)
    accountListbox.grid(row=3, column=1, columnspan=23, padx=10, sticky="snew")
    refreshButton.grid(row=4, column=1, pady=10)

    load_titles(profile_name)

    exportButton = Button(
        trackedTitleFrame,
        text="Export Data",
        command=lambda: export_tracked_titles(profile_name)
    )
    
    exportButton.grid(row=4, column=2, pady=10)

    def on_close():
        profile_window.destroy()
        profile_window.master.deiconify()  

    profile_window.protocol("WM_DELETE_WINDOW", lambda: on_close())