#Program for calculator

import tkinter as tk


def button_click(event):
    current = display.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif text == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, text)


# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create a display widget
display = tk.Entry(root, font=("Arial", 18))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Add buttons to the grid
row = 1
col = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, font=("TimesNewRoman", 14), padx=20, pady=10)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the main loop
root.mainloop()
