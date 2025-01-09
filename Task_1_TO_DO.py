import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("600x500")  
        self.root.resizable(False, False)

       
        self.create_gradient_background()

        
        self.title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 18, "bold"), bg="#87CEEB", fg="white")
        self.title_label.pack(pady=10)

        
        self.task_input = tk.Entry(root, font=("Helvetica", 12), width=50, bd=2, relief=tk.GROOVE)
        self.task_input.pack(pady=10)

        
        button_frame = tk.Frame(root, bg="#87CEEB")
        button_frame.pack(pady=10)

        
        self.add_button = tk.Button(button_frame, text="Add Task", bg="#007FFF", fg="white", width=12, command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=10)

        self.update_button = tk.Button(button_frame, text="Update Task", bg="#6495ED", fg="white", width=12, command=self.update_task)
        self.update_button.grid(row=0, column=1, padx=10)

        self.delete_button = tk.Button(button_frame, text="Delete Task", bg="#FF6347", fg="white", width=12, command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=10)

        self.complete_button = tk.Button(button_frame, text="Mark Completed", bg="#32CD32", fg="white", width=12, command=self.mark_completed)
        self.complete_button.grid(row=0, column=3, padx=10)

        
        self.task_label = tk.Label(root, text="Tasks", font=("Helvetica", 14, "bold"), bg="#87CEEB", fg="white")
        self.task_label.pack(pady=10)

        self.task_listbox = tk.Listbox(root, font=("Helvetica", 12), width=60, height=12, bd=2, relief=tk.GROOVE, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=20, side=tk.BOTTOM)

    def create_gradient_background(self):
        """Creates a blue gradient background."""
        canvas = tk.Canvas(self.root, width=600, height=500, highlightthickness=0)
        canvas.place(x=0, y=0)

        for i in range(500):
            color = f"#{int(135 + i / 5):02x}CEEB"
            canvas.create_line(0, i, 600, i, fill=color)

    def add_task(self):
        """Add a task to the list."""
        task = self.task_input.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")

    def update_task(self):
        """Update the selected task."""
        selected_index = self.task_listbox.curselection()
        if selected_index:
            new_task = simpledialog.askstring("Update Task", "Enter the updated task:")
            if new_task:
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, new_task)
            else:
                messagebox.showwarning("Input Error", "Task cannot be empty!")
        else:
            messagebox.showwarning("Selection Error", "No task selected!")

    def delete_task(self):
        """Delete the selected task."""
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)
        else:
            messagebox.showwarning("Selection Error", "No task selected!")

    def mark_completed(self):
        """Mark the selected task as completed."""
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.task_listbox.get(selected_index)
            if "[Completed]" not in task:
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, f"{task} [Completed]")
            else:
                messagebox.showinfo("Task Completed", "Task is already marked as completed!")
        else:
            messagebox.showwarning("Selection Error", "No task selected!")

# Main Function
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
