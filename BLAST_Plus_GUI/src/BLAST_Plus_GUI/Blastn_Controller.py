'''
Created on Jan 24, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import Helper_Functions as HF

class Blastn_Controller(object):
    """Controller, handlers of All the GUI widgets in the view with a dictionary to hold all the tk global variables and references to make a mapping to
    the blastn_dict, which holds the command line options, when the BLAST button is pushed. Also the subprocess method """
    def __init__(self):        
        self.view_refs = { 'BLAST_Main' : None, 'Enter_Query_Sequence' : None, 'Enter_Subject_Sequence' : None, 'Choose_Search_Set' : None, 
                           'Program_Selection' : None, 'BLAST' : None, 'General_Parameters' : None, 'Scoring_Parameters' : None, 
                           'Filters_andMasking' : None }
        

        
    #Handlers
    #BLAST main view     
            
    def refresh_search_set(self, view):
        """When start adding organisms need to expand vertically search set box"""
        view.search_set.grid_forget()
        view.search_set.grid(row =3, column =1, sticky = 'W')
        view.search_set = HF.makeWidgetWidthEven(view, view.set_width, view.search_set)
    
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
    
    #Enter Query Sequence (Some handlers reused from above)
        
    def save_handler(self, view):
        savefilename = asksaveasfilename()
        view.save_status.configure(text = savefilename)
    
    def outputFmtHandler(self, event, view):
        print(view.save_output_box.current())
        print(view.comboVar.get())
        formatIndex = view.save_output_box.current()
        if formatIndex == 6 or formatIndex == 7 or formatIndex == 10:
            view.specify_further.grid(row = view.row_for_additional_formatting, column =5, sticky = 'E')
            view.additional_formatting_box.grid(row = view.row_for_additional_formatting, column = 6, columnspan = 4, sticky = 'W', padx = 10)
        else :
            view.specify_further.grid_forget()
            view.additional_formatting_box.grid_forget()
            
        
    def subject_vs_search_toggle(self):
        """It's either Subject Entry Box or Choose Search Set this method toggles between them. Loads with Choose Search Set"""
        #If below is true the check box for triggering a subject against query has just been triggered 
        if self.view_refs['Enter_Query_Sequence'].if_subject.get():
            #The forget method defaults everything to smart container packing and loses set pixel dimensions
            self.view_refs['Choose_Search_Set'].grid_forget()
            self.view_refs['Enter_Subject_Sequence'].grid (row = 3, column =1, sticky = 'W')
            self.view_refs['Enter_Subject_Sequence'] = HF.makeWidgetWidthEven(self.view_refs['BLAST_Main'], 
                                                                                self.view_refs['BLAST_Main'].set_width, 
                                                                                self.view_refs['Enter_Subject_Sequence'])
        else :
            self.view_refs['Enter_Subject_Sequence'].grid_forget()
            self.view_refs['Choose_Search_Set'].grid(row =3, column =1, sticky = 'W')
            self.view_refs['Choose_Search_Set'] = HF.makeWidgetWidthEven(self.view_refs['BLAST_Main'], 
                                                                                self.view_refs['BLAST_Main'].set_width, 
                                                                                self.view_refs['Choose_Search_Set'])
    
    def additional_formatting_handler(self, event, view):
        pass
    
    #Choose Search set
    
    #Program selection
    
    #BLAST Button
    
    #General parameters
    
    #Scoring parameters
    
    #Filters and masking
    
    