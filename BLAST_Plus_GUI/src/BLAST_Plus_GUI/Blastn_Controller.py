'''
Created on Jan 24, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import tkinter.messagebox as tm
import Helper_Functions as HF
import Organism_Exclude as OE
import BLAST_Model as BM
import BLASTn_Funcs_Dicts as BD

class Blastn_Controller(object):
    """Controller, handlers of All the GUI widgets in the view with a dictionary to hold all the tk global variables and references to make a mapping to
    the blastn_dict, which holds the command line options, when the BLAST button is pushed. Also the subprocess method """
    def __init__(self):        
        self.view_refs = { 'BLAST_Main' : None, 'Enter_Query_Sequence' : None, 'Enter_Subject_Sequence' : None, 'Choose_Search_Set' : None, 
                           'Program_Selection' : None, 'BLAST' : [], 'General_Parameters' : None, 'Scoring_Parameters' : None, 
                           'Filters_and_Masking' : None }
        
        #Each view object will have a vars_dict containing tk.Vars and other references needed to map info to the command_line string
        self.command_line_lst = ['blastn']
        #Don't know if I can make use of the MVC design pattern
        self.model = BM.BLAST_Model(self)
        """
        Don't need if I need this extra complexity
        #BLAST button handler will call each individual BLAST method for each view object that maps model to correct string for it's piece
        self.string_mapper = []
        #Populate string_mapper
        self.populate_string_mapper(self)
        """
        
        #Example below how to work with pop up warnings.
        #tm.showinfo('Temp File Will Be Created', 'Temp File Being Created')
        

        
    #Handlers
    def populate_string_mapper(self):
        self.string_mapper.append(object)
    #BLAST main view     
                
    #Enter_Sequence Handlers, used by both Query and Subject View objects so need to take view as parameter
    def clear_query(self, view):
        """Clears text widget entry box used in both subject and query objects"""
        view.query_box.delete(1.0, 'end')
        #Re-enable load button so user can choose to use a file
        view.load_query_button.configure(state = 'normal')
            
    def get_query(self, view):
        input = view.query_box.get('1.0', 'end-1c')
        return input
    
    def get_query_loc(self, view):
        """Location on the query sequence in 1-based offsets (Format: start-stop)"""
        return(view.query_from.get()+'-'+view.query_to.get())
    
    def disable_upload_button(self, event, view):
        view.load_query_button.configure(state = 'disabled')
        print('disable button called')
    
    def load_handler(self, view): 
        filename = askopenfilename()
        view.load_status.configure(text = filename)
        #Clear Query Box and Diasble It
        self.clear_query(view)
        view.query_box.configure(state='disabled')
        #Find if Query or Subject View called this method and update appropriate dictionary in model
        for view_name, view_ref in self.view_refs.items() :
            if view is view_ref :
                break
        sequence_dict = getattr(self.model, str(view_name))
        sequence_dict['up_file'] = filename
       
    def temp_file_handler(self, view_name, model_piece):
        """If textbox in subject or query view object is filled a temp file is created to be funneled into command line tool"""
        text = model_piece['textbox'].get('1.0', 'end -1c')
        if len(text) > 0 :
            print('tempfile being created for ' + str(view_name))
            f = open(str(view_name)+'_Temp', 'w')
            f.write(text)
            model_piece['up_file'] = str(view_name)+'_Temp'
            
        #print('from = ' + model_piece['from'].get() + 'length = ' + str(len(model_piece['from'].get())))
        
    def is_from_to_filled(self, model_piece):
        """returns a boolean indicating if from and to fields are filled, which is used when assembling the command line
            string. If it returns False then the -from and -to strings are not added to the command."""
        if len(model_piece['from'].get()) > 0 and len(model_piece['to'].get()) > 0:
            return True
        else :
            return False
    
    def enter_sequence_mapper(self, view_name):
        """This method creates the command line string for the blastn program for both the Enter_Query_Sequence
            and Enter_Subject_Sequence Objects. I am calling these methods mapper because they map the information
            in the GUI data entry fields into the correct command line string for blastn.
        """
        cmd_string = ''
        if view_name is 'Enter_Subject_Sequence' :
            name = '-subject'
        else :
            name = '-query'
        #Gets a piece of the model that is associated with GUI object
        model_piece = getattr(self.model, str(view_name))
        #create a file when user is using textbox
        self.temp_file_handler(view_name, model_piece)
        cmd_string += name + ' ' + str(model_piece['up_file'])
        if self.is_from_to_filled(model_piece):
            cmd_string += ' ' + name + '_loc ' + model_piece['from'].get() + '-' + model_piece['to'].get()
        return cmd_string
    
    #Enter Query Sequence (Some handlers reused from above)
        
    def save_handler(self, view_name):
        model_piece = getattr(self.model, str(view_name))
        savefilename = asksaveasfilename()
        self.view_refs[view_name].save_status.configure(text = savefilename)
        model_piece['save_file'] = savefilename
    
    def outputFmtHandler(self, event, view):
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
        if self.model.Enter_Query_Sequence['if_subject'].get():
            #The forget method defaults everything to smart container packing and loses set pixel dimensions
            self.view_refs['Choose_Search_Set'].grid_forget()
            self.view_refs['Enter_Subject_Sequence'].grid (row = 3, column =1, sticky = 'W')
            self.view_refs['Enter_Subject_Sequence'] = self.makeWidgetWidthEven( self.view_refs['Enter_Subject_Sequence'])
        else :
            self.view_refs['Enter_Subject_Sequence'].grid_forget()
            self.view_refs['Choose_Search_Set'].grid(row =3, column =1, sticky = 'W')
            self.view_refs['Choose_Search_Set'] = self.makeWidgetWidthEven(self.view_refs['Choose_Search_Set'])
        #BLAST button text needs to be updated
        self.updateText()
    
    def query_sequence_mapper(self):
        """Calls the generic enter_sequence_mapper which is used by the query mapper and the subject mapper and adds on
            the file save name for the remote blast and the output format.
        """
        cmd_string = ''
        view_name = 'Enter_Query_Sequence'
        model_piece = getattr(self.model, view_name)
        cmd_string = self.enter_sequence_mapper(view_name)
        cmd_string += ' -out ' + str(model_piece['save_file']) + ' -outfmt ' + str(model_piece['-outfmt'].current())
        
        print('Entered query sequence mapper')
        return cmd_string
    
    #Choose Search set
    def radio_db(self):
        """Linked to combo_db_handler. That is the three radio buttons for database choices which are: 1)Human genomic
            2) mouse genomic and 3)others. These buttons are linked to the combo box below it in the choose search set
            view
        """
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
        """When you change the drop down combo box this makes the radio buttons move appropriately"""
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
        self.updateText()
        
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
        HF.makeWidgetWidthEven(view, self.model.frame_width, view.search_set)
    #Program selection
    def blastnTypeHandler(self):
        """Radio buttons for type of Blastn, needs to update text associated with BLAST button"""
        self.updateText()
    
    def program_selection_mapper(self):
        """ Returns a string of '-task <type of blastn>' """
        cmd_string = ''
        view_name = 'Program_Selection'
        view_ref = self.view_refs[view_name]
        model_piece = getattr(self.model, view_name)
        cmd_string += ' -task ' + str(model_piece[view_ref.blastn_type.get()])
        print('Entered program_selection_mapper')
        return cmd_string
    
    #BLAST Button
    def blast(self):
        """Needs to spin off a subprocess daemon"""
        query_commands = self.query_sequence_mapper()
        print ('Query commands = ' + query_commands)
        if self.model.Enter_Query_Sequence['if_subject'].get() :
            subject_commands = self.enter_sequence_mapper('Enter_Subject_Sequence')
            print ('Subject commands = ' +subject_commands)
            
        task = self.program_selection_mapper()
        print(task)
        general_parameters = self.general_parameters_mapper()
        print(general_parameters)
        scoring_parameters = self.scoring_parameters_mapper()
        print(scoring_parameters)
        """
        for v in self.command_line_lst:
            print (v)
        """
    
    def updateText(self):
        """Choose Search Set & Subject Sequence & Program Selection all change the text label associated with BLAST Button"""
        #there are two BLAST button references stored in BLAST
        prg_sel = self.view_refs['Program_Selection']
        fourth_string_index = prg_sel.blastn_type.get()
        for i in self.view_refs['BLAST']:
            i.text.configure(state = 'normal')
            i.text.delete('1.0', 'end')
            i.text.insert('end', 'Search ', ('normal'))
            if self.model.Enter_Query_Sequence['if_subject'].get() :
                i.text.insert('end', 'nucleotide sequence ', ('blue'))
            else :
                database = self.view_refs['Choose_Search_Set'].combo_db_Var.get()
                i.text.insert('end', 'database ' + str(database), ('blue'))
            i.text.insert('end', ' using ', ('normal'))
            i.text.insert('end', BD.blast_fourth_text_piece[fourth_string_index] , ('blue'))
            i.text.configure(state = 'disabled')
    
    #General parameters
    def general_parameters_mapper(self):
        """Returns a command string for the expect threshold and the word size"""
        print('Entered general parameters mapper')
        cmd_string = ''
        view_name = 'General_Parameters'
        #Returns the dictionary holding the model variables associated with general parameter view
        model_piece = getattr(self.model, view_name)
        cmd_string += ' -evalue ' + str(model_piece['expect_threshold'].get())
        cmd_string += ' -word_size ' +str(model_piece['word_size'].get())
        return cmd_string
        
    
    #Scoring parameters
    def scoring_parameters_mapper(self):
        """Returns the match mismatch reward/penalty for BLAST search and 
            gap insertion/extension cost for command line blastn
        """
        print('Entered scoring parameters mapper')
        cmd_string = ''
        view_name = 'Scoring_Parameters'
        #Returns the dictionary holding the model variables associated with general parameter view
        model_piece = getattr(self.model, view_name)
        #Get match_mismatch, cast into string, slice string for match / mismatch
        match_mismatch_string = str(model_piece['tkVar_match_mismatch'].get())
        cmd_string += ' -reward ' + match_mismatch_string[0]
        cmd_string += ' -penalty ' + match_mismatch_string[2:]
        gap_cost = str(model_piece['tkVar_gap_costs'].get())
        index_colon = gap_cost.find(':')
        if index_colon != -1:
            gap_insertion_cost = gap_cost[(index_colon+1):(index_colon+2)]
            second_colon = gap_cost.find(':', index_colon+1)
            gap_extension_cost = gap_cost[(second_colon+1):(second_colon+2)]
            cmd_string += ' -gapopen ' + gap_insertion_cost
            cmd_string += ' -gapextend ' + gap_extension_cost
        return cmd_string
    
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
    
    def printKeyValue (self, dictionary):
        """Helper function to print key value pairs in a dictionary"""
        for k, v in dictionary.items():
            print('Key = ' + str(k), ' value = '+str(v))
            
    def register_view(self, view_name, view_reference):
        """Puts reference to view objects into Controller's Dictionary and returns the appropriate dictionary variable from model"""      
        self.view_refs[view_name] = view_reference
        #print(view_name + ' = ' + str(self.view_refs[view_name]))

        return getattr(self.model, str(view_name))
    
    #Methods to Interact with Model
    def set_frames_width(self, width):
        self.model.frame_width = width
    
    