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
import winsound 

def notes():
    window = Tk()
    window.title("Notes")  
    window.geometry("1150x570") 

    tabControl = ttk.Notebook(window) 
    tab1 = ttk.Frame(tabControl)
    tabControl.add(tab1, text = "Untitled                ") 
    tabControl.pack(expand=1, fill="both")

    scrollbar = Scrollbar(tab1, orient = "vertical")  
    scrollbar.pack(side = RIGHT, fill = Y, expand = FALSE) 


    typingarea = Text(tab1, height = 1150, width = 500, yscrollcommand = scrollbar.set, undo = True, borderwidth = 0, wrap = CHAR)  
    typingarea.configure(font = ("Courier", 12))
    typingarea.pack() 

    scrollbar.config(command = typingarea.yview)  


    keyboard = Controller()

    def save_as():
        file_extension = [("Text Document (*.txt)", "*.txt"), ("Rich Text Format (*.rtf)", "*.rtf")]
        text_file = asksaveasfile(mode = "w", filetypes = file_extension, defaultextension = file_extension, title = "Save As...")  
        data = typingarea.get(0.0, END) 
        text_file.write(data) 
        text_file.close()

    def new_tab():
        global tab2
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text = "Untitled                ") 
        tabControl.pack(expand = 1, fill = "both")

        new_scrollbar = Scrollbar(tab2, orient = "vertical")  
        new_scrollbar.pack(side = RIGHT, fill = Y, expand = FALSE) 


        global new_typing_area 
        new_typing_area = Text(tab2, height = 1150, width = 500, yscrollcommand = new_scrollbar.set, undo = True, borderwidth = 0)
        new_typing_area.configure(font = ("Courier", 12))
        new_typing_area.pack()

        new_scrollbar.config(command = new_typing_area.yview)  


    def new(): 
        new_tab() 

    def open():
        new_tab() 
        tabControl.add(tab2, text = "{NAME OF TEXT FILE}                ") 
        
        file_extensions = [("All Files (*.*)", "*.*"), ("Text Document (*.txt)", "*.txt"), ("Rich Text Format (*.rtf)", "*.rtf")] 
        text_file = askopenfile(parent = window, mode = "rb", filetypes = file_extensions, title = "Open...") 

        new_typing_area.delete(0.0, END) 

        data = text_file.read()
        new_typing_area.insert(0.0, data) 
        text_file.close()  

    def exit():
        winsound.PlaySound("SystemAsterick", winsound.SND_ASYNC)

        if messagebox.askyesno("Notes", "If you haven't saved the currently open file then it will be lost. Do you want to continue?"):
            window.destroy()     

        else: 
            save_as() 
            window.destroy()

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
        new_typing_area.insert(0.0, date_and_time)  

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
        
    def view_help():

        try:
            options = webdriver.ChromeOptions()
            options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            browser = webdriver.Chrome("C:\\Users\\Ashwin\\Documents\\Python Apps\\Basics App Suite\\Notes\\chromedriver.exe", chrome_options = options)   
            browser.get("https://www.google.com/search?sxsrf=ALeKk01-BzXrUEFcTW9iu-ejxVgsQQ35_g%3A1590437280250&ei=oCXMXsH1Do3i-gTi_bbgAg&q=Help+with+Windows+10+Notepad&oq=Help+with+Windows+10+Notespad&gs_lcp=CgZwc3ktYWIQA1AAWABg5zRoAHAAeACAAQCIAQCSAQCYAQCqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwjBxYHJ6M_pAhUNsZ4KHeK-DSwQ4dUDCAw&uact=5")
    
        except: 
            winsound.PlaySound("SystemHand", winsound.SND_ASYNC)

            messagebox.showerror("Error", "Web browser not supported.                                                       ") 

    def about_notes(): 
        showinfo("About Notes", "Notes 1.0 Beta                                                            \nBuilt by Ashwin Kalyan                                                            ")

    menubar = Menu(window) 

    filemenu = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = "File", menu = filemenu) 
    filemenu.add_command(label = "New                             ", command = new)
    filemenu.add_command(label = "New Window                      ", command = new_window)  
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
    formatmenu.add_separator() 
    formatmenu.add_checkbutton(label = "Word Wrap                       ") 
    
    tabmenu = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label = "Tab", menu = tabmenu) 
    tabmenu.add_command(label = "New Tab                         ", command = new_tab)  
    tabmenu.add_command(label = "Close Tab                       ") 
    tabmenu.add_command(label = "Close All Tabs                  ")  
    
    viewmenu = Menu(menubar, tearoff = 0) 
    zoommenu = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label = "View", menu = viewmenu)
    zoommenu.add_command(label = "Zoom In                         ")  
    zoommenu.add_command(label = "Zoom Out                        ") 
    zoommenu.add_command(label = "Restore Default Zoom            ") 
    viewmenu.add_cascade(label = "Zoom                            ", menu = zoommenu)
    viewmenu.add_separator() 
    viewmenu.add_checkbutton(label = "Status Bar                      ")  
    viewmenu.add_separator() 
    viewmenu.add_checkbutton(label = "Transparency Effects            ") 

    helpmenu = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = "Help", menu = helpmenu)
    helpmenu.add_command(label = "View Help                       ", command = view_help)
    helpmenu.add_separator() 
    helpmenu.add_command(label = "About Notes                     ", command = about_notes)

    window.config(menu = menubar)
    mainloop()

def new_window():
    notes()

notes() 
