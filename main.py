# Snap Ahoy - Main Application
#
# This is the main entry point for the Snap Ahoy application.
#
import tkinter as tk

def main():
    """Main function for the Snap Ahoy application."""
    root = tk.Tk()
    root.title("Snap Ahoy")
    root.geometry("800x600")

    label = tk.Label(root, text="Hello, Snap Ahoy!", font=("Helvetica", 24))
    label.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
