import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv

class DatabaseManager:
    """Handles all database operations."""
    def __init__(self, db_name='bmi_database.db'):
        self.db_name = db_name
        self._initialize_db()

    def _initialize_db(self):
        """Initialize the database and create tables if they don't exist."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS user_data (
                    id INTEGER PRIMARY KEY,
                    weight REAL,
                    height REAL,
                    bmi REAL,
                    category TEXT
                )
            ''')
            conn.commit()

    def save_bmi_data(self, weight, height, bmi, category):
        """Save BMI data to the database."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO user_data (weight, height, bmi, category)
                VALUES (?, ?, ?, ?)
            ''', (weight, height, bmi, category))
            conn.commit()

    def fetch_bmi_history(self):
        """Fetch all BMI data from the database."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT weight, height, bmi, category FROM user_data')
            return cursor.fetchall()

class BMI_Calculator_GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("BMI Calculator")
        self.master.geometry("500x400")
        self.master.resizable(False, False)

        self.db_manager = DatabaseManager()

        self._setup_ui()

    def _setup_ui(self):
        """Setup the user interface."""
        style = ttk.Style()
        style.theme_use('clam')  # Modern theme

        # Main frame
        self.main_frame = ttk.Frame(self.master, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Instructions
        self.label_instructions = ttk.Label(self.main_frame, text="Enter your weight and height below:", font=('Segoe UI', 12))
        self.label_instructions.grid(row=0, column=0, columnspan=2, pady=10)

        # Weight input
        self.label_weight = ttk.Label(self.main_frame, text="Weight (kg):", font=('Segoe UI', 10))
        self.label_weight.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entry_weight = ttk.Entry(self.main_frame, font=('Segoe UI', 10))
        self.entry_weight.grid(row=1, column=1, pady=5)

        # Height input
        self.label_height = ttk.Label(self.main_frame, text="Height (m):", font=('Segoe UI', 10))
        self.label_height.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.entry_height = ttk.Entry(self.main_frame, font=('Segoe UI', 10))
        self.entry_height.grid(row=2, column=1, pady=5)

        # Calculate BMI button
        self.btn_calculate = ttk.Button(self.main_frame, text="Calculate BMI", command=self.calculate_bmi)
        self.btn_calculate.grid(row=3, column=0, columnspan=2, pady=10)

        # View History button
        self.btn_view_history = ttk.Button(self.main_frame, text="View History", command=self.view_history)
        self.btn_view_history.grid(row=4, column=0, columnspan=2, pady=5)

        # Export Data button
        self.btn_export_data = ttk.Button(self.main_frame, text="Export Data", command=self.export_data)
        self.btn_export_data.grid(row=5, column=0, columnspan=2, pady=5)

    def calculate_bmi(self):
        """Calculate BMI and display the result."""
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())

            if weight <= 0 or height <= 0:
                messagebox.showerror("Error", "Weight and height must be positive values.")
                return

            bmi = weight / (height ** 2)
            category = self._classify_bmi(bmi)
            recommendation = self._get_bmi_recommendation(category)

            self.db_manager.save_bmi_data(weight, height, bmi, category)

            result_text = f"Your BMI is: {bmi:.2f}\nCategory: {category}\nRecommendation: {recommendation}"
            messagebox.showinfo("BMI Result", result_text)

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numeric values.")

    def _classify_bmi(self, bmi):
        """Classify BMI into categories."""
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

    def _get_bmi_recommendation(self, category):
        """Provide health recommendations based on BMI category."""
        recommendations = {
            "Underweight": "Consider gaining weight through a balanced diet and exercise.",
            "Normal weight": "Maintain your current weight with a healthy lifestyle.",
            "Overweight": "Consider losing weight through diet and exercise.",
            "Obese": "Seek medical advice for weight management."
        }
        return recommendations.get(category, "No recommendation available.")

    def view_history(self):
        """Display BMI history in a new window."""
        data = self.db_manager.fetch_bmi_history()

        if not data:
            messagebox.showinfo("No Data", "No BMI data available.")
            return

        history_window = tk.Toplevel(self.master)
        history_window.title("BMI History")
        history_window.geometry("600x400")

        # Treeview to display data
        tree = ttk.Treeview(history_window, columns=("Weight", "Height", "BMI", "Category"), show="headings", height=10)
        tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        for col in ["Weight", "Height", "BMI", "Category"]:
            tree.heading(col, text=col)
            tree.column(col, width=120, anchor='center')

        for row_data in data:
            tree.insert("", "end", values=row_data)

        # Analyze BMI Trend button
        btn_analyze_trend = ttk.Button(history_window, text="Analyze BMI Trend", command=self.analyze_bmi_trend)
        btn_analyze_trend.pack(pady=10)

    def analyze_bmi_trend(self):
        """Analyze and plot BMI trend."""
        data = self.db_manager.fetch_bmi_history()

        if not data:
            messagebox.showinfo("No Data", "No BMI data available for analysis.")
            return

        bmi_values = [row[2] for row in data]

        plt.figure(figsize=(8, 6))
        plt.plot(range(1, len(bmi_values) + 1), bmi_values, marker='o', color='#0078D4')
        plt.title("BMI Trend Analysis", fontdict={'fontname': 'Segoe UI', 'fontsize': 12})
        plt.xlabel("Entry Number", fontdict={'fontname': 'Segoe UI', 'fontsize': 10})
        plt.ylabel("BMI", fontdict={'fontname': 'Segoe UI', 'fontsize': 10})
        plt.grid(True)

        trend_window = tk.Toplevel(self.master)
        trend_window.title("BMI Trend Analysis")

        canvas = FigureCanvasTkAgg(plt.gcf(), master=trend_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def export_data(self):
        """Export BMI history to a CSV file."""
        data = self.db_manager.fetch_bmi_history()

        if not data:
            messagebox.showinfo("No Data", "No BMI data available to export.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Weight (kg)", "Height (m)", "BMI", "Category"])
                writer.writerows(data)
            messagebox.showinfo("Export Successful", "BMI data has been exported successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BMI_Calculator_GUI(root)
    root.mainloop()