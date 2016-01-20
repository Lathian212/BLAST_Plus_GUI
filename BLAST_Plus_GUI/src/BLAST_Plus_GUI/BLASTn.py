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
from BLAST_Button import BLAST_Button 
import General_Parameters_Blastn as GP
import Helper_Functions as HF

class BLASTn(ttk.Frame):
    #Attached to radio buttons for switching between Blast types.
    def __init__(self, parent, set_width, *args, **kwargs):
        if 'left_row_limit' in kwargs :
            self.left_row_limit = kwargs['left_row_limit']
            del kwargs['left_row_limit']
        else :
            self.left_row_limit = 50 
            
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        #Get width of scrolled canvas parent in pixels, chop off some padding and then pass along to each frame so all same width 
        self.parent = parent
        self.parent.update()
        self.set_width = set_width
        print('self.set_width = ' + str(self.set_width))
        
        HF.buildMargins(self, self.left_row_limit)
        
        self.ROW = 1
        self.enter_query = Enter_Query_Sequence(self, 'Query')
        self.enter_query.grid(row = 1, column = 1, sticky = 'W')
        self.enter_query = HF.makeWidgetWidthEven(self, self.set_width, self.enter_query)
        

        #Rows 2,3,4 will be space for Subject Query Box or Search Set Box Subject
        self.subject_query = Enter_Sequence(self, 'Subject')
        
        self.search_set = Choose_Search_Set(self)
        self.search_set.grid ( row =3, column = 1, sticky = 'W')
        self.search_set = HF.makeWidgetWidthEven(self, self.set_width, self.search_set)
        
        self.ROW = 5
        self.prg_selection = Program_Selection(self)
        self.prg_selection.grid (row = self.ROW, column = 1, sticky = 'W')
        self.prg_selection = HF.makeWidgetWidthEven(self, self.set_width, self.prg_selection)
        
        self.ROW += 2
        self.blast_button = BLAST_Button(self, 2)
        self.blast_button.grid (row = self.ROW, column = 1, sticky = 'W')
        self.blast_button = HF.makeWidgetWidthEven(self, self.set_width, self.blast_button)
        
        self.ROW += 2
        tk.Label(self, text = 'Algorithm Parameters:', font = ('Arial', '14', 'bold', 'underline')
                 ).grid(row = self.ROW, column = 1)
                 
        self.ROW += 2
        #Fix so blastn_word_sizes deafults to 28
        self.blastn_word_sizes = ['16', '20', '24', '28', '32', '48', '64', '128', '256']
        self.general_parameters = GP.General_Parameters_Blastn(self, 8, 10, self.blastn_word_sizes, 0)
        self.general_parameters.grid (row = self.ROW, column = 1, sticky = 'W')
        self.blast_button = HF.makeWidgetWidthEven(self, self.set_width, self.general_parameters)
        

            
    #Handlers        
    def subject_vs_search_toggle(self):
        """It's either Subject Entry Box or Choose Search Set this method toggles between them. Loads with Choose Search Set"""
        #If below is true the check box for triggering a subject against query has just been triggered 
        if self.enter_query.if_subject.get():
            #The forget method defaults everything to smart container packing and loses set pixel dimensions
            self.search_set.grid_forget()
            self.subject_query.grid (row = 3, column =1, sticky = 'W')
            self.subject_query = HF.makeWidgetWidthEven(self, self.set_width, self.subject_query)
        else :
            self.subject_query.grid_forget()
            self.search_set.grid(row =3, column =1, sticky = 'W')
            self.search_set = HF.makeWidgetWidthEven(self, self.set_width, self.search_set)
            
    def refresh_search_set(self):
        """When start adding organisms need to expand vertically search set box"""
        self.search_set.grid_forget()
        self.search_set.grid(row =3, column =1, sticky = 'W')
        self.search_set = HF.makeWidgetWidthEven(self, self.set_width, self.search_set)
    

if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    blastn = BLASTn(root, 1000, left_row_limit = 20).grid(row = 0, column = 0)
    root.mainloop()

    