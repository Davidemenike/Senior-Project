from distutils.cmd import Command
from cgitb import text
from fileinput import close
from msilib.schema import ListBox
from os import kill
import Inventory_insert as Inserting
import Inventory_update as Update
import inventory_delete as Delete
import inventory_read as Read


from struct import pack
from textwrap import fill
from tkinter import *
import tkinter as tk
from tkinter import ttk
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

        
        # new3 = tk.Tk()
        # self.new2 = tk.Canvas(master, width = 160, height = 160)
        # self.new2.pack()
        
        
        
        self.container.pack()
        self.w.pack()


    

    def inventory(self):
        new = tk.Toplevel(self.w)
        new.geometry("1200x1200")
        new.title("Inventory")
        new.configure(bg = "green")

        addFilament_sect = tk.Canvas(new, width = 1200, height = 60, background="blue" )
        addFilament_button = tk.Button(new, text = "Add Filament", activebackground="red",
                                       activeforeground="brown", height=1, command = self.newfilament).place(x = 899, y = 20)
        editFilament_button = tk.Button(new, text = "Edit Filament", activebackground="red",
                                       activeforeground="brown", height=1, command = self.free_window).place(x = 999, y = 20)
        
        deleteFilament_button = tk.Button(new, text = "Delete Filament", activebackground="red",
                                       activeforeground="brown", height=1, command=self.free_window2).place(x = 1100, y = 20)
        
        refreshFilament_button = tk.Button(new, text = "Refresh", activebackground="red",
                                       activeforeground="brown", height=1, command= "").place(x = 100, y = 20)
        
        # Inserting.querydata()
        
        conn = pymysql.connect(host = cf.host, user = cf.user,
                           password = cf.password, db = cf.database)
        curr = conn.cursor()
        curr.execute("SELECT * from filament")
        rows = curr.fetchall()
        
        style = ttk.Style()
        style.configure("Treeview",
                        background = "grey",
                        foreground = "blue",
                        rowheight = 25,
                        fieldbackground = "silver")
        
        style.map('Treeview',
                                    background =[('selected', 'green')])
        # columns = ("Material", "Color", "Addetive", "Brand", "Remaining")
        tree = ttk.Treeview(addFilament_sect, height = 50, column = ("ID", "Material", "Color", "Addetive", "Brand", "Remaining"), show = 'headings')
       
        tree.heading("#1", text = "ID" )
        tree.heading("#2", text = "Material" )
        tree.heading("#3", text = "Color" )
        tree.heading("#4", text = "Addetive" )
        tree.heading("#5", text = "Brand" )
        tree.heading("#6", text = "Remaining" )
        # tree.insert("", tk.END, value = rows[0])
        # print(len(rows))
        for i in range(len(rows)):
            # print(rows[i])
            tree.insert("", tk.END, values= rows[i])
        conn.close()
        tree.pack(pady=50)
        addFilament_sect.pack()

    def free_window(self):
        new = tk.Toplevel(self.w)
        new.geometry("500x500")
        new.title("Edit Filament")
        sb = Scrollbar(new)
        sb.pack(side = RIGHT, fill = Y)
        newContact_sect = tk.Canvas(
            new, width="500", background="blue", height=500, yscrollcommand=sb.set)
        
        sb.config(command=newContact_sect.yview)
        

        # scrollbar = ttk.Scrollbar(newContact_sect, orient = 'vertical', command=newContact_sect.yview)
        
        def read():
            # print("update")
            filament_name = []
            filament_color = []
            filament_addetive = []
            filament_brand = []
            filament_remaining = []
            filament_ID = []

            i = 0
            index = 0
            filament_name, filament_color, filament_addetive, filament_brand, filament_remaining, filament_ID = Read.ReadData()
            for names in filament_name:
                # print(names)
                F_color = filament_color[index]
                F_name =  filament_name[index]
                F_addetive = filament_addetive[index]
                F_brand = filament_brand[index]
                F_remaining = filament_remaining[index]
                ID = filament_ID[index]
                

                filament_name[index] = tk.Button(newContact_sect, text=names,activebackground="green",
                                            background="red", height = 1, command=lambda color = F_color,material = F_name, addetive = F_addetive,brand = F_brand, remaining = F_remaining, ID = ID: [self.edit_filament(material,color,addetive, brand, remaining,ID)] )
                filament_name[index].place(x=20, y=40+i)
                i += 40
                index += 1
                
                
            

        
       
        
        confirm_button = tk.Button(newContact_sect, width = '20', text = 'Inventory', bg = "#008037", height = 2, command = read).place(x = 172, y = 455)
        
        
            
        
        
        newContact_sect.pack()
        


    
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

        submit_button= tk.Button(new, width = '20', text = "Enter", bg = '#008037', height = 2, command = lambda: [Inserting.insertdata(material_entry,color_entry,addetive_entry,brand_entry,remaining_entry),new.destroy()])
        submit_button.place(x = 14, y = 355)
        

        newContact_sect.pack()
        newContact_sect2.pack()

    #This window is called when the delete button is pressed
    def free_window2(self):
        new = tk.Toplevel(self.w)
        new.geometry("500x500")
        new.title("Delete Filament")
        sb = Scrollbar(new)
        sb.pack(side = RIGHT, fill = Y)
        newContact_sect = tk.Canvas(
            new, width="500", background="blue", height=500, yscrollcommand=sb.set)
        
        sb.config(command=newContact_sect.yview)
        

        # scrollbar = ttk.Scrollbar(newContact_sect, orient = 'vertical', command=newContact_sect.yview)
        
        def read():
            # print("update")
            filament_name = []
            filament_color = []
            filament_addetive = []
            filament_brand = []
            filament_remaining = []
            filament_ID = []

            i = 0
            index = 0
            filament_name, filament_color, filament_addetive, filament_brand, filament_remaining, filament_ID = Read.ReadData()
            for names in filament_name:
                # print(names)
                F_color = filament_color[index]
                F_name =  filament_name[index]
                F_addetive = filament_addetive[index]
                F_brand = filament_brand[index]
                F_remaining = filament_remaining[index]
                ID = filament_ID[index]
                

                filament_name[index] = tk.Button(newContact_sect, text=names,activebackground="green",
                                            background="red", height = 1, command=lambda color = F_color,material = F_name, addetive = F_addetive,brand = F_brand, remaining = F_remaining, ID = ID: [Delete.DeleteData(ID),new.destroy(), duty.refresh()])
                filament_name[index].place(x=20, y=40+i)
                i += 40
                index += 1
                
                
            

        
       
        
        confirm_button = tk.Button(newContact_sect, width = '20', text = 'Inventory', bg = "#008037", height = 2, command = read).place(x = 172, y = 455)
        
        
            
        
        
        newContact_sect.pack()


   
    
    
    
    def create_buttons(self, material_name, name, color, material, addetive, brand, remaining,index,i,ID):  
        addFilament_sect = tk.Canvas(self.free_window, width = 350, height = 450, background="blue" )
        material_name[index] = tk.Button(addFilament_sect, text=name,activebackground="green",
                                         background="red", height = 1, command=lambda color = color,material = material, addetive = addetive,brand = brand, remaining = remaining, ID = ID: [self.edit_filament(material,color,addetive, brand, remaining,ID)] )
        
        addFilament_sect.pack()

    




    def makeNameList(self):
        print("update")
        filament_name = []
        filament_color = []
        filament_addetive = []
        filament_brand = []
        filament_remaining = []
        filament_ID = []

        i = 0
        index = 0
        filament_name, filament_color, filament_addetive, filament_brand, filament_remaining, filament_ID = Read.ReadData()
        for names in filament_name:
            F_color = filament_color[index]
            F_name =  filament_name[index]
            F_addetive = filament_addetive[index]
            F_brand = filament_brand[index]
            F_remaining = filament_remaining[index]
            ID = filament_ID[index]
            self.create_buttons(filament_name,names,F_color,F_name,F_addetive,F_brand,F_remaining,index,i,ID)
            i += 40
            index += 1

    #This window is called when the edit button is pressed
    def free_window(self):
        new = tk.Toplevel(self.w)
        new.geometry("500x500")
        new.title("Edit Filament")
        sb = Scrollbar(new)
        sb.pack(side = RIGHT, fill = Y)
        newContact_sect = tk.Canvas(
            new, width="500", background="blue", height=500, yscrollcommand=sb.set)
        
        sb.config(command=newContact_sect.yview)
        

        # scrollbar = ttk.Scrollbar(newContact_sect, orient = 'vertical', command=newContact_sect.yview)
        
        def read():
            # print("update")
            filament_name = []
            filament_color = []
            filament_addetive = []
            filament_brand = []
            filament_remaining = []
            filament_ID = []

            i = 0
            index = 0
            filament_name, filament_color, filament_addetive, filament_brand, filament_remaining, filament_ID = Read.ReadData()
            for names in filament_name:
                # print(names)
                F_color = filament_color[index]
                F_name =  filament_name[index]
                F_addetive = filament_addetive[index]
                F_brand = filament_brand[index]
                F_remaining = filament_remaining[index]
                ID = filament_ID[index]
                

                filament_name[index] = tk.Button(newContact_sect, text=names,activebackground="green",
                                            background="red", height = 1, command=lambda color = F_color,material = F_name, addetive = F_addetive,brand = F_brand, remaining = F_remaining, ID = ID: [self.edit_filament(material,color,addetive, brand, remaining,ID)] )
                filament_name[index].place(x=20, y=40+i)
                i += 40
                index += 1
                
                
            

        
       
        
        confirm_button = tk.Button(newContact_sect, width = '20', text = 'Inventory', bg = "#008037", height = 2, command = read).place(x = 172, y = 455)
        
        
            
        
        
        newContact_sect.pack()

    def edit_filament(self,material, color, addetive, brand, remaining,ID):    
        new = tk.Toplevel(self.w)
        new.geometry("500x500")
        new.title("Add Filament")


        newContact_sect = tk.Canvas(
            new, width="500", background="#7ED957", height=100)
        newContact_sect.create_text(
            175, 60, text="EDIT FILAMENT", fill="white", font="Helvetica 22 bold")
        
        newContact_sect2 = tk.Canvas(
            new, width="500", background="white", height=400)
        

        newContact_sect2.create_text(
            65, 40, text="Material", fill="grey", font="Helvetica 15 bold")
        material_entry = tk.Entry(new, width="20", background="white", foreground="black",
                                highlightbackground="grey", highlightcolor='grey', highlightthickness=4)
        material_entry.insert(0,material)
        material_entry.place(x=14, y=160)

        newContact_sect2.create_text(
            260, 40, text='Color', fill="grey", font="Helvetica 15 bold")
        color_entry = tk.Entry(new, width='20', background='white', foreground="black",
                                highlightcolor="grey", highlightbackground='grey', highlightthickness=4)
        color_entry.insert(0, color)
        color_entry.place(x=200, y=160)


        newContact_sect2.create_text(
            65, 100, text="Addetive", fill='grey', font='Helvetica 15 bold')
        addetive_entry = tk.Entry(new, background='white', foreground="black", highlightcolor="grey",
                                    highlightbackground='grey', highlightthickness=4)
        addetive_entry.insert(0,addetive)
        addetive_entry.place(x=14, y=230)


        newContact_sect2.create_text(
            260, 100, text="Brand", fill="grey", font="Helvetica 15 bold")
        brand_entry = tk.Entry(new, background='white', foreground="black", highlightcolor="grey",
                                highlightbackground='grey', highlightthickness=4)
        brand_entry.insert(0, brand)
        brand_entry.place(x=200, y=230)

        newContact_sect2.create_text(
            65, 169, text="remaining", fill="grey", font="Helvetica 15 bold")
        remaining_entry = tk.Entry(new, width="20", background="white", foreground="black",
                                highlightbackground="grey", highlightcolor='grey', highlightthickness=4)
        remaining_entry.insert(0, remaining)
        remaining_entry.place(x=14, y=290)

        submit_button= tk.Button(new, width = '20', text = "Enter", bg = '#008037', height = 2, command = lambda: [Update.updateData(material_entry,color_entry,addetive_entry,brand_entry,remaining_entry, ID),new.destroy()])
        submit_button.place(x = 14, y = 355)
        

        newContact_sect.pack()
        newContact_sect2.pack()







    # def inventoryGrid(self, material_name, 

    def refresh(self):
        self.weight_entry.delete(0, "end")
        self.text.delete("1.0", "end")






master = tk.Tk()
master.title("3D Print Inventory App")
duty = window(master)
duty.__init__()
master.mainloop()