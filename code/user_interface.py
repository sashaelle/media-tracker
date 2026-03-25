from tkinter import *
from media_search import search

#-------------------------------------------------Functions------------------------------------------------------------#

#Searching for a title from the database and displaying the results
def query():
    userSearchedTitle = searchTextField.get()
    print(f"Searching for... {userSearchedTitle}")  # Debugging print statement
    for row in search(userSearchedTitle):
        print(row)
        listbox.insert(END, row)
    print("Search Complete\n")

#Selecting an item from the listbox
def on_select(event):
    widget = event.widget
    selection = widget.curselection()

    if selection:
        index = selection[0]
        data = widget.get(index)
        print(f"You selected: {index}:'{data}'")
        open_title_window()
              


#---------------------------------------------------------Set Up---------------------------------------------------------------#
root = Tk()
root.title("Personal Media Tracker")

root.geometry("1000x900")

#Welcome Header
welcomeLabel = Label(root, text="Welcome to Personal Media Tracker")
welcomeLabel.pack(padx=10,pady=10,anchor="center")

#--------------------------------------------------Search Feature Frame--------------------------------------------------------#
searchFrame = Frame(root, width=1000, height=100)

#Variable for search box
searchBoxVar = StringVar()

#Widgets for search feature
searchTextField = Entry(searchFrame, width=30,textvariable=searchBoxVar, text="Enter Title or Keyword")
searchButton = Button(searchFrame, text="Search", command=query)

#Positioning the widgets
searchFrame.pack(padx=10,pady=10,anchor="center")
searchTextField.grid(row=1, column=0)
searchButton.grid(row=1, column=1, padx=10)

#-------------------------------------------------Search Results Frame----------------------------------------------------------#
# create listbox object
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


#--------------------------------------------------Track Feature Frame----------------------------------------------------------#



#-------------------------------------------Rating and Reviews Feature Frame----------------------------------------------------#
#Opening a Title window
from tkinter import *

# Assuming root exists and increment_count is defined elsewhere
def open_title_window():                
    title_window = Toplevel(root)
    title_window.title("Title Details")
    title_window.geometry("1000x900")
    
    # 1. Create Frame
    ratingFrame = Frame(title_window, width=1000, height=100)
    # 2. Place Frame in Toplevel
    ratingFrame.grid(row=0, column=0, padx=10, pady=10)
    # 3. Optional: Prevent frame from shrinking to 1x1
    ratingFrame.grid_propagate(False)

    # Saved value for rating
    saved_value = IntVar()
    saved_value.set(0)

    #Widgets for title details window - DONT grid on the same line
    ratingLabel = Label(ratingFrame, text="Rating: ", font=("Arial", 12))                
    ratingOne = Button(ratingFrame, text="1", borderwidth=3, relief="raised", padx=5, pady=10, command=lambda:increment_count(1))
    ratingTwo = Button(ratingFrame, text="2", borderwidth=3, relief="raised", padx=5, pady=10, command=lambda:increment_count(2))
    ratingThree = Button(ratingFrame, text="3", borderwidth=3, relief="raised", padx=5, pady=10, command=lambda:increment_count(3))
    ratingFour = Button(ratingFrame, text="4", borderwidth=3, relief="raised", padx=5, pady=10, command=lambda:increment_count(4))
    ratingFive = Button(ratingFrame, text="5", borderwidth=3, relief="raised", padx=5, pady=10, command=lambda:increment_count(5))

    #Positioning the widgets inside ratingFrame
    ratingLabel.grid(row=0, column=0, padx=10)
    ratingOne.grid(row=1, column=0, padx=10)
    ratingTwo.grid(row=1, column=1, padx=10)
    ratingThree.grid(row=1, column=2, padx=10)
    ratingFour.grid(row=1, column=3, padx=10)
    ratingFive.grid(row=1, column=4, padx=10)

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
