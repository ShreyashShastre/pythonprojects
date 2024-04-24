import tkinter as tk

def calculate_bmi():
    height = float(height_entry.get()) / 100  # Convert height from cm to meters
    weight = float(weight_entry.get())
    bmi = weight / (height * height)
    result_label.config(text="Your BMI is: {:.2f}".format(bmi))

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create labels and entries for height and weight
tk.Label(root, text="Height (cm):").grid(row=0, column=0, padx=5, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Weight (kg):").grid(row=1, column=0, padx=5, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1, padx=5, pady=5)

# Create a button to calculate BMI
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the main event loop
root.mainloop()
