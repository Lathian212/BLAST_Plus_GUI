'''
Created on Jan 18, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk
import Helper_Functions as HF
import Blastn_Controller as BC

class General_Parameters(ttk.Labelframe):
    def __init__(self, parent, controller = None, view_name = 'General_Parameters', left_row_limit = 8, *args, **kwargs):
        ttk.Labelframe.__init__(self, parent, *args, **kwargs)
        self.view_name = view_name
        self.parent = parent
        if controller is None:
            self.controller = BC.Blastn_Controller()
        else :
            self.controller = controller
        #View object registers with controller with it's string name and self as the reference
        self.model_vars = self.controller.register_view(self.view_name, self)
        self.wordValues = ['16', '20', '24', '28', '32', '48', '64', '128', '256']
        self.ROW = 1
        self.outer_label = ttk.Label(self, text = 'General Parameters', font=('Arial', '14'), relief = 'raised', foreground = 'light sky blue', 
                                     background = 'white')
        self.config(labelwidget = self.outer_label)
        self.left_row_limit = left_row_limit 
        HF.buildMargins(self, self.left_row_limit)
         
        self.buildWidgetSpecifics()
        
    #Widget Layout
    def buildWidgetSpecifics(self):    
        """Lay out Widgets in LabelFrame Container """ 
        self.ROW += 2
        ttk.Label(self, text='Expect threshold:', font=('Arial', '10', 'bold')).grid(row = self.ROW , column = 1, 
                                                                                    columnspan=2, sticky = 'w')
        
        self.expect_entry = ttk.Entry(self, textvariable = self.model_vars['expect_threshold'], width = 8).grid(row = self.ROW, column = 3, sticky = 'W')
        
        self.ROW += 2
        ttk.Label(self, text='Word size:', font=('Arial', '10', 'bold')).grid(row = self.ROW, column = 1, 
                                                                                    columnspan=2, sticky = 'w')
        #Word Size Combo Box values differs for each of the various BLAST have Controller Set Them
        
        self.word_size_box = ttk.Combobox(self, values = self.wordValues ,  textvariable = self.model_vars['word_size'],
                                           state='readonly', width = 7)
        self.word_size_box.grid(row = self.ROW, column = 3, sticky = 'W')
        #Deafult word size is 28
        self.word_size_box.current(3)

if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    
    blast_controller = BC.Blastn_Controller()
    frame = General_Parameters(root, blast_controller)
    frame.grid(row = 0, column = 0)
    frame.setWordSizes(['8', '10'])
    root.mainloop()  