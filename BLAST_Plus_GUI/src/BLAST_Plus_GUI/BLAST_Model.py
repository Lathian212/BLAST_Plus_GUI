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

        self.enter_query_sequence = { '-query' : tk.StringVar(), '-query_loc' : tk.StringVar(), '-entrez_query' : tk.StringVar(), 
                                     '-out' : tk.StringVar(), '-outfmt' : tk.StringVar()}
        

if __name__ == "__main__":
    controller = Blastn_Controller()
    model =

