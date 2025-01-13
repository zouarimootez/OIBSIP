import tkinter as tk
from tkinter import ttk

def apply_theme(master, theme):
    """Apply the selected theme."""
    if theme == "light":
        master.configure(bg="white")
        ttk.Style().configure(".", background="white", foreground="black")
    elif theme == "dark":
        master.configure(bg="#2d2d2d")
        ttk.Style().configure(".", background="#2d2d2d", foreground="white")