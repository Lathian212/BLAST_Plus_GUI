'''
Created on Jan 24, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import Helper_Functions as HF
import Organism_Exclude as OE
import BLAST_Model as BM

class Blastn_Controller(object):
    """Controller, handlers of All the GUI widgets in the view with a dictionary to hold all the tk global variables and references to make a mapping to
    the blastn_dict, which holds the command line options, when the BLAST button is pushed. Also the subprocess method """
    def __init__(self):        
        self.view_refs = { 'BLAST_Main' : None, 'Enter_Query_Sequence' : None, 'Enter_Subject_Sequence' : None, 'Choose_Search_Set' : None, 
                           'Program_Selection' : None, 'BLAST' : None, 'General_Parameters' : None, 'Scoring_Parameters' : None, 
                           'Filters_andMasking' : None }
        self.model = BM.BLAST_Model(self)
        

        
    #Handlers
    #BLAST main view     
                
    #Enter_Sequence Handlers, used by both Query and Subject View objects so need to take view as parameter
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
            self.view_refs['Enter_Subject_Sequence'] = self.makeWidgetWidthEven( self.view_refs['Enter_Subject_Sequence'])
        else :
            self.view_refs['Enter_Subject_Sequence'].grid_forget()
            self.view_refs['Choose_Search_Set'].grid(row =3, column =1, sticky = 'W')
            self.view_refs['Choose_Search_Set'] = self.makeWidgetWidthEven(self.view_refs['Choose_Search_Set'])
    
    def additional_formatting_handler(self, event, view):
        pass
    
    #Choose Search set
    def radio_db(self):
        """Linked to combo_db_handler"""
        view = self.view_refs['Choose_Search_Set']
        if view.radio_int.get() == 1 :
            view.db_box.current(0)
            view.organism_frame.grid_forget()
        elif view.radio_int.get() == 2 :
            view.db_box.current(1)
            view.organism_frame.grid_forget()
        else :
            view.db_box.current(2)
            if not view.organism_frame.winfo_ismapped() :
                view.organism_frame.grid(row = view.row_organism, column = 1, columnspan = 10, sticky = 'W')
                
    def combo_db_handler(self, event):
        """When you change the drop down combo box this makes the radio buttons move apropiately"""
        view = self.view_refs['Choose_Search_Set']
        if view.db_box.current() == 0 :
            view.radio_int.set(1)
            view.organism_frame.forget()
        elif view.db_box.current() == 1 :
            view.radio_int.set(2)
            view.organism_frame.forget()
        else :
            view.radio_int.set(3)
            if not view.organism_frame.winfo_ismapped() :
                view.organism_frame.grid(row = view.row_organism, column = 1, columnspan = 10, sticky = 'W')
        
    def addOrganismEntry(self):
        """Creates more organism include exclude view objects for users to enter species"""
        view = self.view_refs['Choose_Search_Set']
        newRow = view.organism_list[-1].row + 1
        view.organism_list.append(OE.Organism_Exclude(view.organism_frame, newRow))
        view.organism_list[-1].grid(row = newRow, column = 1)
        self.refresh_search_set()
        
    def refresh_search_set(self):
        """When start adding organism include/exclude boxes need to reset frame width so it is in line with others"""
        view = self.view_refs['Choose_Search_Set']
        view.grid_forget()
        view.grid(row =3, column =1, sticky = 'W')
        HF.makeWidgetWidthEven(view, view.set_width, view.search_set)
    #Program selection
    def blastnTypeHandler(self):
        """Radio buttons for type of Blastn, needs to update text associated with BLAST button"""
        view = self.view_refs['Program_Selection']
        print(str(view.blastn_type.get()))
    
    #BLAST Button
    def blast(self):
        """Needs to spin off a subprocess daemon"""
        pass
    
    def updateText(self):
        """Choose Search Set & Subject Sequence & Program Selection all change the text label associated with BLAST Button"""
        #there will neede to be TWO text boxes that get updated for the two BLAST buttons and the MODEL needs to reflect this
        return
        self.text.configure(state = 'normal')
        for key, value in self.view_refs.items():
            if value is None:
                self.text.insert('1.0', 'here is the default text', 'normal')
                self.text.configure(state = 'disabled')
    
    #General parameters
    
    #Scoring parameters
    
    #Filters and masking
    
    #Helper Methods For View
    def buildMargins(self, view, left_row_limit):
        """This method makes cells along the top and right side of the frame so that gridding can easier when it's time to place widgets""" 
        for col in range(10):
            ttk.Label(view, text= '%s' % (col+1) , width =10).grid(row = 0, column = (col+1))
        for row in range(left_row_limit):
            ttk.Label(view, text= '%s' % row, width = 3).grid(row = row, column = 0)
                
    def makeWidgetWidthEven (self, widget):
        """Resizes widget to set_width"""
        self.view_refs['BLAST_Main'].parent.update()
        widget_height = widget.winfo_height()
        #Turn off propagate which sets widget size based on what it contains and what it is contained in
        widget.grid_propagate(False)
        #widget.configure (width = self.model.frame_width, height = 500)
        widget.configure (width = self.model.frame_width, height = widget_height)
        return widget
    
    #Methods to Interact with Model
    def set_frames_width(self, width):
        self.model.frame_width = width
    
    