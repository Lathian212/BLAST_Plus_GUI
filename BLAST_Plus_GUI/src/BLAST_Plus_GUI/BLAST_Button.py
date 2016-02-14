'''
Created on Jan 18, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk
import Helper_Functions as HF

class BLAST_Button(tk.Frame):
    def __init__(self, parent, controller, left_row_limit = 1, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.ROW = 1
        self.controller = controller
        self.parent = parent
        #buildMargins allows easy frame expansion and makes gridding easier
        self.left_row_limit = left_row_limit 
        HF.buildMargins(self, self.left_row_limit)
        #BLAST text can be replaced with graphics
        self.BLAST_button = tk.Button(self, text = 'BLAST', command = self.blast, foreground = 'black', background = 'light sky blue')
        self.BLAST_button.grid ( row = 1, column = 1)
        
        self.dynamic = ttk.Label(self, text = 'Needs dynamic updating text?', font=('Arial', '14'), relief = 'raised', foreground = 'light sky blue', 
                                 background = 'white')
        self.dynamic.grid( row =1, column = 3, columnspan = 4)
        
    #Handlers
    def blast(self):
        """Needs to spin off a subprocess daemon"""
        pass

if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    
    blast_button = BLAST_Button(root, 1, background = 'white')
    blast_button.grid(row = 0, column = 0)
    root.mainloop()   