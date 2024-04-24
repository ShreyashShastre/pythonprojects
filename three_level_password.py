import tkinter as tk
from tkinter import messagebox

# Function to validate the password and grant access level
def validate_password():
    password = password_entry.get()

    if password == "admin123":
        messagebox.showinfo("Success", "Welcome! You have access to Level 3.")
    elif password == "user123":
        messagebox.showinfo("Success", "Welcome! You have access to Level 2.")
    elif password == "guest123":
        messagebox.showinfo("Success", "Welcome! You have access to Level 1.")
    else:
        messagebox.showerror("Error", "Invalid password!")

# Create the main window
root = tk.Tk()
root.title("Password System")

# Create labels and entries for password
tk.Label(root, text="Enter Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create a button to validate the password
validate_button = tk.Button(root, text="Login", command=validate_password)
validate_button.pack()

# Run the main event loop
root.mainloop()
