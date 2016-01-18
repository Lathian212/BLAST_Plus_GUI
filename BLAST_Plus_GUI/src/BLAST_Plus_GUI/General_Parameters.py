'''
Created on Jan 18, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk
import Helper_Functions as HF

class General_Parameters(ttk.Labelframe):
    def __init__(self, parent, left_row_limit = 20, *args, **kwargs):
        ttk.Labelframe.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.ROW = 1
        self.parent = parent
        self.outer_label = ttk.Label(self, text = 'General Parameters', font=('Arial', '14'), relief = 'raised', foreground = 'light sky blue', 
                                     background = 'white')
        self.config(labelwidget = self.outer_label)
        self.left_row_limit = left_row_limit 
        HF.buildMargins(self, self.left_row_limit)
         
        self.buildWidgetSpecifics()
        
            #Widget Layout
    def buildWidgetSpecifics(self):    
        """Lay out Widgets in LabelFrame Container """ 
        self.ROW += 1
        ttk.Label(self, text='Expect threshold:', font=('Arial', '10', 'bold')).grid(row = self.ROW , column = 1, 
                                                                                    columnspan=2, sticky = 'w')
        
        self.ROW += 2
        ttk.Label(self, text='Word size:', font=('Arial', '10', 'bold')).grid(row = self.ROW, column = 1, 
                                                                                    columnspan=2, sticky = 'w')
        
        self.ROW += 2
        ttk.Label(self, text='Max matches in a', font=('Arial', '10', 'bold')).grid(row = self.ROW , column = 1, 
                                                                                    columnspan=2, sticky = 'w')
        self.ROW += 1
        ttk.Label(self, text='query range:', font=('Arial', '10', 'bold')).grid(row = self.ROW , column = 1, 
                                                                                    columnspan=2, sticky = 'w')

if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    
    frame = General_Parameters(root,)
    frame.grid(row = 0, column = 0)
    root.mainloop()  