import tkinter as tk
from tkinter import messagebox
import random
import string

# -----------------------------
# Password Generator Function
# -----------------------------
def generate_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0!")
            return

        characters = ""

        if upper_var.get():
            characters += string.ascii_uppercase

        if lower_var.get():
            characters += string.ascii_lowercase

        if digit_var.get():
            characters += string.digits

        if symbol_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showwarning(
                "Selection Error",
                "Please select at least one character type!"
            )
            return

        password = ''.join(random.choice(characters) for _ in range(length))

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")


# -----------------------------
# Copy Password Function
# -----------------------------
def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "Generate a password first!")


# -----------------------------
# GUI Window
# -----------------------------
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x500")
root.resizable(False, False)

# Colors
BG_COLOR = "#E8F5E9"
FRAME_COLOR = "#FFFFFF"
BUTTON_COLOR = "#4CAF50"
TEXT_COLOR = "#1B5E20"

root.configure(bg=BG_COLOR)

# -----------------------------
# Heading
# -----------------------------
title = tk.Label(
    root,
    text="🔐 Password Generator",
    font=("Arial", 20, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)
title.pack(pady=15)

# -----------------------------
# Length Section
# -----------------------------
tk.Label(
    root,
    text="Password Length",
    font=("Arial", 12, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
).pack()

length_entry = tk.Entry(
    root,
    font=("Arial", 12),
    justify="center",
    width=10
)
length_entry.pack(pady=10)
length_entry.insert(0, "12")

# -----------------------------
# Options
# -----------------------------
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

frame = tk.Frame(root, bg=FRAME_COLOR, padx=20, pady=15)
frame.pack(pady=10)

tk.Checkbutton(
    frame,
    text="Uppercase Letters (A-Z)",
    variable=upper_var,
    bg=FRAME_COLOR,
    font=("Arial", 11)
).pack(anchor="w")

tk.Checkbutton(
    frame,
    text="Lowercase Letters (a-z)",
    variable=lower_var,
    bg=FRAME_COLOR,
    font=("Arial", 11)
).pack(anchor="w")

tk.Checkbutton(
    frame,
    text="Numbers (0-9)",
    variable=digit_var,
    bg=FRAME_COLOR,
    font=("Arial", 11)
).pack(anchor="w")

tk.Checkbutton(
    frame,
    text="Symbols (!@#$%)",
    variable=symbol_var,
    bg=FRAME_COLOR,
    font=("Arial", 11)
).pack(anchor="w")

# -----------------------------
# Generate Button
# -----------------------------
generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    bg=BUTTON_COLOR,
    fg="white",
    width=20,
    command=generate_password
)
generate_btn.pack(pady=20)

# -----------------------------
# Password Output
# -----------------------------
password_entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center",
    width=30
)
password_entry.pack(pady=10)

# -----------------------------
# Copy Button
# -----------------------------
copy_btn = tk.Button(
    root,
    text="Copy Password",
    font=("Arial", 12, "bold"),
    bg="#2196F3",
    fg="white",
    width=20,
    command=copy_password
)
copy_btn.pack(pady=10)

# -----------------------------
# Footer
# -----------------------------
footer = tk.Label(
    root,
    text="Secure Password Generator using Python & Tkinter",
    bg=BG_COLOR,
    fg="gray",
    font=("Arial", 9)
)
footer.pack(side="bottom", pady=10)

root.mainloop()