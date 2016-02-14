'''
Created on Jan 18, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk
import Helper_Functions as HF

class General_Parameters(ttk.Labelframe):
    def __init__(self, parent, controller, left_row_limit = 8, expectVar = 10, wordValues = ['0'], maxMatches = 0, *args, **kwargs):
        ttk.Labelframe.__init__(self, parent, *args, **kwargs)
        self.controller = controller 
        self.parent = parent
        self.expectVar = tk.StringVar()
        self.expectVar.set(expectVar)
        self.wordValues = wordValues
        self.maxMatches = tk.StringVar()
        self.maxMatches.set(maxMatches)
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
        
        self.expect_entry = ttk.Entry(self, textvariable = self.expectVar, width = 8).grid(row = self.ROW, column = 3, sticky = 'W')
        
        self.ROW += 2
        ttk.Label(self, text='Word size:', font=('Arial', '10', 'bold')).grid(row = self.ROW, column = 1, 
                                                                                    columnspan=2, sticky = 'w')
        #Word Size Combo Box values differs for each of the various BLAST have Controller Set Them
        
        self.word_size_box = ttk.Combobox(self, values = self.wordValues ,  textvariable = self.wordValues, state='readonly', width = 7)
        self.word_size_box.bind("<<ComboboxSelected>>", self.wordSizeHandler)
        self.word_size_box.grid(row = self.ROW, column = 3, sticky = 'W')
        
        self.ROW += 2
        ttk.Label(self, text='Max matches in a', font=('Arial', '10', 'bold')).grid(row = self.ROW , column = 1, 
                                                                                    columnspan=2, sticky = 'w')
        self.ROW += 1
        ttk.Label(self, text='query range:', font=('Arial', '10', 'bold')).grid(row = self.ROW , column = 1, 
                                                                                    columnspan=2, sticky = 'w')
        self.max_matches = ttk.Entry(self, textvariable = self.maxMatches, width = 8).grid(row = self.ROW, column = 3, sticky = 'W')
        
    #Handlers (Move Everything to Controllers?)
    def wordSizeHandler(self):
        pass
    def setWordSizes(self, sizeList):
        self.word_size_box['values'] = sizeList

if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    
    frame = General_Parameters(root)
    frame.grid(row = 0, column = 0)
    frame.setWordSizes(['8', '10'])
    root.mainloop()  