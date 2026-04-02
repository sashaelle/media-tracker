from tkinter import *
from tkinter import messagebox
from unicodedata import name

root = Tk()
root.title("Personal Media Tracker")

# root.geometry("1000x900")

#---------------------------Profile Frame---------------------------#
def create_profile():
    print("Creating profile...")

def profile_form():
    global form_window
    form_window = Toplevel(root)
    form_window.title("Create Profile")

    name_label = Label(form_window, text="Name:")
    name_entry = Entry(form_window)

    name_label.grid(row=0, column=0, padx=10, pady=10)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    createBtn = Button(form_window, text="Create", command=lambda: validate_profile(name_entry.get()))
    createBtn.grid(row=1, column=0, columnspan=2, pady=10)


def validate_profile(name):
    print("Validating profile...")
    if not name.strip():
        messagebox.showwarning("Error", "This field is required!")
        profile_form()  # Reopen the form for correction
    else:
        create_profile()
        messagebox.showinfo("Success", f"Profile '{name}' created successfully!")
        form_window.destroy()

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
                          command=profile_form,
                          wraplength=50,
                          width = 10,
                          height = 5)
createProfileBtn.grid(row=1, column=1, padx=12)

root.mainloop()
