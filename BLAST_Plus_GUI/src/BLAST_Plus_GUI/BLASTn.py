'''
Created on Jan 9, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import CallBack_Handlers as cb
import BLASTn_Funcs_Dicts as bd
from tkinter import scrolledtext
from Enter_Query_Sequence import Enter_Query_Sequence
from Enter_Sequence import Enter_Sequence
from Choose_Search_Set import Choose_Search_Set
from Program_Selection import Program_Selection 
import Helper_Functions as HF

class BLASTn(ttk.Frame):
    #Attached to radio buttons for switching between Blast types.
    def __init__(self, parent, *args, **kwargs):
        if 'left_row_limit' in kwargs :
            self.left_row_limit = kwargs['left_row_limit']
            del kwargs['left_row_limit']
        else :
            self.left_row_limit = 50 
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        HF.buildMargins(self, self.left_row_limit)
        self.ROW = 1
        self.enter_query = Enter_Query_Sequence(self, 'Query')
        self.enter_query.grid(row = self.ROW, column =1)

        #Rows 2,3,4 will be space for Subject Query Box or Search Set Box Subject
        self.subject_query = Enter_Sequence(self, 'Subject')
        self.search_set = Choose_Search_Set(self)
        self.search_set.grid ( row =3, column = 1, sticky = 'W')
        self.ROW = 5
        self.prg_selection = Program_Selection(self)
        self.prg_selection.grid (row = self.ROW, column = 1, sticky = 'W')
            
    #Handlers        
    def subject_vs_search_toggle(self):
        """It's either Subject Entry Box or Choose Search Set this method toggles between them. Loads with Choose Search Set"""
        #If below is true the check box for triggering a subject against query has just been triggered 
        if self.enter_query.if_subject.get():
            self.search_set.grid_forget()
            self.subject_query.grid (row = 3, column =1, sticky = 'W')
        else :
            self.subject_query.grid_forget()
            self.search_set.grid(row =3, column =1, sticky = 'W')
    

if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    blastn = BLASTn(root, left_row_limit = 20).grid(row = 0, column = 0)
    root.mainloop()

    