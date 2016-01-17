'''
Created on Jan 17, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk

class Program_Selection(ttk.Labelframe):
    def __init__(self, parent):
        ttk.Labelframe.__init__(self, parent)
        self.ROW = 1
        self.parent = parent
        self.outer_label = ttk.Label(self, text = 'Program Selection', font=('Arial', '14'), relief = 'raised', foreground = 'light sky blue', background = 'white')
        self.config(labelwidget = self.outer_label)
        self.blastn_type = tk.IntVar()
        self.buildMargins()
        self.buildPrgSelection()
        
    #Widget Layout
    def buildMargins(self):
        """This method makes cells along the top and right side of the frame so that gridding can easier when it's time to place widgets""" 
        for col in range(10):
            ttk.Label(self, text= '%s' % (col+1) , width =10).grid(row = 0, column = (col+1))
        for row in range(100):
            ttk.Label(self, text= '%s' % row, width = 3).grid(row = row, column = 0)
        
    def buildPrgSelection(self):
        #This will need a helper method to map the int values onto -task.
        """ Program selection embodied in the command line option:  -task <String, Permissible values: 'blastn' 'blastn-short' 'dc-megablast'
                'megablast' 'rmblastn' > Task to execute Default = `megablast' """
        ttk.Label(self, text='Optimize for:', font=('Arial', '12', 'bold')).grid(row = self.ROW , column = 1, 
                                                                                            columnspan=2, sticky = 'w')
        
        self.R1 = tk.Radiobutton(self, text="Highly similar sequences (megablast)", font=('Arial', '12'),
                             variable=self.blastn_type, value=1, command=self.blastnTypeHandler)
        self.R1.grid(row = self.ROW, column = 3, columnspan = 4, sticky = 'w')
        self.ROW+=1
        self.R2 = tk.Radiobutton(self, text="More dissimilar sequences (discontiguous megablast)", font=('Arial', '12'),
                             variable=self.blastn_type, value=2, command=self.blastnTypeHandler)
        self.R2.grid(row = self.ROW, column = 3, columnspan = 4, sticky = 'w')
        self.ROW+=1
        self.R3 = tk.Radiobutton(self, text="Somewhat similar sequences (blastn)", font=('Arial', '12'),
                             variable=self.blastn_type, value=3, command=self.blastnTypeHandler)
        self.R3.grid(row = self.ROW, column = 3, columnspan = 4, sticky = 'w')
        self.blastn_type.set(1)
        self.ROW+=1
        
    def blastnTypeHandler(self):
        pass
        
if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    
    frame = Program_Selection(root)
    frame.grid(row = 0, column = 0)
    
    root.mainloop()