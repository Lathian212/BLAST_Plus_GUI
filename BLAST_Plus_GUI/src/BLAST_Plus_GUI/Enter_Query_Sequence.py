'''
Created on Jan 17, 2016

@author: lathian
Note this is using inheritance on a simpler view object I created (Enter_Squence). It allows you to pick the
save file, the load file, and the output format.
'''
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from Enter_Sequence import Enter_Sequence
import Blastn_Controller as BC
from tkinter import scrolledtext


class Enter_Query_Sequence(Enter_Sequence):
    def __init__(self, parent, controller = None, view_name = 'Enter_Query_Sequence',  left_row_limit = 18, *args, **kwargs):
        Enter_Sequence.__init__(self, parent, controller , view_name = 'Enter_Query_Sequence', left_row_limit = 18, *args, **kwargs)

        self.buildQuery()

        """
        print('Enter_Query_Sequence widget\'s is = ' + str(self.winfo_class()))
        
        self.styles = ttk.Style()
        print('TLabelFrame layout = ' + str(self.styles.layout('TFrame')))
        print('Frame.border options = ' + str(self.styles.element_options('Frame.border')))
        """
        
    def buildQuery(self):    
        """Tacks on to Enter_Sequence Save, Save Format, and Job Title """    
        
        self.ROW+=2
        
        ttk.Label(self, text ='Save File:', font=('Arial', 10, 'bold')).grid(row = self.ROW, 
                                                                                                 column=1, sticky = 'E')
        self.save_query_button = ttk.Button(self, text='Choose File', command = (lambda : self.controller.save_handler('Enter_Query_Sequence')))
        self.save_query_button.grid(row = self.ROW, column = 2)
        self.save_status = ttk.Label(self, text='No file chosen', font=('Arial', '10'))
        self.save_status.grid(row = self.ROW , column = 3, columnspan = 7, sticky = 'W')
        
        self.ROW+=2

        ttk.Label(self, text ='Save Format:', font=('Arial', 10, 'bold')).grid(row = self.ROW, 
                                                                                         column=1, sticky = 'E')
        
        #bd is the blastFuncsDictionaries module
        self.save_output_box = ttk.Combobox(self, values= self.model_vars['blastn_outputfmt'], state='readonly', width = 30)
        #XML format is suggested by NCBI so make it default
        self.model_vars['-outfmt'] = self.save_output_box
        self.save_output_box.current(5)
        self.save_output_box.bind("<<ComboboxSelected>>", lambda event, view = self : self.controller.outputFmtHandler(event, view))
        self.save_output_box.grid(row = self.ROW, column = 2, columnspan = 4, sticky = 'W', padx = 10)
        #Save current ROW as global to class so if need to pop in additional widget func knows where
        self.row_for_additional_formatting = self.ROW
        
        self.ROW += 1
        
        self.model_vars['if_subject'].set(False)
        #Temporary all the control stuff needs to go to the controller
        self.check_if_subject = tk.Checkbutton(self, text = 'Align two or more sequences', font=('Arial', 9, 'bold'),
                                      variable = self.model_vars['if_subject'], command = self.controller.subject_vs_search_toggle)
        self.check_if_subject.grid(row = self.ROW, column = 1, columnspan = 3, sticky = 'W')
        self.ROW+=1



       
if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    
    frame = Enter_Query_Sequence(root)
    frame.grid(row = 0, column = 1)
    
    root.mainloop()           
