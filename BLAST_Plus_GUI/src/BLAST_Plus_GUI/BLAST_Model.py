import tkinter as tk
from tkinter import ttk
import Blastn_Controller as BC

class BLAST_Model(object):
    def __init__(self, controller, *args, **kwargs):
        #Default label frame width reset by setter in controller
        self.frame_width = 1500
        
        #Let's say store and declare all tk.Vars in model
        #Use dictionary with key : value pairs with key being what needs to be on command line taken from BLASTn_Help
        #All keys are deinfed in apendix C of BLAST® Command Line Applications User Manual, http://www.ncbi.nlm.nih.gov/books/NBK279690/
        
        """
        self.view_refs = { 'BLAST_Main' : None, 'Enter_Query_Sequence' : None, 'Enter_Subject_Sequence' : None, 'Choose_Search_Set' : None, 
                   'Program_Selection' : None, 'BLAST' : [], 'General_Parameters' : None, 'Scoring_Parameters' : None, 
                   'Filters_and_Masking' : None }
        """
        self.Enter_Subject_Sequence = { 'textbox' : None, 'from' : tk.StringVar(), 'to' : tk.StringVar(), 'up_file' : None}

        self.Enter_Query_Sequence = { 'textbox' : None, 'from' : tk.StringVar(), 'to' : tk.StringVar(), 'up_file' : None, 
                                     'save_file' : None, '-outfmt' : None, 'add_fmt' : None, 'job_title' : tk.StringVar(),
                                     'if_subject' : tk.BooleanVar()}
        
        self.Choose_Search_Set = {'-db' : tk.StringVar(),  'organisms' : [],  '-entrez_query' : tk.StringVar()}
        
        self.Program_Selection = ['blastn-short', 'megablast', 'dc-megablast', 'blastn']  
        
        self.General_Parameters = {'expect_threshold' : tk.StringVar(), 'word_size' : tk.StringVar()}
        #Default expect_threshold is 10 so set it here.
        self.General_Parameters['expect_threshold'].set(10)
        
        

if __name__ == "__main__":
    controller = BC.Blastn_Controller()


