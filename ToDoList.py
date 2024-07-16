import tkinter as tk
from tkinter import messagebox


class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List App")

        # Task list
        self.tasks = []

        # Create UI elements
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_task_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=60, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        complete_task_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        complete_task_button.grid(row=2, column=0, padx=10, pady=10)

        remove_task_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        remove_task_button.grid(row=2, column=1, padx=10, pady=10)

        exit_task_button = tk.Button(root, text="Exit", command=self.exit_task)
        exit_task_button.grid(row=3, column=1, padx=20, pady=10)


    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning!!", "Please enter a task!")


    def complete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            completed_task = self.task_listbox.get(task_index)
            self.task_listbox.delete(task_index)
            self.tasks.remove(completed_task)
            messagebox.showinfo("Task Completed", f"Completed: {completed_task}")
        except IndexError:
            messagebox.showwarning("Warning!!", "Please select a task to complete!")


    def remove_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            removed_task = self.task_listbox.get(task_index)
            self.task_listbox.delete(task_index)
            self.tasks.remove(removed_task)
            messagebox.showinfo("Task Removed", f"Removed: {removed_task}")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove!")


    def exit_task(self):
         self.root.destroy()


# Main function
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
