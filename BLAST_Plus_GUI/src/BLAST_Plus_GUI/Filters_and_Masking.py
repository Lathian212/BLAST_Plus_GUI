'''
Created on Jan 18, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk
import Blastn_Controller as BC

class Filters_and_Masking(ttk.Labelframe):
    def __init__(self, parent, controller = None, view_name = 'Filters_and_Masking', 
                 left_row_limit = 7, ifBlastn = False, *args, **kwargs):
        ttk.Labelframe.__init__(self, parent, *args, **kwargs)
        self.view_name = view_name
        self.parent = parent
        self.ROW = 1
        if controller is None:
            self.controller = BC.Blastn_Controller()
        else :
            self.controller = controller
        #View object registers with controller with it's string name and self as the reference
        self.model_vars = self.controller.register_view(self.view_name, self)
        self.outer_label = ttk.Label(self, text = 'Masking', font=('Arial', '14'), 
                                     relief = 'raised', foreground = 'light sky blue', 
                                     background = 'white')
        self.config(labelwidget = self.outer_label)
        self.left_row_limit = left_row_limit 
        self.controller.buildMargins(self, self.left_row_limit)
         
        self.buildWidgetSpecifics()
        
    #Widget Layout
    def buildWidgetSpecifics(self):    
        """Lay out Widgets in LabelFrame Container """ 
        self.ROW += 1
        
        ttk.Label(self, text='Mask', font=('Arial', '10', 'bold')).grid(row = self.ROW , column = 1, sticky = 'w')
        self.check_if_mask_lower = tk.Checkbutton(self, text = 'Mask lower case letters', font=('Arial', 9, 'bold'),
                                      variable = self.model_vars['if_mask_lower'])
        self.check_if_mask_lower.grid(row = self.ROW, column = 2, columnspan = 4, sticky = 'W')
        
        self.ROW += 1

if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    
    frame = Filters_and_Masking(root, ifBlastn = True)
    frame.grid(row = 0, column = 0)
    root.mainloop()  