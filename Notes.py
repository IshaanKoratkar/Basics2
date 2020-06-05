"""
New Window, Save, and the Options functions are still not working so those need to be fixed.
Also, the title formating, ya know when you open a new text file its like "{FILE NAME} - Notes", yeah we need to make that work too.
Also tabs, tabs need to work.
Yeah that's pretty much it.
"""

import tkinter  
from tkinter import ttk 
from tkinter.messagebox import *
from tkinter.filedialog import *
import pynput
from pynput.keyboard import *
import selenium
from selenium import webdriver 
import os
import datetime

window = Tk()
window.title("Untitled - Notes")  
window.geometry("1150x500") 

scrollbar = Scrollbar(window)
scrollbar.pack(side = RIGHT, fill = Y) 

scrollbar_2 = Scrollbar(window, orient = "horizontal")
scrollbar_2.pack(side = BOTTOM, fill = X)  

typingarea = Text(window, height = 1150, width = 500, xscrollcommand = scrollbar_2.set, yscrollcommand = scrollbar.set, undo = True)  
typingarea.configure(font = ("Courier", 12))
typingarea.pack() 

scrollbar.config(command = typingarea.yview)  
scrollbar_2.config(command = typingarea.xview) 

keyboard = Controller()

def save_as():
    file_extension = [("Text Document (*.txt)", "*.txt"), ("Rich Text Format (*.rtf)", "*.rtf")]
    text_file = asksaveasfile(mode = "w", filetypes = file_extension, defaultextension = file_extension, title = "Save As...")  
    window.title("{NAME OF TEXT FILE} - Notes") 
    data = typingarea.get(0.0, END) 
    text_file.write(data) 
    text_file.close()

def new(): 
    if messagebox.askyesno("Notes", "If you haven't saved the currently open file then it will be lost. Do you want to continue?"):
        typingarea.delete(0.0, END)
        window.title("Untitled - Notes") 

    else:
        save_as() 

def open():
    if messagebox.askyesno("Notes", "If you haven't saved the currently open file then it will be lost. Do you want to continue?"):
        file_extensions = [("All Files (*.*)", "*.*"), ("Text Document (*.txt)", "*.txt"), ("Rich Text Format (*.rtf)", "*.rtf")] 
        text_file = askopenfile(parent = window, mode = "rb", filetypes = file_extensions, title = "Open...") 

        window.title("{NAME OF TEXT FILE} - Notes")
        typingarea.delete(0.0, END) 

        data = text_file.read()
        typingarea.insert(0.0, data) 
        text_file.close()  

    else:
        save_as() 

def exit():
    if messagebox.askyesno("Notes", "If you haven't saved the currently open file then it will be lost. Do you want to continue?"):
        window.destroy()     

    else:
        save_as() 

def undo(): 
    keyboard.press(Key.ctrl)
    keyboard.press("z")
    keyboard.release(Key.ctrl)
    keyboard.release("z")

def redo():
    keyboard.press(Key.ctrl)
    keyboard.press("y")
    keyboard.release(Key.ctrl)
    keyboard.release("y")

def copy():
    keyboard.press(Key.ctrl)
    keyboard.press("c")
    keyboard.release(Key.ctrl)
    keyboard.release("c")

def paste():
    keyboard.press(Key.ctrl)
    keyboard.press("v")
    keyboard.release(Key.ctrl)
    keyboard.release("v")

def cut(): 
    keyboard.press(Key.ctrl)
    keyboard.press("x")
    keyboard.release(Key.ctrl)
    keyboard.release("x")

def delete():
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)

def select_all():
    keyboard.press(Key.ctrl)
    keyboard.press("a")
    keyboard.release("a")
    keyboard.release(Key.ctrl)

def date_time():
    date_and_time = str(datetime.datetime.now()) 
    typingarea.insert(0.0, date_and_time) 

def options():
    window_2 = Toplevel() 
    window_2.title("Options...") 
    window_2.geometry("500x185") 

    fontlabel = Label(window_2, text = "Font:")
    fontlabel.grid(column = 3, row = 1)

    fontsizelabel = Label(window_2, text = "Font Size:")
    fontsizelabel.grid(column = 4, row = 1) 

    fonttypelabel = Label(window_2, text = "Font Type:")
    fonttypelabel.grid(column = 5, row = 1)

    fontmenu = ttk.Combobox(window_2, width = 25, values = ["Arial", "Courier", "Times New Roman", "Verdana"])
    fontmenu.grid(column = 3, row = 2)
    fontmenu.current(1)

    fontsizemenu = ttk.Combobox(window_2, width = 8, values = ["8", "9", "10", "11", "12", "14", "16", "18", "20", "22", "24", "28", "36", "48", "72"])
    fontsizemenu.grid(column = 4, row = 2)
    fontsizemenu.current(4)

    fonttypemenu = ttk.Combobox(window_2, width = 15, values = ["Regular", "Bold", "Italic", "Bold Italic"]) 
    fonttypemenu.grid(column = 5, row = 2)
    fonttypemenu.current(0) 

    frame = LabelFrame(window_2, text = "Sample Text", padx = 10, pady = 30, borderwidth = 1) 
    frame.grid(row = 5, column = 1)  

    mainloop() 

def transparency_on():
    window.attributes("-alpha", 0.95) 

def transparency_off():
    window.attributes("-alpha", 1.00)  

def light_mode():
    typingarea.configure(background = "white") 
    typingarea.configure(foreground = "black")

def dark_mode():
    typingarea.configure(background = "gray10") 
    typingarea.configure(foreground = "white") 

def view_help():
    options = webdriver.ChromeOptions()
    options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    browser = webdriver.Chrome("C:\\Users\\Ashwin\\Documents\\Python Apps\\Basics App Suite\\Notes\\chromedriver.exe", chrome_options = options)   
    browser.get("https://www.google.com/search?sxsrf=ALeKk01-BzXrUEFcTW9iu-ejxVgsQQ35_g%3A1590437280250&ei=oCXMXsH1Do3i-gTi_bbgAg&q=Help+with+Windows+10+Notepad&oq=Help+with+Windows+10+Notespad&gs_lcp=CgZwc3ktYWIQA1AAWABg5zRoAHAAeACAAQCIAQCSAQCYAQCqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwjBxYHJ6M_pAhUNsZ4KHeK-DSwQ4dUDCAw&uact=5")
   
def about_notes():
    showinfo("About Notes", "Notes 1.0 Beta                                                            \nBuilt by Ashwin Kalyan                                                            ")

menubar = Menu(window) 

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu) 
filemenu.add_command(label = "New                             ", command = new)
filemenu.add_command(label = "New Tab                         ")   
filemenu.add_command(label = "New Window                      ") 
filemenu.add_separator() 
filemenu.add_command(label = "Save                            ")   
filemenu.add_command(label = "Save as...                      ", command = save_as) 
filemenu.add_command(label = "Open...                         ", command = open) 
filemenu.add_separator()  
filemenu.add_command(label = "Exit                            ", activebackground = "deep pink", command = exit)  

editmenu = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label = "Undo                            ", command = undo)
editmenu.add_command(label = "Redo                            ", command = redo)  
editmenu.add_separator() 
editmenu.add_command(label = "Cut                             ", command = cut) 
editmenu.add_command(label = "Copy                            ", command = copy)
editmenu.add_command(label = "Paste                           ", command = paste)
editmenu.add_command(label = "Delete                          ", command = delete) 
editmenu.add_separator() 
editmenu.add_command(label = "Select All                      ", command = select_all)
editmenu.add_command(label = "Date/Time                       ", command = date_time) 

formatmenu = Menu(menubar, tearoff = 0)  
menubar.add_cascade(label = "Format", menu = formatmenu) 
formatmenu.add_command(label = "Options...                      ", command = options) 

viewmenu = Menu(menubar, tearoff = 0) 
zoommenu = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label = "View", menu = viewmenu)
zoommenu.add_command(label = "Zoom In                         ")  
zoommenu.add_command(label = "Zoom Out                        ") 
zoommenu.add_command(label = "Restore Default Zoom            ") 
viewmenu.add_cascade(label = "Zoom                            ", menu = zoommenu) 
viewmenu.add_separator() 
viewmenu.add_command(label = "Transparency Effects On         ", command = transparency_on) 
viewmenu.add_command(label = "Transparency Effects Off        ", command = transparency_off) 
viewmenu.add_separator() 
viewmenu.add_command(label = "Light Mode                      ", command = light_mode)
viewmenu.add_command(label = "Dark Mode                       ", activebackground = "gray10", command = dark_mode) 

helpmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label = "View Help                       ", command = view_help)
helpmenu.add_separator() 
helpmenu.add_command(label = "About Notes                     ", command = about_notes)

window.config(menu = menubar)
mainloop()
