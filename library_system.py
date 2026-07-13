import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date, timedelta

from books import books


class LibraryManagementSystem:
    """Library Management System GUI."""

    def __init__(self, root):
        """Initialize the application."""

        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800")
        self.root.resizable(False, False)

        # ======================================================
        # Student Information Variables
        # ======================================================

        self.student_name = tk.StringVar()
        self.class_name = tk.StringVar()
        self.section = tk.StringVar()
        self.roll_no = tk.StringVar()
        self.address = tk.StringVar()
        self.mobile_no = tk.StringVar()

        # ======================================================
        # Book Information Variables
        # ======================================================

        self.book_title = tk.StringVar()
        self.author_name = tk.StringVar()
        self.date_borrowed = tk.StringVar()
        self.date_due = tk.StringVar()
        self.late_fine = tk.StringVar()
        self.book_price = tk.StringVar()

        # ======================================================
        # Build User Interface
        # ======================================================

        self.create_header()
        self.create_main_frame()

    # ==========================================================
    # Header
    # ==========================================================

    def create_header(self):
        """Create application heading."""

        title = tk.Label(
            self.root,
            text="LIBRARY MANAGEMENT SYSTEM",
            font=("Times New Roman", 40, "bold"),
            bg="powder blue",
            fg="green",
            bd=15,
            relief=tk.RIDGE
        )

        title.pack(fill=tk.X)

    # ==========================================================
    # Main Frame
    # ==========================================================

    def create_main_frame(self):
        """Create main application frame."""

        self.main_frame = tk.Frame(
            self.root,
            bd=12,
            relief=tk.RIDGE,
            bg="powder blue"
        )

        self.main_frame.place(
            x=10,
            y=120,
            width=1530,
            height=600
        )

        # Create all sections
        self.create_left_frame()
        self.create_right_frame()
    # ==========================================================
    # Left Frame
    # ==========================================================

    def create_left_frame(self):
        """Create the left section containing student information."""

        self.left_frame = tk.LabelFrame(
            self.main_frame,
            text="Student Information",
            font=("Times New Roman", 12, "bold"),
            bg="powder blue",
            fg="black",
            bd=8,
            relief=tk.RIDGE
        )

        self.left_frame.place(
            x=10,
            y=5,
            width=500,
            height=580
        )

        # ------------------------------------------------------
        # Labels
        # ------------------------------------------------------

        labels = [
            "Student Name",
            "Class",
            "Section",
            "Roll Number",
            "Address",
            "Mobile Number"
        ]

        for index, text in enumerate(labels):
            tk.Label(
                self.left_frame,
                text=text,
                font=("Arial", 12, "bold"),
                bg="powder blue"
            ).grid(
                row=index,
                column=0,
                padx=10,
                pady=10,
                sticky="w"
            )

        # ------------------------------------------------------
        # Entry Boxes
        # ------------------------------------------------------

        tk.Entry(
            self.left_frame,
            textvariable=self.student_name,
            font=("Arial", 12),
            width=28
        ).grid(row=0, column=1, padx=10, pady=10)

        tk.Entry(
            self.left_frame,
            textvariable=self.class_name,
            font=("Arial", 12),
            width=28
        ).grid(row=1, column=1, padx=10, pady=10)

        tk.Entry(
            self.left_frame,
            textvariable=self.section,
            font=("Arial", 12),
            width=28
        ).grid(row=2, column=1, padx=10, pady=10)

        tk.Entry(
            self.left_frame,
            textvariable=self.roll_no,
            font=("Arial", 12),
            width=28
        ).grid(row=3, column=1, padx=10, pady=10)

        tk.Entry(
            self.left_frame,
            textvariable=self.address,
            font=("Arial", 12),
            width=28
        ).grid(row=4, column=1, padx=10, pady=10)

        tk.Entry(
            self.left_frame,
            textvariable=self.mobile_no,
            font=("Arial", 12),
            width=28
        ).grid(row=5, column=1, padx=10, pady=10)

        # ------------------------------------------------------
        # Book Details Section
        # ------------------------------------------------------

        self.book_frame = tk.LabelFrame(
            self.left_frame,
            text="Book Details",
            font=("Times New Roman", 12, "bold"),
            bg="powder blue",
            fg="black",
            bd=5,
            relief=tk.RIDGE
        )

        self.book_frame.place(
            x=10,
            y=300,
            width=460,
            height=250
        )        


        self.book_frame.place(
    x=10,
    y=300,
    width=460,
    height=250
)
        
        # ------------------------------------------------------
        # Book Labels
        # ------------------------------------------------------

        book_labels = [
            "Book Title",
            "Author",
            "Date Borrowed",
            "Due Date",
            "Late Fine",
            "Book Price"
        ]

        for index, text in enumerate(book_labels):
            tk.Label(
                self.book_frame,
                text=text,
                font=("Arial", 11, "bold"),
                bg="powder blue"
            ).grid(
                row=index,
                column=0,
                padx=10,
                pady=8,
                sticky="w"
            )

        # ------------------------------------------------------
        # Book Entry Boxes
        # ------------------------------------------------------

        self.book_title_entry = tk.Entry(
            self.book_frame,
            textvariable=self.book_title,
            font=("Arial", 11),
            width=25
        )
        self.book_title_entry.grid(row=0, column=1, padx=10, pady=8)

        self.author_entry = tk.Entry(
            self.book_frame,
            textvariable=self.author_name,
            font=("Arial", 11),
            width=25
        )
        self.author_entry.grid(row=1, column=1, padx=10, pady=8)

        self.date_borrowed_entry = tk.Entry(
            self.book_frame,
            textvariable=self.date_borrowed,
            font=("Arial", 11),
            width=25
        )
        self.date_borrowed_entry.grid(row=2, column=1, padx=10, pady=8)

        self.date_due_entry = tk.Entry(
            self.book_frame,
            textvariable=self.date_due,
            font=("Arial", 11),
            width=25
        )
        self.date_due_entry.grid(row=3, column=1, padx=10, pady=8)

        self.late_fine_entry = tk.Entry(
            self.book_frame,
            textvariable=self.late_fine,
            font=("Arial", 11),
            width=25
        )
        self.late_fine_entry.grid(row=4, column=1, padx=10, pady=8)

        self.book_price_entry = tk.Entry(
            self.book_frame,
            textvariable=self.book_price,
            font=("Arial", 11),
            width=25
        )
        self.book_price_entry.grid(row=5, column=1, padx=10, pady=8)


    # ==========================================================
    # Right Frame
    # ==========================================================

    def create_right_frame(self):
        """Create the right section containing the book list."""

        self.right_frame = tk.LabelFrame(
            self.main_frame,
            text="Available Books",
            font=("Times New Roman", 12, "bold"),
            bg="powder blue",
            fg="black",
            bd=8,
            relief=tk.RIDGE
        )

        self.right_frame.place(
            x=520,
            y=5,
            width=990,
            height=580
        )

        self.create_book_list()


    # ==========================================================
    # Book Selection
    # ==========================================================

    def select_book(self, event):
        """Display book details after selection."""

        selection = self.book_list.curselection()

        if not selection:
            return

        selected_book = self.book_list.get(selection[0])

        self.book_title.set(selected_book)

        self.author_name.set(
            books[selected_book]["author"]
        )

        self.book_price.set(
            books[selected_book]["price"]
        )

        self.late_fine.set(
            books[selected_book]["fine"]
        )

        today = date.today()

        self.date_borrowed.set(
            today.strftime("%d/%m/%Y")
        )

        due_date = today + timedelta(days=14)

        self.date_due.set(
            due_date.strftime("%d/%m/%Y")
        )
        self.create_book_list()
        self.create_receipt_frame() 
        self.create_book_list()
        self.create_receipt_frame()       

    # ==========================================================
    # Receipt Frame
    # ==========================================================

    def create_receipt_frame(self):
        """Create receipt display area."""

        self.receipt_frame = tk.LabelFrame(
            self.right_frame,
            text="Book Issue Receipt",
            font=("Times New Roman", 12, "bold"),
            bg="powder blue",
            fg="black",
            bd=5,
            relief=tk.RIDGE
        )

        self.receipt_frame.place(
            x=420,
            y=10,
            width=540,
            height=540
        )

        receipt_scroll = tk.Scrollbar(
            self.receipt_frame,
            orient=tk.VERTICAL
        )

        self.receipt_text = tk.Text(
            self.receipt_frame,
            width=58,
            height=30,
            font=("Consolas", 11),
            yscrollcommand=receipt_scroll.set,
            wrap=tk.WORD
        )

        receipt_scroll.config(
            command=self.receipt_text.yview
        )

        receipt_scroll.pack(
            side=tk.RIGHT,
            fill=tk.Y
        )

        self.receipt_text.pack(
            fill=tk.BOTH,
            expand=True
        )


    # ==========================================================
    # Generate Receipt
    # ==========================================================

    def generate_receipt(self):
        """Generate borrowing receipt."""

        self.receipt_text.delete(
            "1.0",
            tk.END
        )

        self.receipt_text.insert(
            tk.END,
            "=" * 45 + "\n"
        )

        self.receipt_text.insert(
            tk.END,
            "        LIBRARY RECEIPT\n"
        )

        self.receipt_text.insert(
            tk.END,
            "=" * 45 + "\n\n"
        )

        self.receipt_text.insert(
            tk.END,
            f"Student Name : {self.student_name.get()}\n"
        )

        self.receipt_text.insert(
            tk.END,
            f"Class        : {self.class_name.get()}\n"
        )

        self.receipt_text.insert(
            tk.END,
            f"Section      : {self.section.get()}\n"
        )

        self.receipt_text.insert(
            tk.END,
            f"Roll No      : {self.roll_no.get()}\n"
        )

        self.receipt_text.insert(
            tk.END,
            f"Mobile       : {self.mobile_no.get()}\n\n"
        )

        self.receipt_text.insert(
            tk.END,
            "-" * 45 + "\n"
        )

        self.receipt_text.insert(
            tk.END,
            f"Book         : {self.book_title.get()}\n"
        )

        self.receipt_text.insert(
            tk.END,
            f"Author       : {self.author_name.get()}\n"
        )

        self.receipt_text.insert(
            tk.END,
            f"Issue Date   : {self.date_borrowed.get()}\n"
        )

        self.receipt_text.insert(
            tk.END,
            f"Due Date     : {self.date_due.get()}\n"
        )

        self.receipt_text.insert(
            tk.END,
            f"Late Fine    : {self.late_fine.get()}\n"
        )

        self.receipt_text.insert(
            tk.END,
            f"Book Price   : {self.book_price.get()}\n"
        )

        self.receipt_text.insert(
            tk.END,
            "\n" + "=" * 45 + "\n"
        )

        self.receipt_text.insert(
            tk.END,
            "Thank you for using our Library.\n"
        )

        self.receipt_text.insert(
            tk.END,
            "=" * 45
        )

    # ==========================================================
    # Button Frame
    # ==========================================================

    def create_button_frame(self):
        """Create all action buttons."""

        self.button_frame = tk.Frame(
            self.root,
            bd=10,
            relief=tk.RIDGE,
            bg="powder blue"
        )

        self.button_frame.place(
            x=10,
            y=730,
            width=1530,
            height=60
        )

        # ------------------------------------------------------
        # Issue Book Button
        # ------------------------------------------------------

        tk.Button(
            self.button_frame,
            text="Issue Book",
            font=("Arial", 12, "bold"),
            bg="green",
            fg="white",
            width=18,
            cursor="hand2",
            command=self.issue_book
        ).grid(
            row=0,
            column=0,
            padx=15,
            pady=5
        )

        # ------------------------------------------------------
        # Return Book Button
        # ------------------------------------------------------

        tk.Button(
            self.button_frame,
            text="Return Book",
            font=("Arial", 12, "bold"),
            bg="royal blue",
            fg="white",
            width=18,
            cursor="hand2",
            command=self.return_book
        ).grid(
            row=0,
            column=1,
            padx=15
        )

        # ------------------------------------------------------
        # Reset Button
        # ------------------------------------------------------

        tk.Button(
            self.button_frame,
            text="Reset",
            font=("Arial", 12, "bold"),
            bg="orange",
            fg="black",
            width=18,
            cursor="hand2",
            command=self.reset_fields
        ).grid(
            row=0,
            column=2,
            padx=15
        )

        # ------------------------------------------------------
        # Exit Button
        # ------------------------------------------------------

        tk.Button(
            self.button_frame,
            text="Exit",
            font=("Arial", 12, "bold"),
            bg="red",
            fg="white",
            width=18,
            cursor="hand2",
            command=self.exit_application
        ).grid(
            row=0,
            column=3,
            padx=15
        )

    # ==========================================================
    # Temporary Functions
    # ==========================================================

    def issue_book(self):
        pass

    def return_book(self):
        pass

    def reset_fields(self):
        pass

    def exit_application(self):
        self.root.destroy()

    # ==========================================================
    # Issue Book
    # ==========================================================

    def issue_book(self):
        """Issue a book after validating all details."""

        # -------------------------
        # Validation
        # -------------------------

        if self.student_name.get().strip() == "":
            messagebox.showerror(
                "Missing Information",
                "Please enter the student's name."
            )
            return

        if self.class_name.get().strip() == "":
            messagebox.showerror(
                "Missing Information",
                "Please enter the class."
            )
            return

        if self.section.get().strip() == "":
            messagebox.showerror(
                "Missing Information",
                "Please enter the section."
            )
            return

        if self.roll_no.get().strip() == "":
            messagebox.showerror(
                "Missing Information",
                "Please enter the roll number."
            )
            return

        if self.mobile_no.get().strip() == "":
            messagebox.showerror(
                "Missing Information",
                "Please enter the mobile number."
            )
            return

        if self.book_title.get().strip() == "":
            messagebox.showerror(
                "No Book Selected",
                "Please select a book first."
            )
            return

        # -------------------------
        # Generate Receipt
        # -------------------------

        self.generate_receipt()

        messagebox.showinfo(
            "Success",
            f"'{self.book_title.get()}' has been issued successfully!"
        )

    # ==========================================================
    # Return Book
    # ==========================================================

    def return_book(self):
        """Return the currently issued book."""

        if self.book_title.get().strip() == "":
            messagebox.showwarning(
                "No Book Issued",
                "There is no issued book to return."
            )
            return

        confirm = messagebox.askyesno(
            "Return Book",
            f"Are you sure you want to return\n'{self.book_title.get()}'?"
        )

        if not confirm:
            return

        returned_book = self.book_title.get()

        self.book_title.set("")
        self.author_name.set("")
        self.date_borrowed.set("")
        self.date_due.set("")
        self.late_fine.set("")
        self.book_price.set("")

        self.receipt_text.delete(
            "1.0",
            tk.END
        )

        messagebox.showinfo(
            "Book Returned",
            f"'{returned_book}' has been returned successfully."
        )


    # ==========================================================
    # Reset All Fields
    # ==========================================================

    def reset_fields(self):
        """Clear all student details, book details and receipt."""

        confirm = messagebox.askyesno(
            "Reset",
            "Are you sure you want to clear all information?"
        )

        if not confirm:
            return

        # ------------------------------------------------------
        # Student Information
        # ------------------------------------------------------

        self.student_name.set("")
        self.class_name.set("")
        self.section.set("")
        self.roll_no.set("")
        self.address.set("")
        self.mobile_no.set("")

        # ------------------------------------------------------
        # Book Information
        # ------------------------------------------------------

        self.book_title.set("")
        self.author_name.set("")
        self.date_borrowed.set("")
        self.date_due.set("")
        self.late_fine.set("")
        self.book_price.set("")

        # ------------------------------------------------------
        # Clear Receipt
        # ------------------------------------------------------

        self.receipt_text.delete(
            "1.0",
            tk.END
        )

        # ------------------------------------------------------
        # Clear Book Selection
        # ------------------------------------------------------

        self.book_list.selection_clear(
            0,
            tk.END
        )

        messagebox.showinfo(
            "Reset Successful",
            "All information has been cleared."
        )

    # ==========================================================
    # Exit Application
    # ==========================================================

    def exit_application(self):
        """Close the application."""

        confirm = messagebox.askyesno(
            "Exit Application",
            "Are you sure you want to exit?"
        )

        if confirm:
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()

