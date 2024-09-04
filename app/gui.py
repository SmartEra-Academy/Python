import tkinter as tk
from tkinter import messagebox, ttk
from app.data_manager import DataManager

class StudentForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("600x400")
        self.root.configure(bg="#f5f5f5")

        # Menu Bar
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        # Add "Student" menu
        student_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Student", menu=student_menu)
        student_menu.add_command(label="Register", command=self.show_registration_form)
        student_menu.add_command(label="View Students", command=self.show_student_list)

        # Table for student data
        self.table = ttk.Treeview(root, columns=("First Name", "Last Name", "Student ID", "Subject", "Teacher"), show='headings')
        self.table.heading("First Name", text="First Name")
        self.table.heading("Last Name", text="Last Name")
        self.table.heading("Student ID", text="Student ID")
        self.table.heading("Subject", text="Subject")
        self.table.heading("Teacher", text="Teacher")
        self.table.pack(fill=tk.BOTH, expand=True)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(fill=tk.X, pady=10)

        delete_btn = ttk.Button(button_frame, text="Delete Selected", command=self.delete_student)
        delete_btn.pack(side=tk.LEFT, padx=10)
        edit_btn = ttk.Button(button_frame, text="Edit Selected", command=self.edit_student)
        edit_btn.pack(side=tk.LEFT, padx=10)

        # Load initial data
        self.show_student_list()

    def show_registration_form(self):
        reg_form = tk.Toplevel(self.root)
        reg_form.title("Register Student")
        reg_form.geometry("400x300")

        labels = ["First Name", "Last Name", "Student ID", "Subject", "Teacher"]
        self.entries = {}

        for i, label_text in enumerate(labels):
            label = ttk.Label(reg_form, text=label_text)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="W")

            entry = ttk.Entry(reg_form, width=30)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[label_text] = entry

        submit_btn = ttk.Button(reg_form, text="Submit", command=self.submit_student)
        submit_btn.grid(row=5, column=1, pady=10)

    def submit_student(self):
        student_data = {key: entry.get() for key, entry in self.entries.items()}
        students = DataManager.load_data()
        students.append(student_data)
        DataManager.save_data(students)
        messagebox.showinfo("Success", "Student registered successfully!")
        self.clear_entries()
        self.show_student_list()

    def show_student_list(self):
        self.table.delete(*self.table.get_children())
        students = DataManager.load_data()

        for student in students:
            self.table.insert('', 'end', values=(student['First Name'], student['Last Name'], student['Student ID'], student['Subject'], student['Teacher']))

    def delete_student(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a student to delete.")
            return

        student_id = self.table.item(selected_item[0])['values'][2]
        DataManager.delete_student(student_id)
        self.show_student_list()

    def edit_student(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a student to edit.")
            return

        student_id = self.table.item(selected_item[0])['values'][2]
        students = DataManager.load_data()
        student_data = next((student for student in students if student['Student ID'] == student_id), None)

        if not student_data:
            messagebox.showerror("Error", "Student data not found.")
            return

        edit_form = tk.Toplevel(self.root)
        edit_form.title("Edit Student")
        edit_form.geometry("400x300")

        labels = ["First Name", "Last Name", "Student ID", "Subject", "Teacher"]
        self.entries = {}

        for i, label_text in enumerate(labels):
            label = ttk.Label(edit_form, text=label_text)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="W")

            entry = ttk.Entry(edit_form, width=30)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entry.insert(0, student_data[label_text])
            self.entries[label_text] = entry

        submit_btn = ttk.Button(edit_form, text="Update", command=lambda: self.update_student(student_id))
        submit_btn.grid(row=5, column=1, pady=10)

    def update_student(self, student_id):
        updated_data = {key: entry.get() for key, entry in self.entries.items()}
        updated_data['Student ID'] = student_id
        DataManager.update_student(updated_data)
        messagebox.showinfo("Success", "Student data updated successfully!")
        self.show_student_list()

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
