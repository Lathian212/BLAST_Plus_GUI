'''
Created on Jan 24, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

class Blastn_Controller(object):
    """Controller, handlers of All the GUI widgets in the view with a dictionary to hold all the tk global variables and references to make a mapping to
    the blastn_dict, which holds the command line options, when the BLAST button is pushed. Also the subprocess method """
    def __init__(self):        
        self.frame_refs = { 'Enter_Query_Sequence' : None, 'Enter_Subject_Sequence' : None, 'Choose_Search_Set' : None, 'Program_Selection' : None,
                                  'BLAST' : None, 'General_Parameters' : None, 'Scoring_Parameters' : None, 'Filters_andMasking' : None }
        

        
    #Handlers
    
    #Enter_Sequence
    def clear_query(self, view):
        input = view.query_box.get('1.0', 'end-1c')
        end = str((len(input)/1.0))
        view.query_box.delete('1.0', end)
    
    def get_query(self, view):
        input = view.query_box.get('1.0', 'end-1c')
        return input
    
    def get_query_loc(self, view):
        """Location on the query sequence in 1-based offsets (Format: start-stop)"""
        return(view.query_from.get()+'-'+view.query_to.get())
    
    def load_handler(self, view):
        filename = askopenfilename()
        view.load_status.configure(text = filename)
        #Clear Query Box and Diasble It
        view.clear_query()
        view.query_box.config(state='disabled')
    
    #Enter Query Sequence
    
    #Enter Subject sequence
    
    #Choose Search set
    
    #Program selection
    
    #BLAST
    
    #General parameters
    
    #Scoring parameters
    
    #Filters and masking