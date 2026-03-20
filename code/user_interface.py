from tkinter import *
root = Tk()
root.title("Personal Media Tracker")

root.geometry("1000x900")

#Welcome Header
welcomeLabel = Label(root, text="Welcome to Personal Media Tracker")
welcomeLabel.pack(anchor="center")

#-----------------Search Feature Frame------------------#
def search():
    userSearchedTitle = searchBoxVar.get()

searchFrame = Frame(root, width=1000, height=100)
searchFrame.pack(padx=20, pady=20)

searchBoxVar = StringVar()
searchTextField = Entry(searchFrame, width=30,textvariable=searchBoxVar, text="Enter Title or Keyword")
searchTextField.pack(in_=searchFrame, pady=20, side=LEFT)


searchButton = Button(searchFrame, text="Search")
searchButton.pack(in_=searchFrame, side=RIGHT)

root.mainloop()