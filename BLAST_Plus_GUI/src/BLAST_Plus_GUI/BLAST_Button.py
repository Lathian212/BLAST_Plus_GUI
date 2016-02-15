'''
Created on Jan 18, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk
import Blastn_Controller as BC

class BLAST_Button(tk.Frame):
    def __init__(self, parent, controller, left_row_limit = 2, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.ROW = 1
        self.controller = controller
        self.parent = parent
        #buildMargins allows easy frame expansion and makes gridding easier
        self.left_row_limit = left_row_limit 
        self.controller.buildMargins(self, self.left_row_limit)
        #BLAST text can be replaced with graphics
        self.BLAST_button = tk.Button(self, text = 'BLAST', command = self.controller.blast, foreground = 'black', background = 'light sky blue')
        self.BLAST_button.grid ( row = 1, column = 1)
        
        self.text = tk.Text(self, width = 80, height = 1, bd = -1)
        self.text.tag_config('blue', foreground = 'light sky blue', font = 'arial 10 bold')
        self.text.tag_config('normal', font = 'arial 10')
        self.text.grid( row =1, column = 2, columnspan = 8, sticky = 'W')
        self.controller.updateText()

        
    #Handlers


if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    
    blast_controller = BC.Blastn_Controller()
    blast_button = BLAST_Button(root, blast_controller)
    blast_button.grid(row = 0, column = 0)
    root.mainloop()   