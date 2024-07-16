import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = ttk.Label(root, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)

        self.length_entry = ttk.Entry(root, width=10)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.uppercase_var = tk.IntVar()
        self.uppercase_check = ttk.Checkbutton(root, text="Include Uppercase", variable=self.uppercase_var)
        self.uppercase_check.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.lowercase_var = tk.IntVar()
        self.lowercase_check = ttk.Checkbutton(root, text="Include Lowercase", variable=self.lowercase_var)
        self.lowercase_check.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.numbers_var = tk.IntVar()
        self.numbers_check = ttk.Checkbutton(root, text="Include Numbers", variable=self.numbers_var)
        self.numbers_check.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.symbols_var = tk.IntVar()
        self.symbols_check = ttk.Checkbutton(root, text="Include Symbols", variable=self.symbols_var)
        self.symbols_check.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.password_label = ttk.Label(root, text="Generated Password:")
        self.password_label.grid(row=6, column=0, padx=10, pady=10)

        self.password_display = ttk.Entry(root, width=30, state="readonly")
        self.password_display.grid(row=6, column=1, padx=10, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be a positive integer.")

            include_uppercase = bool(self.uppercase_var.get())
            include_lowercase = bool(self.lowercase_var.get())
            include_numbers = bool(self.numbers_var.get())
            include_symbols = bool(self.symbols_var.get())

            characters = ''
            if include_uppercase:
                characters += string.ascii_uppercase
            if include_lowercase:
                characters += string.ascii_lowercase
            if include_numbers:
                characters += string.digits
            if include_symbols:
                characters += string.punctuation

            if not any([include_uppercase, include_lowercase, include_numbers, include_symbols]):
                messagebox.showerror("Error", "Please select at least one character type:(")
                return

            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_display.configure(state="normal")
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, password)
            self.password_display.configure(state="readonly")

        except ValueError as ve:
            messagebox.showerror("Error", str(ve))

# Main function
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
