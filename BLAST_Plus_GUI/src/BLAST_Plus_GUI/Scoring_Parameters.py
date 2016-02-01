'''
Created on Jan 18, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk
import Helper_Functions as HF

class Scoring_Parameters(ttk.Labelframe):
    def __init__(self, parent, left_row_limit = 6, *args, **kwargs):
        ttk.Labelframe.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.ROW = 1
        self.outer_label = ttk.Label(self, text = 'Scoring Parameters', font=('Arial', '14'), relief = 'raised', foreground = 'light sky blue', 
                                     background = 'white')
        self.config(labelwidget = self.outer_label)
        self.left_row_limit = left_row_limit 
        HF.buildMargins(self, self.left_row_limit)
         
        self.buildWidgetSpecifics()
        
    #Widget Layout
    def buildWidgetSpecifics(self):    
        """Lay out Widgets in LabelFrame Container """ 
        self.ROW += 2
        ttk.Label(self, text='Match/Mismatch \n Scores', font=('Arial', '10', 'bold')).grid(row = self.ROW , column = 1, 
                                                                                    columnspan=2, sticky = 'w')
        
        #Match Mismatch Combo Box 
        self.match_mismatch = ['1,-2', '1,-3', '1,-4', '2, -3', '4, -5', '1, -1']
        self.match_mismatch_var = tk.StringVar()
        self.match_mismatch_box = ttk.Combobox(self, values = self.match_mismatch ,  textvariable = self.match_mismatch_var, 
                                               state='readonly', width = 7)
        self.match_mismatch_box.current(0)
        self.match_mismatch_box.bind("<<ComboboxSelected>>", self.wordSizeHandler)
        self.match_mismatch_box.grid(row = self.ROW, column = 3, sticky = 'W')
        
        self.ROW += 2
        ttk.Label(self, text='Gap Costs', font=('Arial', '10', 'bold')).grid(row = self.ROW , column = 1, 
                                                                                    columnspan=2, sticky = 'w')
        
        #Gap Costs Combo Box (This and above can be refactored Label/Combo Box combined widget) 
        self.gap_costs = ['Linear', 'Existence:5 Extension:2', 'Existence:2 Extension:2', 'Existence:1 Extension:2', 'Existence:0 Extension:2', 
                          'Existence:3 Extension:1', 'Existence:2 Extension:1', 'Existence:1 Extension:1']
        self.gap_costs_var = tk.StringVar()
        self.gap_costs_box = ttk.Combobox(self, values = self.gap_costs ,  textvariable = self.gap_costs_var, 
                                               state='readonly', width = 20)
        self.gap_costs_box.current(0)
        self.gap_costs_box.bind("<<ComboboxSelected>>", self.wordSizeHandler)
        self.gap_costs_box.grid(row = self.ROW, column = 3, columnspan = 3, sticky = 'W')
        
    #Handlers (Move Everything to Controllers?)
    def wordSizeHandler(self):
        pass
    def setWordSizes(self, sizeList):
        self.word_size_box['values'] = sizeList
    

if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    
    frame = Scoring_Parameters(root)
    frame.grid(row = 0, column = 0)
    root.mainloop()  