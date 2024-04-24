import tkinter as tk

def book_flight():
    destination = destination_entry.get()
    departure_date = departure_date_entry.get()
    return_date = return_date_entry.get()
    passengers = passengers_entry.get()
    
    # Here you can implement the booking process or display a confirmation message
    confirmation_message = f"Flight booked to {destination} for {passengers} passengers.\nDeparture: {departure_date}\nReturn: {return_date}"
    tk.messagebox.showinfo("Booking Confirmation", confirmation_message)

# Create the main window
root = tk.Tk()
root.title("Travel and Tourism Application")

# Create labels and entries for booking details
tk.Label(root, text="Destination:").grid(row=0, column=0, padx=5, pady=5)
destination_entry = tk.Entry(root)
destination_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Departure Date:").grid(row=1, column=0, padx=5, pady=5)
departure_date_entry = tk.Entry(root)
departure_date_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Return Date:").grid(row=2, column=0, padx=5, pady=5)
return_date_entry = tk.Entry(root)
return_date_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Passengers:").grid(row=3, column=0, padx=5, pady=5)
passengers_entry = tk.Entry(root)
passengers_entry.grid(row=3, column=1, padx=5, pady=5)

# Create a button to book the flight
book_button = tk.Button(root, text="Book Flight", command=book_flight)
book_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Run the main event loop
root.mainloop()
