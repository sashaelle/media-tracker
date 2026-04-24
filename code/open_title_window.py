from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from tracked_title import track_title, delete_tracked_title

def open_title_window(
    title,
    release_year,
    media_id,
    profile_window,
    profile_name,
    media_type,
    existing_entry=None
):

    title_window = Toplevel(profile_window)
    title_window.title(f"About {title}")
    title_window.geometry("600x900")

    # ---------------- Header ---------------- #
    headerFrame = Frame(title_window, width=600, height=100)
    headerFrame.pack(padx=10, pady=10)

    Label(headerFrame, text=f"{title}", font=("Arial", 24, "bold")).grid(row=0, column=0, padx=10)
    Label(headerFrame, text=f"Release Year: {release_year}", font=("Arial", 12)).grid(row=1, column=0, padx=10)

    # ---------------- Tracking ---------------- #
    trackingFrame = Frame(title_window, width=600, height=100)
    trackingFrame.pack(padx=10, pady=10)

    trackingComboBoxVar = StringVar()

    if existing_entry and existing_entry["status"]:
        trackingComboBoxVar.set(existing_entry["status"])
    else:
        trackingComboBoxVar.set("Not Watched")

    trackingOptionsList = ["Not Watched", "Watching", "Want to Watch", "Watched"]

    Label(trackingFrame, text="Tracking Status:", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=10)

    trackingComboBox = Combobox(
        trackingFrame,
        values=trackingOptionsList,
        textvariable=trackingComboBoxVar,
        state="readonly"
    )
    trackingComboBox.grid(row=2, column=0, padx=10)

    # ---------------- Rating ---------------- #
    ratingFrame = Frame(title_window, width=600, height=100)
    ratingFrame.pack(padx=10, pady=10, anchor="center")

    saved_rating = StringVar(ratingFrame)

    if existing_entry and existing_entry["rating"] is not None:
        saved_rating.set(str(existing_entry["rating"]))
    else:
        saved_rating.set("0")

    Label(ratingFrame,text="Rating:", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=5, pady=5)

    values = {
        "1 Star": "1",
        "2 Stars": "2",
        "3 Stars": "3",
        "4 Stars": "4",
        "5 Stars": "5"
    }

    for text, value in values.items():
        Radiobutton(
            ratingFrame,
            text=text,
            variable=saved_rating,
            value=value,
            indicator=0
        ).grid(row=1, column=int(value) - 1, padx=5)

    # ---------------- Rating Hint ---------------- #
    ratingDescriptionFrame = Frame(title_window, width=600, height=100)
    ratingDescriptionFrame.pack(padx=10, pady=10)

    Label(ratingDescriptionFrame, text="(Scale of 1–5, 1 = lowest, 5 = highest)", font=("Arial", 10)).grid(row=0, column=0, padx=10)

    # ---------------- Review ---------------- #

    reviewFrame = Frame(title_window, width=600, height=400)
    reviewFrame.pack(padx=10, pady=10)

    Label(reviewFrame, text="Review:", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10)

    reviewTextField = Text(reviewFrame, width=50, height=10)
    reviewTextField.grid(row=1, column=0, padx=10)

    placeholder = "Write your review here..."

    def set_placeholder():
        reviewTextField.delete("1.0", END)
        reviewTextField.insert("1.0", placeholder)

    if existing_entry and existing_entry["review"]:
        reviewTextField.insert("1.0", existing_entry["review"])
    else:
        set_placeholder()

    # ---------------- Show Hint Text ---------------- #
    def on_focus_in(event):
        current = reviewTextField.get("1.0", "end-1c")
        if current == placeholder:
            reviewTextField.delete("1.0", END)

    # ---------------- Hide Hint Text ---------------- #
    def on_focus_out(event):
        current = reviewTextField.get("1.0", "end-1c").strip()
        if current == "":
            set_placeholder()

    reviewTextField.bind("<FocusIn>", on_focus_in)
    reviewTextField.bind("<FocusOut>", on_focus_out)

    
    # ---------------- Save Entry ---------------- #
    def save_entry():
        review = reviewTextField.get("1.0", END).strip()

        if review == placeholder:
            review = ""

        status = trackingComboBoxVar.get()
        rating = saved_rating.get()

        track_title(profile_name, media_id, title, status, rating, review, media_type)

        print("Saved!")
        title_window.destroy()

    # ---------------- Delete Entry ---------------- #
    def delete_entry():
        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Delete '{title}'?"
        )

        if confirm:
            delete_tracked_title(profile_name, media_id)
            messagebox.showinfo("Deleted", f"'{title}' was deleted.")
            title_window.destroy()

    # ---------------- Buttons ---------------- #
    buttonFrame = Frame(reviewFrame)
    buttonFrame.grid(row=2, column=0, pady=10)

    Button(buttonFrame, text="Save Entry", command=save_entry).pack(side=LEFT, padx=5)
    Button(buttonFrame, text="Delete Entry", command=delete_entry).pack(side=LEFT, padx=5)
    Button(buttonFrame, text="Back", command=title_window.destroy).pack(side=LEFT, padx=5)

    return title_window