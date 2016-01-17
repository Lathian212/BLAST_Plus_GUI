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

class BLASTn(ttk.Frame):
    #Attached to radio buttons for switching between Blast types.
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.buildMargins()
        self.ROW = 1
        self.enter_query = Enter_Query_Sequence(self, 'Query')
        self.enter_query.grid(row = self.ROW, column =1)
        #Get width in pixels to even out label frames
        self.frame_max_width = self.enter_query.winfo_width()
        #Rows 2,3,4 will be space for Subject Query Box or Search Set Box Subject
        self.subject_query = Enter_Sequence(self, 'Subject')
        self.search_set = Choose_Search_Set(self)
        self.search_set.grid ( row =3, column = 1, sticky = 'W')
        self.ROW = 5
        self.prg_selection = Program_Selection(self)
        self.prg_selection.grid (row = self.ROW, column = 1, sticky = 'W')

    def buildMargins(self):
        """This method makes cells along the top and right side of the frame so that gridding can easier when it's time to place widgets""" 
        for col in range(10):
            ttk.Label(self, text= '%s' % (col+1) , width =10).grid(row = 0, column = (col+1))
        for row in range(100):
            ttk.Label(self, text= '%s' % row, width = 3).grid(row = row, column = 0)
            
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
    blastn = BLASTn(root).grid(row = 0, column = 0)
    root.mainloop()

    