from tkinter import *
from tkinter.ttk import Combobox
<<<<<<< Updated upstream
from tracked_title import track_title
    
def open_title_window(title, release_year, media_id, profile_window, profile_name, media_type):                
=======
from tkinter import messagebox
from tracked_title import track_title, delete_tracked_title

def open_title_window(title, 
                      release_year, 
                      media_id, 
                      profile_window, 
                      profile_name, 
                      media_type, 
                      existing_entry=None):   
                 
>>>>>>> Stashed changes
    title_window = Toplevel(profile_window)
    title_window.title("Title Details")
    title_window.geometry("1000x900")

    #--------------------------------------------------Header Frame----------------------------------------------------------#
    headerFrame = Frame(title_window, width=1000, height=100)
    headerFrame.grid(row=0, column=0, padx=10, pady=10)
    headerFrame.grid_propagate(False)

    titleLabel = Label(headerFrame, text=f'Title: {title}', font=("Arial", 16))
    release_yearLabel = Label(headerFrame, text=f'Release Year: {release_year}', font=("Arial", 12))
    titleLabel.grid(row=0, column=0, padx=10)
    release_yearLabel.grid(row=1, column=0, padx=10)

                     
    #--------------------------------------------------Track Feature Frame----------------------------------------------------------#

    trackingFrame = Frame(title_window, width=1000, height=100)
    trackingFrame.grid(row=1, column=0, padx=10, pady=10)
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
    trackingLabel.grid(row=1, column=0, padx=10)
    trackingComboBox.grid(row=2, column=0, padx=10)


        
    #--------------------------------------------------Rating Feature Frame----------------------------------------------------------#
    ratingFrame = Frame(title_window, width=1000, height=100)
    ratingFrame.grid(row=2, column=0, padx=10, pady=1)
    ratingFrame.grid_propagate(False)

    # Saved value for rating
    saved_rating = StringVar(ratingFrame, "1")
    saved_rating.set("0")

    #Function to set the rating when a button is clicked
    def set_rating(rating):
        saved_rating.set(rating)
        print(f"Rating set to: {saved_rating.get()}") #checking if the rating is being set correctly

    #Rating widgets
    ratingLabel = Label(ratingFrame, text="Rating: ", font=("Arial", 12))           
    values = {"1 Star": "1", 
              "2 Stars": "2", 
              "3 Stars": "3", 
              "4 Stars": "4", 
              "5 Stars": "5"}
    
    for (text, value) in values.items():
        Radiobutton(ratingFrame, 
                    text = text, 
                    variable = saved_rating, 
                    value = value, 
                    indicator = 0).grid(row=1, 
                                        column=int(value)-1, 
                                        padx=5)
        
    
    #Positioning the widgets inside Rating Frame
    ratingLabel.grid(row=0, column=0, padx=10)
    
    #--------------------------------------------Rating Description Feature Frame----------------------------------------------------#
    ratingDescriptionFrame = Frame(title_window, width=1000, height=100)
    ratingDescriptionFrame.grid(row=3, column=0, padx=10, pady=10)
    ratingDescriptionFrame.grid_propagate(False)

    ratingDescriptionLabel = Label(ratingDescriptionFrame, text="(Hint: Scale of 1-5, with 1 being the lowest and 5 being the highest)")
    ratingDescriptionLabel.grid(row=0, column=0, padx=10)

    #--------------------------------------------------Review Feature Frame----------------------------------------------------------#
    reviewFrame = Frame(title_window, width=1000, height=400)
    reviewFrame.grid(row=4, column=0, padx=10, pady=10)
    reviewFrame.grid_propagate(False)

    #Saved user input for review
    saved_review = StringVar()
    saved_review.set("")

    #Default text for review text field
    placeholder = "Write your review here..."

    #Widgets for review frame
    reviewLabel = Label(reviewFrame, text="Review:", font=("Arial", 12))
    reviewTextField = Text(reviewFrame, width=50, height=10)
    reviewTextField.insert("1.0", placeholder)


    #Function to clear the default text when the text field is clicked
    def on_focus_in(event):
        if reviewTextField.get("1.0", "end-1c") == placeholder:
            reviewTextField.delete("1.0", "end")

    #Function to return the default text if the user clicks out of the text field without writing a review
    def on_focus_out(event):
        if reviewTextField.get("1.0", "end-1c").strip() == "":
            reviewTextField.insert("1.0", placeholder)

    #Calling the functions to clear and return the placeholder text
    reviewTextField.bind("<FocusIn>", on_focus_in)
    reviewTextField.bind("<FocusOut>", on_focus_out)


    #Function to save all the user input from the title details window and save it to the account specific tracker database
    def save_entry():
        # Get review text
        review = reviewTextField.get("1.0", END).strip()
        saved_review.set(review)

        # Get other values
        status = trackingComboBoxVar.get()
        rating = saved_rating.get()

        # Save to database
        track_title(profile_name, media_id, title, status, rating, review, media_type)

        print("Saved everything to database!")
<<<<<<< Updated upstream
=======
        title_window.destroy() # Close the title details window after saving the entry

    def delete_entry():
        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Delete '{title}'?"
        )

        if confirm:
            delete_tracked_title(profile_name, media_id)
            messagebox.showinfo("Deleted", f"'{title}' was deleted.")
            print("Deleted tracked title from database!")
            title_window.destroy()
>>>>>>> Stashed changes
 

    #Positioning the widgets inside Rating Frame
    reviewLabel.grid(row=0, column=0, padx=10)
    reviewTextField.grid(row=1, column=0, padx=10)
<<<<<<< Updated upstream
    submitButton = Button(reviewFrame, text="Save Entry", command=save_entry)
    submitButton.grid(row=2, column=0, padx=10)
        
    
=======

    buttonFrame = Frame(reviewFrame)
    buttonFrame.grid(row=2, column=0, pady=10)

    submitButton = Button(buttonFrame, text="Save Entry", command=save_entry)
    submitButton.pack(side="left", padx=5)

    deleteButton = Button(buttonFrame, text="Delete Entry", command=delete_entry)
    deleteButton.pack(side="left", padx=5)
>>>>>>> Stashed changes

    #Rating variable and function
    count = 0
    ans = StringVar(ratingFrame)
    ans.set("Unrated")
    increments = 0

        
def increment_count(x):
    global count,increments,ans
    count += x
    increments+=1
    ans.set(str(count/increments))
    return ans