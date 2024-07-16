import tkinter as tk
from tkinter import messagebox


class ContactBook(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contact Book")
        self.geometry("400x400")

        # Initialize contacts list
        self.contacts = []

        # Labels
        tk.Label(self, text="Name:").pack(pady=5)
        self.name_entry = tk.Entry(self, width=30)
        self.name_entry.pack()
        tk.Label(self, text="Phone:").pack(pady=5)
        self.phone_entry = tk.Entry(self, width=30)
        self.phone_entry.pack()

        # Buttons
        tk.Button(self, text="Add Contact", command=self.add_contact).pack(pady=20)
        tk.Button(self, text="View Contacts", command=self.view_contacts).pack(pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        if name and phone:
            self.contacts.append((name, phone))
            messagebox.showinfo("Success", "Contact added successfully!")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both name and phone number.")

    def view_contacts(self):
        if self.contacts:
            view_window = tk.Toplevel(self)
            view_window.title("Contacts")
            view_window.geometry("400x400")

            tk.Label(view_window, text="Contacts List", font=("TimesNewRoman", 16)).pack(pady=10)

            for contact in self.contacts:
                tk.Label(view_window, text=f"Name: {contact[0]}, Phone: {contact[1]}").pack(pady=5)
        else:
            messagebox.showinfo("Empty", "No contacts found.")


if __name__ == "__main__":
    app = ContactBook()
    app.mainloop()
