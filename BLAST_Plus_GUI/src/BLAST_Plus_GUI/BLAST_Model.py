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
        #Data for the word_size combo box
        self.General_Parameters['wordValues'] = ['16', '20', '24', '28', '32', '48', '64', '128', '256']
        #Default expect_threshold is 10 so set it here.
        self.General_Parameters['expect_threshold'].set(10)
        
        #The model besides holding tk global vars used by the mapper methods in the controller
        #can also be used to hold the initializing data.
        self.Scoring_Parameters = {}
        #Note if the key is not present in the dictionary as below it is added to the dictionary
        #These numbers reflect the reward for a match and the penalty for a mismatch
        self.Scoring_Parameters['match_mismatch'] = ['1,-2', '1,-3', '1,-4', '2,-3', '4,-5', '1,-1']
        #The matching tk.StringVar() will be used by the mapper in the control module to retrieve the values
        self.Scoring_Parameters['tkVar_match_mismatch'] = tk.StringVar()
        #Below values are for gap and gap extension costs.
        self.Scoring_Parameters['gap_costs'] = ['Linear', 'Existence:5 Extension:2', 'Existence:2 Extension:2', 
                                                'Existence:1 Extension:2', 'Existence:0 Extension:2', 
                                                'Existence:3 Extension:1', 'Existence:2 Extension:1', 
                                                'Existence:1 Extension:1']
        self.Scoring_Parameters['tkVar_gap_costs'] = tk.StringVar()
        
        
        
        

if __name__ == "__main__":
    controller = BC.Blastn_Controller()


