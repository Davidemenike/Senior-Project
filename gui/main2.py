from distutils.cmd import Command
from cgitb import text
from fileinput import close
from msilib.schema import ListBox
from os import kill
import Inventory_insert as Inserting
import Inventory_update as Update


from struct import pack
from textwrap import fill
import tkinter as tk
from tkinter.ttk import Entry
from turtle import bgcolor, color, width
from venv import create



import pymysql
import config as cf
import sqlite3


# master = tk.Tk()
# master.title("3D Print Inventory App")
# w = tk.Canvas(master, width=550, height=600)
# w.configure(bg='green2')

# first_name = tk.StringVar()
# last_name = tk.StringVar()
# phoneNumber = tk.IntVar()
# Birthday = tk.StringVar()
# entry = tk.StringVar()


# w.pack()
# master.mainloop()


class window:
    def __init__(self,  *args, **kwargs):
        # tk.Tk.__init__(self, *args, **kwargs)
        # # Adding a title to the window
        # self.wm_title
        self.w = tk.Canvas(master, width = 1200, height= 1200)
        self.w.configure(bg='green')


        self.container = tk.Canvas(master, height = 1200, width = 1200, bg="green2")
       
    
        self.container.create_text(290,190, text="BELHAVEN \n 3D \n PRINTING", fill = "white", font = "Helvetica 50 bold")
        # main_text = tk.Text(container, height = 5, width = 32).place(x = 14, y = 100)
        # main_text
        # Text(container, text= "BELHAVEN \n 3D \n PRINTING", height = 5, width = 32).place(x = 14, y = 100)
        
        button = tk.Button(self.container, width = '20', text = 'Inventory', bg = "#008037", height = 2, command = self.inventory ).place(x = 172, y = 455)
        button2 = tk.Button(self.container, width = '20', text = 'Close', bg = "#008037", height = 2).place(x = 672, y = 455)

        self.container.pack()
        self.w.pack()


    

    def inventory(self):
        new = tk.Toplevel(self.w)
        new.geometry("1200x1200")
        new.title("Inventory")
        new.configure(bg = "green")

        addFilament_sect = tk.Canvas(new, width = 1200, height = 60, background="blue" )
        addFilament_button = tk.Button(new, text = "Add FIlament", activebackground="red",
                                       activeforeground="brown", height=1, command = self.newfilament).place(x = 1100, y = 20)


        addFilament_sect.pack()

    
    def newfilament(self):
        new = tk.Toplevel(self.w)
        new.geometry("500x500")
        new.title("Add Filament")


        newContact_sect = tk.Canvas(
            new, width="500", background="#7ED957", height=100)
        newContact_sect.create_text(
            175, 60, text="ADD FILAMENT", fill="white", font="Helvetica 22 bold")
        
        newContact_sect2 = tk.Canvas(
            new, width="500", background="white", height=400)
        

        newContact_sect2.create_text(
            65, 40, text="Material", fill="grey", font="Helvetica 15 bold")
        material_entry = tk.Entry(new, width="20", background="white", foreground="black",
                                   highlightbackground="grey", highlightcolor='grey', highlightthickness=4)
        material_entry.place(x=14, y=160)

        newContact_sect2.create_text(
            260, 40, text='Color', fill="grey", font="Helvetica 15 bold")
        color_entry = tk.Entry(new, width='20', background='white', foreground="black",
                                  highlightcolor="grey", highlightbackground='grey', highlightthickness=4)
        color_entry.place(x=200, y=160)


        newContact_sect2.create_text(
            65, 100, text="Addetive", fill='grey', font='Helvetica 15 bold')
        addetive_entry = tk.Entry(new, background='white', foreground="black", highlightcolor="grey",
                                     highlightbackground='grey', highlightthickness=4)
        addetive_entry.place(x=14, y=230)


        newContact_sect2.create_text(
            260, 100, text="Brand", fill="grey", font="Helvetica 15 bold")
        brand_entry = tk.Entry(new, background='white', foreground="black", highlightcolor="grey",
                                  highlightbackground='grey', highlightthickness=4)
        brand_entry.place(x=200, y=230)

        newContact_sect2.create_text(
            65, 169, text="remaining", fill="grey", font="Helvetica 15 bold")
        remaining_entry = tk.Entry(new, width="20", background="white", foreground="black",
                                   highlightbackground="grey", highlightcolor='grey', highlightthickness=4)
        remaining_entry.place(x=14, y=290)

        print("brand is" + str(brand_entry))
        print("color is " + str(color_entry))
        print("addetive is " + str(addetive_entry))
        print("material is" + str(material_entry))

        submit_button= tk.Button(new, width = '20', text = "Enter", bg = '#008037', height = 2, command = lambda: [Inserting.insertdata(material_entry,color_entry,addetive_entry,brand_entry,remaining_entry ),new.destroy(), duty.refresh()])
        submit_button.place(x = 14, y = 355)
        
        




 





        newContact_sect.pack()
        newContact_sect2.pack()


    def refresh(self):
        self.w.destroy()
        self.container.destroy()
        duty.__init__()







        


    





master = tk.Tk()
master.title("3D Print Inventory App")
duty = window(master)
duty.__init__()
master.mainloop()