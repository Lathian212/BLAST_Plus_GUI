'''
Created on Jan 15, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk

class Organism_Exclude(tk.Frame):
    def __init__(self, parent, row = 0, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        #So each member of this class is aware of the row it's gridded to in parent
        self.parent = parent
        self.row = row
        self.entry = tk.Entry(self, width = 50, foreground = 'gray')
        self.entry.bind('<FocusIn>', self.clear)
        self.entry.insert(0, 'Enter organism name or id')
        self.entry.grid(row = 0, column = 0, padx = 5)
        self.check_button = tk.BooleanVar()
        self.check_button = tk.Checkbutton(self, text = 'Exclude', font=('Arial', 9, 'bold'),
                                      variable = self.check_button)
        self.check_button.grid(row = 0, column =2)
        
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