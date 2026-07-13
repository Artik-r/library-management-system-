import tkinter as tk

from library_system import LibraryManagementSystem


def main():
    root = tk.Tk()
    LibraryManagementSystem(root)
    root.mainloop()


if __name__ == "__main__":
    main()
    