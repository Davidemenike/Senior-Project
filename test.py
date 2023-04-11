import tkinter as tk



master = tk.Tk()
master.title("Phone_book App")
w = tk.Canvas(master, width=650, height=600)
img = tk.PhotoImage(file = "background.png")
w.configure(bg="midnight blue")

w.pack()
master.mainloop()