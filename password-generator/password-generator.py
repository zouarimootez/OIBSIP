import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
import random
import string
import pyperclip
import json
import os
import sqlite3

class PasswordGeneratorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("600x500")
        self.master.resizable(False, False)

        # Initialize database
        self.db_connection = sqlite3.connect("password_database.db")
        self._initialize_database()

        # Load user preferences
        self.preferences = self.load_preferences()

        # Apply saved theme
        self.apply_theme(self.preferences.get("theme", "light"))

        self._setup_ui()

    def _initialize_database(self):
        """Initialize the database and create tables if they don't exist."""
        cursor = self.db_connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                password TEXT UNIQUE,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.db_connection.commit()

    def _setup_ui(self):
        """Setup the user interface."""
        # Main frame
        self.main_frame = ttk.Frame(self.master, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Password Length
        self.label_length = ttk.Label(self.main_frame, text="Password Length:", font=(self.preferences.get("font", "Segoe UI"), 10))
        self.label_length.grid(row=0, column=0, sticky=tk.W, pady=5)

        self.entry_length = ttk.Entry(self.main_frame, font=(self.preferences.get("font", "Segoe UI"), 10))
        self.entry_length.grid(row=0, column=1, pady=5)
        self.entry_length.insert(0, self.preferences.get("default_length", "12"))

        # Character Set Options
        self.check_var_upper = tk.IntVar(value=self.preferences.get("include_upper", 1))
        self.check_upper = ttk.Checkbutton(self.main_frame, text="Include Uppercase (A-Z)", variable=self.check_var_upper)
        self.check_upper.grid(row=1, column=0, columnspan=2, sticky=tk.W, pady=5)

        self.check_var_lower = tk.IntVar(value=self.preferences.get("include_lower", 1))
        self.check_lower = ttk.Checkbutton(self.main_frame, text="Include Lowercase (a-z)", variable=self.check_var_lower)
        self.check_lower.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=5)

        self.check_var_digits = tk.IntVar(value=self.preferences.get("include_digits", 1))
        self.check_digits = ttk.Checkbutton(self.main_frame, text="Include Digits (0-9)", variable=self.check_var_digits)
        self.check_digits.grid(row=3, column=0, columnspan=2, sticky=tk.W, pady=5)

        self.check_var_symbols = tk.IntVar(value=self.preferences.get("include_symbols", 1))
        self.check_symbols = ttk.Checkbutton(self.main_frame, text="Include Symbols (!@#)", variable=self.check_var_symbols)
        self.check_symbols.grid(row=4, column=0, columnspan=2, sticky=tk.W, pady=5)

        # Custom Character Set
        self.btn_custom_chars = ttk.Button(self.main_frame, text="Custom Character Set", command=self.set_custom_chars)
        self.btn_custom_chars.grid(row=5, column=0, columnspan=2, pady=5)

        # Generate Password Button
        self.btn_generate = ttk.Button(self.main_frame, text="Generate Password", command=self.generate_password)
        self.btn_generate.grid(row=6, column=0, columnspan=2, pady=10)

        # Password Display
        self.label_password = ttk.Label(self.main_frame, text="", font=(self.preferences.get("font", "Segoe UI"), 12), wraplength=500)
        self.label_password.grid(row=7, column=0, columnspan=2, pady=10)

        # Copy to Clipboard Button
        self.btn_copy = ttk.Button(self.main_frame, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.btn_copy.grid(row=8, column=0, columnspan=2, pady=5)

        # Save Password Button
        self.btn_save = ttk.Button(self.main_frame, text="Save Password", command=self.save_password)
        self.btn_save.grid(row=9, column=0, columnspan=2, pady=5)

        # Password Strength Indicator
        self.label_strength = ttk.Label(self.main_frame, text="Strength: None", font=(self.preferences.get("font", "Segoe UI"), 10))
        self.label_strength.grid(row=10, column=0, columnspan=2, pady=5)

        # Password History
        self.btn_history = ttk.Button(self.main_frame, text="View Password History", command=self.view_password_history)
        self.btn_history.grid(row=11, column=0, columnspan=2, pady=5)

        # Settings Menu
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        self.settings_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.settings_menu.add_command(label="Change Theme", command=self.change_theme)
        self.settings_menu.add_command(label="Change Font", command=self.change_font)
        self.settings_menu.add_separator()
        self.settings_menu.add_command(label="Save Preferences", command=self.save_preferences)
        self.menu_bar.add_cascade(label="Settings", menu=self.settings_menu)

    def generate_password(self):
        """Generate a password based on user preferences."""
        try:
            length = int(self.entry_length.get())
            if length <= 0:
                raise ValueError("Password length must be a positive integer.")

            character_sets = {
                'upper': string.ascii_uppercase if self.check_var_upper.get() else '',
                'lower': string.ascii_lowercase if self.check_var_lower.get() else '',
                'digits': string.digits if self.check_var_digits.get() else '',
                'symbols': string.punctuation if self.check_var_symbols.get() else '',
                'custom': self.preferences.get("custom_chars", "")
            }

            all_characters = ''.join(character_sets.values())

            if not all_characters:
                raise ValueError("Please select at least one character set.")

            # Generate a unique password
            password = self.generate_unique_password(all_characters, length)
            self.show_password(password)
            self.update_strength_indicator(password)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def generate_unique_password(self, characters, length):
        """Generate a password and ensure it is unique in the database."""
        while True:
            password = ''.join(random.choice(characters) for _ in range(length))
            if not self.password_exists(password):
                break
        return password

    def password_exists(self, password):
        """Check if the password already exists in the database."""
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT id FROM passwords WHERE password = ?", (password,))
        return cursor.fetchone() is not None

    def show_password(self, password):
        """Display the generated password."""
        self.label_password.config(text=password)

    def copy_to_clipboard(self):
        """Copy the generated password to the clipboard."""
        password = self.label_password.cget("text")
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard.")
        else:
            messagebox.showwarning("No Password", "Generate a password first.")

    def save_password(self):
        """Save the generated password to the database."""
        password = self.label_password.cget("text")
        if not password:
            messagebox.showwarning("No Password", "Generate a password first.")
            return

        try:
            cursor = self.db_connection.cursor()
            cursor.execute("INSERT INTO passwords (password) VALUES (?)", (password,))
            self.db_connection.commit()
            messagebox.showinfo("Saved", "Password saved to database.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Password already exists in the database.")

    def update_strength_indicator(self, password):
        """Update the password strength indicator."""
        strength = self.calculate_password_strength(password)
        self.label_strength.config(text=f"Strength: {strength}")

    def calculate_password_strength(self, password):
        """Calculate the strength of the password."""
        length = len(password)
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_lower = any(c in string.ascii_lowercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_symbol = any(c in string.punctuation for c in password)

        score = 0
        if length >= 12:
            score += 2
        elif length >= 8:
            score += 1

        if has_upper:
            score += 1
        if has_lower:
            score += 1
        if has_digit:
            score += 1
        if has_symbol:
            score += 1

        if score >= 5:
            return "Strong"
        elif score >= 3:
            return "Medium"
        else:
            return "Weak"

    def view_password_history(self):
        """Display a history of generated passwords from the database."""
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT password, timestamp FROM passwords ORDER BY timestamp DESC")
        passwords = cursor.fetchall()

        if not passwords:
            messagebox.showinfo("No History", "No passwords have been saved yet.")
            return

        history_window = tk.Toplevel(self.master)
        history_window.title("Password History")
        history_window.geometry("400x300")

        history_text = "\n".join([f"{row[0]} (Generated on: {row[1]})" for row in passwords])
        history_label = ttk.Label(history_window, text=history_text, font=(self.preferences.get("font", "Segoe UI"), 10))
        history_label.pack(pady=10, padx=10)

    def set_custom_chars(self):
        """Allow the user to set a custom character set."""
        custom_chars = simpledialog.askstring("Custom Characters", "Enter custom characters to include:")
        if custom_chars:
            self.preferences["custom_chars"] = custom_chars
            messagebox.showinfo("Success", "Custom character set updated.")

    def change_theme(self):
        """Change the application theme."""
        theme = simpledialog.askstring("Change Theme", "Enter theme (light/dark):")
        if theme in ["light", "dark"]:
            self.preferences["theme"] = theme
            self.apply_theme(theme)
            messagebox.showinfo("Success", f"Theme changed to {theme}.")
        else:
            messagebox.showerror("Error", "Invalid theme. Choose 'light' or 'dark'.")

    def apply_theme(self, theme):
        """Apply the selected theme."""
        if theme == "light":
            self.master.configure(bg="white")
            ttk.Style().configure(".", background="white", foreground="black")
        elif theme == "dark":
            self.master.configure(bg="#2d2d2d")
            ttk.Style().configure(".", background="#2d2d2d", foreground="white")

    def change_font(self):
        """Change the application font."""
        font = simpledialog.askstring("Change Font", "Enter font name (e.g., Arial, Segoe UI):")
        if font:
            self.preferences["font"] = font
            self._setup_ui()  # Rebuild UI with new font
            messagebox.showinfo("Success", f"Font changed to {font}.")

    def save_preferences(self):
        """Save user preferences to a file."""
        with open("preferences.json", "w") as file:
            json.dump(self.preferences, file)
        messagebox.showinfo("Saved", "Preferences saved successfully.")

    def load_preferences(self):
        """Load user preferences from a file."""
        if os.path.exists("preferences.json"):
            with open("preferences.json", "r") as file:
                return json.load(file)
        return {}

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()
