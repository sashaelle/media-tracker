from tkinter import *
from media_search import search

root = Tk()
root.title("Personal Media Tracker")

root.geometry("1000x900")

#Welcome Header
welcomeLabel = Label(root, text="Welcome to Personal Media Tracker")
welcomeLabel.pack(anchor="center")

#-----------------Search Feature Frame------------------#
def query():
    userSearchedTitle = searchTextField.get()
    print(f"Searching for... {userSearchedTitle}")  # Debugging print statement
    for row in search(userSearchedTitle):
        print(row)
        listbox.insert(END, row)
    print("Search Complete\n")

searchFrame = Frame(root, width=1000, height=100)
searchFrame.pack(padx=20, pady=20)

searchBoxVar = StringVar()
searchTextField = Entry(searchFrame, width=30,textvariable=searchBoxVar, text="Enter Title or Keyword")
searchTextField.pack(in_=searchFrame, pady=20, side=LEFT)


searchButton = Button(searchFrame, text="Search", command=query)
searchButton.pack(in_=searchFrame, side=RIGHT)

#-----------------Results Frame------------------#
# create listbox object
listbox = Listbox(root, height = 10, 
                  width = 50, 
                  #bg = "grey",
                  activestyle = 'dotbox', 
                  #font = "Helvetica",
                  #fg = "yellow"
                  )

# Define a label for the list.  
label = Label(root, text = "Search Results") 

# pack the widgets
label.pack()
listbox.pack()

root.mainloop()