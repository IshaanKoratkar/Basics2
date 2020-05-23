import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import datetime

window = Tk() 
window.title("Clocks") 
window.geometry("650x173")
window.attributes("-alpha", 0.95)
window.configure(bg = "gray10")

label_1 = Label(window, font = ("Times", 50, "bold"), background = "gray10", foreground = "turquoise1")
label_2 = Label(window, font = ("Courier", 30), background = "gray10", foreground = "turquoise2")
label_3 = Label(window, font = ("Arial", 15), background = "gray10", foreground = "turquoise3")  

def title():
    label_1.config(text = "Clocks")  
    label_1.pack(anchor = "center") 

    label_2.config(text = "By Ashwin Kalyan") 
    label_2.pack(anchor = "center") 

    label_3.config(text = "Version 0.1, May 2020") 
    label_3.pack(anchor = "center") 

def digital():
    window_2 = Toplevel(window)  
    window_2.title("Digital Clock") 
    window_2.geometry("870x85") 
    window_2.attributes("-alpha", 0.95)
    window_2.configure(bg = "gray10") 

    menubar_2 = Menu(window_2)
    view = Menu(menubar_2, tearoff = 0) 
    menubar_2.add_cascade(label = "View", menu = view)
    view.add_command(label = "Title                           ", activebackground = "light sky blue", command = title)
    view.add_command(label = "Analog                          ", activebackground = "light sky blue") 
    view.add_command(label = "Digital                         ", activebackground = "light sky blue", command = digital)
    view.add_separator() 
    view.add_command(label = "Exit                            ", activebackground = "IndianRed1", command = exit) 

    window_2.config(menu = menubar_2) 
 
    label_4 = Label(window_2, font = ("Times", 50, "bold"), background = "gray10", foreground = "maroon1") 

    def digital_2():    
        time_text = datetime.datetime.now()
    
        label_4.config(text = time_text) 
        label_4.after(1, digital_2)    
        label_4.pack(anchor = "center") 

    digital_2()   


def exit():
    if messagebox.askyesno("Exit", "Are you sure you want to close Clock?"):
        window.destroy()    

menubar = Menu(window)
view = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label = "View", menu = view)
view.add_command(label = "Title                           ", activebackground = "light sky blue", command = title)
view.add_command(label = "Analog                          ", activebackground = "light sky blue") 
view.add_command(label = "Digital                         ", activebackground = "light sky blue", command = digital)
view.add_separator() 
view.add_command(label = "Exit                            ", activebackground = "IndianRed1", command = exit) 

title()

window.config(menu = menubar)
window.mainloop() 
