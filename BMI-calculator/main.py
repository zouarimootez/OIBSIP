import tkinter as tk
from gui.bmi_calculator_gui import BMI_Calculator_GUI

if __name__ == "__main__":
    root = tk.Tk()
    app = BMI_Calculator_GUI(root)
    root.mainloop()