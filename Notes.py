import tkinter  
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os

#class commands():

class window():
    
    window = Tk()
    window.geometry("1000x450") 
    window.title("Notes")

    scrollbar = Scrollbar(window)
    scrollbar.pack(side = RIGHT, fill = Y)

    typingarea = Text(window, height = 1000, width = 450)
    typingarea.pack()

    icon = PhotoImage(file = "Notes_Icon.png") 
    window.iconphoto(False, icon) 

    class menubar(): 

        menubar = Menu(window)

        filemenu = Menu(menubar, tearoff = 0) 
        filemenu.add_command(label = "New                       ") 
        filemenu.add_command(label = "New Window                ")  
        filemenu.add_command(label = "Open...                   ") 
        filemenu.add_command(label = "Save                      ") 
        filemenu.add_separator() 
        filemenu.add_command(label = "Exit                      ") 
        menubar.add_cascade(label = "File", menu = filemenu)

        editmenu = Menu(menubar, tearoff = 0) 
        editmenu.add_command(label = "Undo                          ") 
        editmenu.add_command(label = "Redo                          ")
        editmenu.add_command(label = "Copy                          ")
        editmenu.add_command(label = "Paste                         ") 
        editmenu.add_command(label = "Cut                           ") 
        editmenu.add_command(label = "Delete                        ") 
        editmenu.add_separator() 
        editmenu.add_command(label = "Select All                    ") 
        editmenu.add_separator() 
        editmenu.add_command(label = "Datetime                      ") 
        menubar.add_cascade(label = "Edit", menu = editmenu)

        viewmenu = Menu(menubar, tearoff=0) 
        viewmenu.add_command(label = "Zoom In                   ") 
        viewmenu.add_command(label = "Zoom Out                  ") 
        viewmenu.add_command(label = "Default Zoom              ") 
        menubar.add_cascade(label = "View", menu = viewmenu)

        helpmenu = Menu(menubar, tearoff = 0)
        helpmenu.add_command(label = "View Help                 ")
        helpmenu.add_separator() 
        helpmenu.add_command(label = "About Notes               ")
        menubar.add_cascade(label = "Help", menu = helpmenu)

        window.config(menu = menubar)

window.mainloop()
