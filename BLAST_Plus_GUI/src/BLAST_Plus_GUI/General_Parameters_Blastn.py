'''
Created on Jan 20, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk
import Helper_Functions as HF
import General_Parameters as GP

class General_Parameters_Blastn(GP.General_Parameters):
    def __init__(self, parent, left_row_limit = 8, *args, **kwargs):
        self.expectVar = 10
        self.wordValues = ['16', '20', '24', '28', '32', '48', '64', '128', '256']
        self.maxMatches = 0
        GP.General_Parameters.__init__(self, parent, left_row_limit, expectVar = self.expectVar, wordValues = self.wordValues, 
                                       maxMatches = self.maxMatches, *args, **kwargs)
        #In parent is self.word_size_box
        self.word_size_box.current(3)

if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    
    frame = General_Parameters_Blastn(root)
    frame.grid(row = 0, column = 0)
    root.mainloop()  