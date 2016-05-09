'''
Created on Jan 17, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk
import Blastn_Controller as BC

class Program_Selection(ttk.Labelframe):
    def __init__(self, parent, controller, left_row_limit = 4, *args, **kwargs):
        ttk.Labelframe.__init__(self, parent, *args, **kwargs)
        self.parent = parent 
        self.ROW = 1
        self.controller = controller
        self.parent = parent
        self.outer_label = ttk.Label(self, text = 'Program Selection', font=('Arial', '14'), relief = 'raised', foreground = 'light sky blue', 
                                     background = 'white')
        self.config(labelwidget = self.outer_label)
        self.blastn_type = tk.IntVar()
        self.left_row_limit = left_row_limit
        self.controller.buildMargins(self, self.left_row_limit)
        self.buildPrgSelection()
        
    def buildPrgSelection(self):
        #This will need a helper method to map the int values onto -task.
        """ Program selection embodied in the command line option:  -task <String, Permissible values: 'blastn' 'blastn-short' 'dc-megablast'
                'megablast' 'rmblastn' > Task to execute Default = `megablast' """
        ttk.Label(self, text='Optimize for:', font=('Arial', '12', 'bold')).grid(row = self.ROW , column = 1, 
                                                                                            columnspan=2, sticky = 'w')
        self.R0 = tk.Radiobutton(self, text="Short Query Sequence (blastn-short)", font=('Arial', '12'),
                             variable=self.blastn_type, value=0, command=self.controller.blastnTypeHandler)
        self.R0.grid(row = self.ROW, column = 3, columnspan = 4, sticky = 'w')  
        self.ROW+=1     
        self.R1 = tk.Radiobutton(self, text="Highly similar sequences (megablast)", font=('Arial', '12'),
                             variable=self.blastn_type, value=1, command=self.controller.blastnTypeHandler)
        self.R1.grid(row = self.ROW, column = 3, columnspan = 4, sticky = 'w')
        self.ROW+=1
        self.R2 = tk.Radiobutton(self, text="More dissimilar sequences (discontiguous megablast)", font=('Arial', '12'),
                             variable=self.blastn_type, value=2, command=self.controller.blastnTypeHandler)
        self.R2.grid(row = self.ROW, column = 3, columnspan = 5, sticky = 'w')
        self.ROW+=1
        self.R3 = tk.Radiobutton(self, text="Somewhat similar sequences (blastn)", font=('Arial', '12'),
                             variable=self.blastn_type, value=3, command=self.controller.blastnTypeHandler)
        self.R3.grid(row = self.ROW, column = 3, columnspan = 4, sticky = 'w')
        self.blastn_type.set(1)
        self.ROW+=1
        

        
if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    
    blast_controller = BC.Blastn_Controller()
    frame = Program_Selection(root, blast_controller)
    blast_controller.view_refs['Program_Selection'] = frame
    frame.grid(row = 0, column = 0)
    

    root.mainloop()