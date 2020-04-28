import tkinter  
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os

window = Tk()
window.geometry("1000x450") 
window.title("Notes")

scrollbar = Scrollbar(window)
scrollbar.pack(side = RIGHT, fill = Y)

typingarea = Text(window, height = 1000, width = 450)
typingarea.pack() 

icon = PhotoImage(file = "Notes_Icon.png") 
window.iconphoto(False, icon) 

def open():

    text_file = askopenfile(parent = window, mode = "rb", title = "Open...")

    if text_file != None:
        contents = text_file.read()
        typingarea.insert("1.0", contents) 
        text_file.close()  

def save():

    file_extension = [("Text Document (*.txt)", "*.txt"), 
                      ("Rich Text Format (*.rtf)", "*.rtf"), 
                      ("Microsoft Word Open XML Document (*.docx)", "*.docx"), 
                      ("Microsoft Word Document (*.doc)", "*.doc"), 
                      ("Portable Document Format (*.pdf)", "*.pdf")]
    text_file = asksaveasfile(mode = "w", filetypes = file_extension, defaultextension = file_extension, title = "Save")   
    data = typingarea.get(0.0, END) 
    text_file.write(data) 
    text_file.close()

def exit():

    if messagebox.askyesno("Exit", "Are you sure you want to close Notes?"):

        window.destroy()     

menubar = Menu(window)

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu) 
filemenu.add_command(label = "New                             ", activebackground = "light sky blue") 
filemenu.add_command(label = "New Window                      ", activebackground = "light sky blue")  
filemenu.add_command(label = "Save                            ", activebackground = "light sky blue", command = save) 
filemenu.add_command(label = "Open...                         ", activebackground = "light sky blue", command = open) 
filemenu.add_separator()  
filemenu.add_command(label = "Print                           ", activebackground = "light sky blue")
filemenu.add_command(label = "Page Format                     ", activebackground = "light sky blue") 
filemenu.add_separator() 
filemenu.add_command(label = "Exit                            ", activebackground = "IndianRed1", command = exit)  

editmenu = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label = "Undo                            ", activebackground = "light sky blue")
editmenu.add_command(label = "Redo                            ", activebackground = "light sky blue")
editmenu.add_separator() 
editmenu.add_command(label = "Copy                            ", activebackground = "light sky blue")
editmenu.add_command(label = "Paste                           ", activebackground = "light sky blue")
editmenu.add_command(label = "Cut                             ", activebackground = "light sky blue") 
editmenu.add_command(label = "Delete                          ", activebackground = "light sky blue")
editmenu.add_separator() 
editmenu.add_command(label = "Select All                      ", activebackground = "light sky blue")
editmenu.add_command(label = "Deselect All                    ", activebackground = "light sky blue")
editmenu.add_separator() 
editmenu.add_command(label = "Datetime                        ", activebackground = "light sky blue") 

viewmenu = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label = "View", menu = viewmenu)
viewmenu.add_command(label = "Zoom In                         ", activebackground = "light sky blue") 
viewmenu.add_command(label = "Zoom Out                        ", activebackground = "light sky blue") 
viewmenu.add_command(label = "Default Zoom                    ", activebackground = "light sky blue") 

helpmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label = "View Help                       ", activebackground = "light sky blue")
helpmenu.add_separator() 
helpmenu.add_command(label = "About Notes                     ", activebackground = "light sky blue")

window.config(menu = menubar)
window.mainloop()
