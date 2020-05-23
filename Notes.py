import tkinter  
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import pynput
from pynput.keyboard import *
import os

window = Tk()
window.title("Untitled - Notes")  
window.geometry("1000x450") 

scrollbar = Scrollbar(window)
scrollbar.pack(side = RIGHT, fill = Y) 

typingarea = Text(window, height = 1000, width = 450, yscrollcommand = scrollbar.set, undo = True)  
typingarea.configure(font = ("Courier", 12))
typingarea.pack() 

scrollbar.config(command = typingarea.yview)  

keyboard = Controller()

def new(): 
    typingarea.delete(0.0, END)
    window.title("Untitled - Notes") 

def save_as():
    file_extension = [("Text Document (*.txt)", "*.txt"), ("Rich Text Format (*.rtf)", "*.rtf"), ("Microsoft Word Open XML Document (*.docx)", "*.docx"), ("Microsoft Word Document (*.doc)", "*.doc"), ("Portable Document Format (*.pdf)", "*.pdf")]
    text_file = asksaveasfile(mode = "w", filetypes = file_extension, title = "Save As...")  
    window.title("{NAME OF TEXT FILE} - Notes") 
    data = typingarea.get(0.0, END) 
    text_file.write(data) 
    text_file.close()

def open():
    file_extensions = [("All Files (*.*)", "*.*"), ("Text Document (*.txt)", "*.txt"), ("Rich Text Format (*.rtf)", "*.rtf")] 
    text_file = askopenfile(parent = window, mode = "rb", filetypes = file_extensions, title = "Open...") 

    if text_file == None:
        window.title("{NAME OF TEXT FILE} - Notes")

    if text_file != None:
        window.title("{NAME OF TEXT FILE} - Notes")
        typingarea.delete(0.0, END) 

        data = text_file.read()
        typingarea.insert(0.0, data) 
        text_file.close()  

def exit():
    if messagebox.askyesno("Exit", "Are you sure you want to close Notes?"):
        window.destroy()     

def undo():
    typingarea.edit_undo()

def redo():
    typingarea.edit_redo()

def copy():
    typingarea.event_generate("<<Copy>>") 

def paste():
    typingarea.event_generate("<<Paste>>") 

def cut(): 
    typingarea.event_generate("<<Cut>>")  

def delete():
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)

def backspace():
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace) 

def select_all():
    keyboard.press(Key.ctrl)
    keyboard.press("a")
    keyboard.release("a")
    keyboard.release(Key.ctrl)

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
    showinfo("View Help", "Wdym this is app is soo easy.")  

def about_notes():
    showinfo("About Notes", "Notes 0.1 Beta\nProgrammed by Ashwin Kalyan")

menubar = Menu(window) 

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu) 
filemenu.add_command(label = "New                             ", command = new) 
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
editmenu.add_command(label = "Copy                            ", command = copy)
editmenu.add_command(label = "Paste                           ", command = paste)
editmenu.add_command(label = "Cut                             ", command = cut) 
editmenu.add_separator() 
editmenu.add_command(label = "Delete                          ", command = delete) 
editmenu.add_command(label = "Backspace                       ", command = backspace) 
editmenu.add_separator() 
editmenu.add_command(label = "Select All                      ", command = select_all)

formatmenu = Menu(menubar, tearoff = 0)  
fontmenu = Menu(menubar, tearoff = 0) 
fontsizemenu = Menu(menubar, tearoff = 0) 
fontstylemenu = Menu(menubar, tearoff = 0) 
fontmenu.add_radiobutton(label = "Arial                          ") 
fontmenu.add_radiobutton(label = "Calibri                        ") 
fontmenu.add_radiobutton(label = "Comic Sans MS                  ") 
fontmenu.add_radiobutton(label = "Courier                        ")
fontmenu.add_radiobutton(label = "Geogria                        ")  
fontmenu.add_radiobutton(label = "Times New Roman                ") 
fontmenu.add_radiobutton(label = "Verdana                        ") 
fontsizemenu.add_radiobutton(label = "11  ") 
fontsizemenu.add_radiobutton(label = "12  ") 
fontsizemenu.add_radiobutton(label = "14  ") 
fontsizemenu.add_radiobutton(label = "16  ")
fontsizemenu.add_radiobutton(label = "18  ") 
fontsizemenu.add_radiobutton(label = "20  ") 
fontsizemenu.add_radiobutton(label = "22  ") 
fontsizemenu.add_radiobutton(label = "24  ")
fontsizemenu.add_radiobutton(label = "26  ") 
fontsizemenu.add_radiobutton(label = "28  ")  
fontsizemenu.add_radiobutton(label = "36  ")    
fontsizemenu.add_radiobutton(label = "48  ")   
fontsizemenu.add_radiobutton(label = "72  ")    
fontstylemenu.add_radiobutton(label = "Normal                         ") 
fontstylemenu.add_radiobutton(label = "Bold                           ") 
fontstylemenu.add_radiobutton(label = "Italic                         ") 
fontstylemenu.add_radiobutton(label = "Bold Italic                    ")   
menubar.add_cascade(label = "Format", menu = formatmenu) 
formatmenu.add_cascade(label = "Font                           ", menu = fontmenu)  
formatmenu.add_cascade(label = "Font Size                      ", menu = fontsizemenu) 
formatmenu.add_cascade(label = "Font Style                     ", menu = fontstylemenu)   

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
window.mainloop()
