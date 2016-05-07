'''
Created on Jan 9, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import scrolledtext
from Enter_Query_Sequence import Enter_Query_Sequence
from Enter_Sequence import Enter_Sequence
from Choose_Search_Set import Choose_Search_Set
from Program_Selection import Program_Selection
from BLAST_Button import BLAST_Button 
import General_Parameters as GP
import Scoring_Parameters as SP
import Filters_and_Masking as FM
import Helper_Functions as HF
import ScrollableCanvas as sc 
import Blastn_Controller as BC

class BLASTn(ttk.Frame):
    #Attached to radio buttons for switching between Blast types.
    def __init__(self, parent, *args, **kwargs):
        if 'left_row_limit' in kwargs :
            self.left_row_limit = kwargs['left_row_limit']
            del kwargs['left_row_limit']
        else :
            self.left_row_limit = 50 
            
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        #Get width of scrolled canvas parent in pixels, chop off some padding and then pass along to each frame so all same width 
        self.parent = parent
        self.parent.update()
        
        """Declare a controller object to take care of all callbacks/events and model"""
        self.controller = BC.Blastn_Controller()
        self.controller.view_refs['BLAST_Main'] = self
        
        self.controller.buildMargins(self, self.left_row_limit)
        
        self.buildWidgetLayout()
        """
        #Experimenting with Styles
        print('BLASTn widget\'s is = ' + str(self.winfo_class()))
        self.styles = ttk.Style()
        print('TFrame layout = ' + str(self.styles.layout('TFrame')))
        print('Frame.border options = ' + str(self.styles.element_options('Frame.border')))
        """
     
    def buildWidgetLayout(self):   
        self.ROW = 1
        self.enter_query_sequence = Enter_Query_Sequence(self, controller = self.controller)
        self.enter_query_sequence.grid(row = 1, column = 1, sticky = 'W')
        self.enter_query_sequence = self.controller.makeWidgetWidthEven(self.enter_query_sequence)

        #Rows 2,3,4 will be space for Subject Query Box or Search Set Box Subject
        self.enter_subject_sequence = Enter_Sequence(self, controller = self.controller)
        
        self.search_set = Choose_Search_Set(self, controller = self.controller)
        self.search_set.grid ( row =3, column = 1, sticky = 'W')
        self.search_set = self.controller.makeWidgetWidthEven(self.search_set)
        
        self.ROW = 5
        self.prg_selection = Program_Selection(self, self.controller)
        self.prg_selection.grid (row = self.ROW, column = 1, sticky = 'W')
        self.prg_selection = self.controller.makeWidgetWidthEven(self.prg_selection)
        self.controller.view_refs['Program_Selection'] = self.prg_selection
        
        
        self.ROW += 2
        self.blast_button = BLAST_Button(self, self.controller)
        self.blast_button.grid (row = self.ROW, column = 1, sticky = 'W')
        self.blast_button = self.controller.makeWidgetWidthEven(self.blast_button)
        self.controller.view_refs['BLAST'].append(self.blast_button)
        
        self.ROW += 2
        tk.Label(self, text = 'Algorithm Parameters:', font = ('Arial', '14', 'bold', 'underline')
                 ).grid(row = self.ROW, column = 1)
                 
        self.ROW += 2
        self.general_parameters = GP.General_Parameters(self, self.controller)
        self.general_parameters.grid (row = self.ROW, column = 1, sticky = 'W')
        self.general_parameters = self.controller.makeWidgetWidthEven(self.general_parameters)
        self.controller.view_refs['General_Parameters'] = self.general_parameters
        
        self.ROW += 2
        self.scoring_parameters = SP.Scoring_Parameters(self, self.controller)
        self.scoring_parameters.grid (row = self.ROW, column = 1, sticky = 'W')
        self.scoring_parameters = self.controller.makeWidgetWidthEven(self.scoring_parameters)
        self.controller.view_refs['Scoring_Parameters'] = self.scoring_parameters
        
        self.ROW += 2
        self.filters_and_masking = FM.Filters_and_Masking(self, self.controller, ifBlastn = True)
        self.filters_and_masking.grid (row = self.ROW, column = 1, sticky = 'W')
        self.filters_and_masking = self.controller.makeWidgetWidthEven(self.filters_and_masking)
        self.controller.view_refs['Filters_and_Masking'] = self.filters_and_masking
        
        self.ROW += 2
        self.blast_button2 = BLAST_Button(self, self.controller)
        self.blast_button2.grid (row = self.ROW, column = 1, sticky = 'W')
        self.blast_button2 = self.controller.makeWidgetWidthEven(self.blast_button2)
        self.controller.view_refs['BLAST'].append(self.blast_button2)
        
        #self.controller.printKeyValue(self.controller.view_refs)

            

    

if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    sCanvas = sc.ScrollableCanvas(root)
    sFrame = sCanvas.getScrFrame()
    blastn = BLASTn(sFrame, left_row_limit = 20).grid(row = 0, column = 0)
    root.mainloop()

    