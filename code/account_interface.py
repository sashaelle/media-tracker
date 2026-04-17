from tkinter import *
from tkinter import messagebox
from save_profile import save_profile
from user_interface import open_profile_window

root = Tk()
root.title("Personal Media Tracker")

profiles = []
MAX_PROFILES = 4


# --------------------------- Profile Functions --------------------------- #
def create_profile(profile_name):
    profiles.append(profile_name)

    new_button = Button(
        profileFrame,
        text=profile_name,
        command=lambda: select_profile(profile_name),
        wraplength=60,
        width=10,
        height=5
    )

    col_position = len(profiles)
    new_button.grid(row=1, column=col_position, padx=12)
    save_profile(profile_name)

    if len(profiles) == MAX_PROFILES:
        createProfileBtn.destroy()


def select_profile(profile_name):
    currentProfileLabel.config(text=f"Current Profile: {profile_name}")
    open_profile_window(profile_name)


def profile_form():
    if len(profiles) >= MAX_PROFILES:
        messagebox.showwarning("Limit Reached", "You can only create up to 4 profiles.")
        return

    form_window = Toplevel(root)
    form_window.title("Create Profile")

    name_label = Label(form_window, text="Name:")
    name_entry = Entry(form_window)

    name_label.grid(row=0, column=0, padx=10, pady=10)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    create_btn = Button(
        form_window,
        text="Create",
        command=lambda: validate_profile(name_entry.get(), form_window)
    )
    create_btn.grid(row=1, column=0, columnspan=2, pady=10)


def validate_profile(profile_name, form_window):
    if not profile_name.strip():
        messagebox.showwarning("Error", "This field is required!")
        return

    if profile_name in profiles:
        messagebox.showwarning("Error", "That profile already exists!")
        return

    create_profile(profile_name)
    messagebox.showinfo("Success", f"Profile '{profile_name}' created successfully!")
    form_window.destroy()


# --------------------------- Main UI --------------------------- #
profileFrame = Frame(root)
profileFrame.pack(padx=10, pady=10)

welcomeLabel = Label(profileFrame, text="Login or Create a Profile")
welcomeLabel.grid(row=0, column=0, columnspan=5, pady=10)

createProfileBtn = Button(
    profileFrame,
    text="Create Profile",
    command=profile_form,
    wraplength=50,
    width=10,
    height=5,
    activebackground="lightblue",
    background="lightgrey"
)
createProfileBtn.grid(row=1, column=0, padx=12)

currentProfileLabel = Label(root, text="No profile selected")
currentProfileLabel.pack(pady=10)

root.mainloop()