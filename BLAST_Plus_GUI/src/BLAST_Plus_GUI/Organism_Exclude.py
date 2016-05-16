'''
Created on Jan 15, 2016

@author: lathian
This is a part of the Choose_Search_Set it is a text entry box with a check box that serves the purpose of
a boolean. Note the dictionary in the Model for Choose_Search_Set starts with an empty list '[]' to which
these objects are appended if the user starts selecting organisms to include or exclude. If the list does
not have a value of 'None' these Organism_Exclude objects get accessed an parse into -entrez_query statements
such as -entrez_query'NOT Mus musculus[Organism] AND Homo sapiens[Organism]
'''
import tkinter as tk
from tkinter import ttk

class Organism_Exclude(tk.Frame):
    def __init__(self, parent, row = 0, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        #So each member of this class is aware of the row it's gridded to in parent
        self.parent = parent
        self.row = row
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable = self.entry_var, width = 50, foreground = 'gray')
        self.entry.bind('<FocusIn>', self.clear)
        self.entry.insert(0, 'Enter organism name or id')
        self.entry.grid(row = 0, column = 0, padx = 5)
        self.check_button = tk.BooleanVar()
        self.check_button_box = tk.Checkbutton(self, text = 'Exclude', font=('Arial', 9, 'bold'),
                                      variable = self.check_button)
        self.check_button_box.grid(row = 0, column =2)
        
    def clear(self, event):
        """Clear Entry box of default text and set foreground back to black"""
        self.entry.delete(0, 'end')
        self.entry.configure(foreground = 'black')
        
if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    organism_exclude = Organism_Exclude(root).grid(row = 0, column = 0)
    root.mainloop()
