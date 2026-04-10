from tkinter import *
from tkinter.ttk import Combobox
from media_search import search
from sort_filter import get_filtered_media

#---------------------------------------------------------Set Up---------------------------------------------------------------#
root = Tk()
root.title("Personal Media Tracker")

root.geometry("1000x900")

#Welcome Header
welcomeLabel = Label(root, text="Welcome to Personal Media Tracker")
welcomeLabel.pack(padx=10,pady=10,anchor="center")

#--------------------------------------------------Search Feature Frame--------------------------------------------------------#
#Search for title from database and display results in listbox
def query():
    listbox.delete(0, END)
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
        listbox.insert(END, display_text)
    print("Search Complete\n")

searchFrame = Frame(root, width=1000, height=100)

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
def on_select(event):
    widget = event.widget
    selection = widget.curselection()

    if selection:
        index = selection[0]
        data = widget.get(index)
        print(f"You selected: {index}:'{data}'")
        open_title_window()

searchResultsFrame = Frame(root, width=1000, height=100)

#Widgets for Search Results Frame
searchResultsLabel = Label(searchResultsFrame, text = "Search Results:") 
listbox = Listbox(searchResultsFrame, height = 10, 
                  width = 100, 
                  #bg = "grey",
                  activestyle = 'dotbox', 
                  #font = "Helvetica",
                  #fg = "yellow"
                  )

listbox.bind("<<ListboxSelect>>", on_select)

# pack the widgets
searchResultsFrame.pack(padx=10,pady=10,anchor="center")
searchResultsLabel.grid(row=2, column=1)
listbox.grid(row=3, column=1, columnspan=23, padx=10, sticky="snew")

def open_title_window():                
    title_window = Toplevel(root)
    title_window.title("Title Details")
    title_window.geometry("1000x900")
#--------------------------------------------------Track Feature Frame----------------------------------------------------------#

    trackingFrame = Frame(title_window, width=1000, height=100)
    trackingFrame.grid(row=0, column=0, padx=10, pady=10)
    trackingFrame.grid_propagate(False)

    trackingComboBoxVar = StringVar()
    trackingComboBoxVar.set("Not Watched")

    def update_tracking_status(event):
        selected_status = trackingComboBoxVar.get()
        trackingComboBoxVar.set(selected_status)
        print(f"Tracking status updated to: {selected_status}") #checking if the tracking status is being updated correctly

    trackingOptionsList = ["Not Watched","Watching", "Want to Watch", "Watched"]
    trackingLabel = Label(trackingFrame, text="Tracking Status: ", font=("Arial", 12))
    trackingComboBox = Combobox(trackingFrame, values=trackingOptionsList, textvariable=trackingComboBoxVar, state="readonly")
    trackingComboBox.bind('<<ComboboxSelected>>', update_tracking_status)

    #Positioning the widgets inside Tracking Frame
    trackingLabel.grid(row=0, column=0, padx=10)
    trackingComboBox.grid(row=1, column=0, padx=10)


    
#--------------------------------------------------Rating Feature Frame----------------------------------------------------------#
    ratingFrame = Frame(title_window, width=1000, height=100)
    ratingFrame.grid(row=1, column=0, padx=10, pady=10)
    ratingFrame.grid_propagate(False)

    # Saved value for rating
    saved_rating = IntVar()
    saved_rating.set(0)

    #Function to set the rating when a button is clicked
    def set_rating(rating):
        saved_rating.set(rating)
        print(f"Rating set to: {saved_rating.get()}") #checking if the rating is being set correctly

    #Widgets for title details window 
    ratingLabel = Label(ratingFrame, text="Rating: ", font=("Arial", 12))                
    for i in range(1, 6):
        Button(ratingFrame, text=str(i), borderwidth=3, relief="raised", padx=5, pady=10, command=lambda v=i: set_rating(v)).grid(row=1, column=i-1, padx=10)

    #Positioning the widgets inside Rating Frame
    ratingLabel.grid(row=1, column=0, padx=10)

#--------------------------------------------------Review Feature Frame----------------------------------------------------------#
    reviewFrame = Frame(title_window, width=1000, height=100)
    reviewFrame.grid(row=2, column=0, padx=10, pady=10)
    reviewFrame.grid_propagate(False)

    #Saved user input for review
    saved_review = StringVar()
    saved_review.set("")

    #
    def submit_review():
        text = reviewTextField.get("1.0", END).strip()
        saved_review.set(text)
        print(f"Review submitted: {saved_review.get()}") #checking if the review is being set correctly

    #Widgets for review frame
    reviewLabel = Label(reviewFrame, text="Review:", font=("Arial", 12))
    reviewTextField = Text(reviewFrame, width=50, height=10)
    submitReviewButton = Button(reviewFrame, text="Submit Review", command=submit_review)

    #Positioning the widgets inside Rating Frame
    reviewLabel.grid(row=0, column=0, padx=10)
    reviewTextField.grid(row=1, column=0, padx=10)
    submitReviewButton.grid(row=1, column=1, padx=10)
    

#Rating variable and function
    count = 0
    ans = StringVar(root)
    ans.set("Unrated")
    increments = 0

    
def increment_count(x):
    global count,increments,ans
    count += x
    increments+=1
    ans.set(str(count/increments))
    return ans




root.mainloop()
