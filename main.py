import sqlite3
import tkinter as tk
from struct import pack
from textwrap import fill
from tkinter.ttk import Entry
from turtle import bgcolor, color, width
from venv import create



class MainWindow:
    def __init__(self, *args, **kwargs):
        # the main window to be create

        self.w = tk.Canvas(master, width=750, height=750)
        self.w.configure(bg='white')
        self.entry = tk.StringVar()
        self.init = True
        self.new_name = ""
        self.new_w = tk.Canvas(master, width = 750, height = 60)

master = tk.Tk()
master.title("3d Filament inventory App")
three_Print = MainWindow(master)
master.mainloop()




