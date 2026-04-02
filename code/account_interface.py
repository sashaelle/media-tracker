from tkinter import *

root = Tk()
root.title("Personal Media Tracker")

# root.geometry("1000x900")

#---------------------------Profile Frame---------------------------#
def create_profile():
    print("Creating profile...")

profileFrame = Frame(root, width=1000, height=100)
welcomeLabel = Label(profileFrame, text="Login or Create a Profile")
welcomeLabel.grid(row=0, column=0, columnspan=2, pady=10)
# Widgets for profile frame
# profileLabel = Label(profileFrame, text="Profile Name: ")

#Positioning the widgets
profileFrame.pack(padx=10,pady=10,anchor="center")
# profileLabel.grid(row=0, column=0)

dummyProfile = Button(profileFrame, 
                      text="Dummy Profile", 
                      command=lambda: print("Dummy profile selected"),
                      wraplength=50,
                      width = 10,
                      height = 5)
dummyProfile.grid(row=1, column=0, padx=12)

createProfileBtn = Button(profileFrame, 
                          text="Create Profile", 
                          command=create_profile,
                          wraplength=50,
                          width = 10,
                          height = 5)
createProfileBtn.grid(row=1, column=1, padx=12)

root.mainloop()
