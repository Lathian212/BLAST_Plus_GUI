'''
Created on Jan 9, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import scrolledtext
import Enter_Query_Sequence as EQS
import Enter_Sequence as ES
import Choose_Search_Set as CSS
import Program_Selection as PS
import BLAST_Button as BB 
import General_Parameters as GP
import Scoring_Parameters as SP
import Filters_and_Masking as FM
import ScrollableCanvas as SC  
import Blastn_Controller as BC

class BLASTn(ttk.Frame):
    #Attached to radio buttons for switching between Blast types.
    def __init__(self, parent, controller = None, *args, **kwargs):
        if 'left_row_limit' in kwargs :
            self.left_row_limit = kwargs['left_row_limit']
            del kwargs['left_row_limit']
        else :
            self.left_row_limit = 50 
            
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        #Get width of scrolled canvas parent in pixels, chop off some padding and then pass along to each frame so all same width 
        self.parent = parent
        self.parent.update()
        #If Blastn is not running from main it declares its own controller otherwise it uses main's
        if controller is None:
            self.controller = BC.Blastn_Controller()
        else :
            self.controller = controller
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
        self.BLAST_reset = tk.Button(self, text = 'RESET PAGE', command = self.controller.blast_reset, foreground = 'black', 
                                      background = 'light sky blue')
        self.BLAST_reset.grid ( row = self.ROW, column = 1)
        self.ROW += 1
        
        self.enter_query_sequence = EQS.Enter_Query_Sequence(self, controller = self.controller)
        self.enter_query_sequence.grid(row = self.ROW, column = 1, sticky = 'W')
        self.enter_query_sequence = self.controller.makeWidgetWidthEven(self.enter_query_sequence)
        self.ROW += 1

        #Rows 2,3,4 will be space for Subject Query Box or Search Set Box Subject
        self.enter_subject_sequence = ES.Enter_Sequence(self, controller = self.controller)
        
        self.search_set = CSS.Choose_Search_Set(self, controller = self.controller)
        self.search_set.grid ( row = self.ROW, column = 1, sticky = 'W')
        self.search_set = self.controller.makeWidgetWidthEven(self.search_set)
        
        self.ROW = 5
        self.prg_selection = PS.Program_Selection(self, self.controller)
        self.prg_selection.grid (row = self.ROW, column = 1, sticky = 'W')
        self.prg_selection = self.controller.makeWidgetWidthEven(self.prg_selection)
        self.controller.view_refs['Program_Selection'] = self.prg_selection
        
        
        self.ROW += 2
        self.blast_button = BB.BLAST_Button(self, self.controller)
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
        self.blast_button2 = BB.BLAST_Button(self, self.controller)
        self.blast_button2.grid (row = self.ROW, column = 1, sticky = 'W')
        self.blast_button2 = self.controller.makeWidgetWidthEven(self.blast_button2)
        self.controller.view_refs['BLAST'].append(self.blast_button2)
        
        #self.controller.printKeyValue(self.controller.view_refs)

            

    

if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    sCanvas = SC.ScrollableCanvas(root)
    sFrame = sCanvas.getScrFrame()
    blastn = BLASTn(sFrame, left_row_limit = 20).grid(row = 0, column = 0)
    root.mainloop()

    