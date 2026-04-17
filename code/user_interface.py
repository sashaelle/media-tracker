from tkinter import *
from tkinter.ttk import Combobox
from tracked_title import get_tracked_titles
from media_search import search
from sort_filter import get_filtered_media
from open_title_window import open_title_window

def open_profile_window(profile_name):
    #---------------------------------------------------------Set Up---------------------------------------------------------------#
    profile_window = Toplevel()
    profile_window.title("Personal Media Tracker")

    profile_window.geometry("1000x900")

    #Welcome Header
    welcomeLabel = Label(profile_window, text=f"Welcome, {profile_name}!")
    welcomeLabel.pack(padx=10,pady=10,anchor="center")

    #--------------------------------------------------Search Feature Frame--------------------------------------------------------#
    #Search for title from database and display results in listbox
    def query():
        searchListbox.delete(0, END)
        userSearchedTitle = searchTextField.get()
        selectedType = typeFilterVar.get()
        selectedSort = sortFilterVar.get()
        
        print(f"Searching for... {userSearchedTitle}")  # Debugging print statement
        
        results = get_filtered_media(
            title=userSearchedTitle if userSearchedTitle else None,
            media_type=selectedType if selectedType != "All" else None,
            sort_by=selectedSort
        )
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
            data = widget.get(index)

            print(f"You selected (search): {data}")

            title_part = data.split(" - ")[0]
            title = title_part.split("(")[0].strip()

            release_year = title_part.split("(")[1].split(")")[0]
            media_id = data

            open_title_window(title, release_year, media_id, profile_window, profile_name)

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
            data = widget.get(index)

            print(f"You selected {profile_name}: {data}")

    def load_titles(profile):
        tracked_titles = get_tracked_titles(profile)
        accountListbox.delete(0, END)
        for title in tracked_titles:
            accountListbox.insert(END, title)


    trackedTitleFrame = Frame(profile_window, width=1000, height=100)

    accountTitleLabel = Label(trackedTitleFrame, text="Your Tracked Titles:")

    accountListbox = Listbox(trackedTitleFrame, height=10, width=100)
    accountListbox.bind("<<ListboxSelect>>", on_account_select)

    refreshButton = Button(
        trackedTitleFrame,
        text="Refresh",
        command=lambda: load_titles(profile_name)
    )

    trackedTitleFrame.pack(padx=10, pady=10, anchor="center")

    accountTitleLabel.grid(row=2, column=1)
    accountListbox.grid(row=3, column=1, columnspan=23, padx=10, sticky="snew")
    refreshButton.grid(row=4, column=1, pady=10)