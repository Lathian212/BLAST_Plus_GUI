'''
Created on Jan 18, 2016

@author: lathian
The blast algorithm is a heuristic tool that speeds up tremendously its basic goal of find nucleotide sequences that
'align' that is that are similiar. This object connects to the part of the model reflecting reward for matches;
penalties for mismatches; and costs for indels (insertion deleltions) in the DNA sequence and extensions.
'''
import tkinter as tk
from tkinter import ttk
import Blastn_Controller as BC

class Scoring_Parameters(ttk.Labelframe):
    def __init__(self, parent, controller = None, view_name = 'Scoring_Parameters', left_row_limit = 6, *args, **kwargs):
        ttk.Labelframe.__init__(self, parent, *args, **kwargs)
        self.view_name = view_name
        self.parent = parent
        if controller is None:
            self.controller = BC.Blastn_Controller()
        else :
            self.controller = controller
        #View object registers with controller with it's string name and self as the reference
        self.model_vars = self.controller.register_view(self.view_name, self)
        self.ROW = 1
        self.outer_label = ttk.Label(self, text = 'Scoring Parameters', font=('Arial', '14'), 
                                     relief = 'raised', foreground = 'light sky blue', 
                                     background = 'white')
        self.config(labelwidget = self.outer_label)
        self.left_row_limit = left_row_limit 
        self.controller.buildMargins(self, self.left_row_limit)
         
        self.buildWidgetSpecifics()
        
    #Widget Layout
    def buildWidgetSpecifics(self):    
        """Lay out Widgets in LabelFrame Container """ 
        self.ROW += 2
        ttk.Label(self, text='Match/Mismatch \n Scores', 
                  font=('Arial', '10', 'bold')).grid(row = self.ROW , column = 1, columnspan=2, sticky = 'w')
        
        #Match Mismatch Combo Box 
        self.match_mismatch_box = ttk.Combobox(self, values = self.model_vars['match_mismatch'] ,
                                                textvariable = self.model_vars['tkVar_match_mismatch'], 
                                               state='readonly', width = 7)
        self.match_mismatch_box.current(0)
        self.match_mismatch_box.grid(row = self.ROW, column = 3, sticky = 'W')
        
        self.ROW += 2
        ttk.Label(self, text='Gap Costs', font=('Arial', '10', 'bold')).grid(row = self.ROW , column = 1, 
                                                                                    columnspan=2, sticky = 'w')
        
        #Gap Costs Combo Box 
        self.gap_costs_box = ttk.Combobox(self, values = self.model_vars['gap_costs'],
                                            textvariable = self.model_vars['tkVar_gap_costs'], 
                                            state='readonly', width = 20)
        self.gap_costs_box.current(0)
        self.gap_costs_box.grid(row = self.ROW, column = 3, columnspan = 3, sticky = 'W')
        
if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    
    frame = Scoring_Parameters(root)
    frame.grid(row = 0, column = 0)
    root.mainloop()  
