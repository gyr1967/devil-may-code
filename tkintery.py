import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Create the main application window
root = tk.Tk()
root.title("Image, Text Entry, and Text Box")

# Create a function to update the text box
def update_text():
    text = entry.get()
    text_box.delete(1.0, "end")  # Clear the existing text
    text_box.insert("insert", f"You entered: {text}")

# Load the image
image = Image.open("abaddon.png")
image = image.resize((200, 200))
image = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = ttk.Label(root, image=image)
image_label.pack()

# Create a text entry box
entry = ttk.Entry(root)
entry.pack()

# Create a text box
text_box = tk.Text(root, height=10, width=40)
text_box.pack()

# Create a submit button
submit_button = ttk.Button(root, text="Submit", command=update_text)
submit_button.pack()

# Start the tkinter main loop
root.mainloop()
