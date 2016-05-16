'''
Created on Jan 17, 2016

@author: lathian
Used as is for the Enter_Subject_Sequence view object which is why the view_name is intialized to that. It gets
overriden for the Choose_Search_Sequence
'''
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import scrolledtext
import Blastn_Controller as BC

#Unfinished because the text entry box has to lead to a pop up which saves the contents to file
class Enter_Sequence(ttk.Labelframe):
    def __init__(self, parent, controller = None, view_name = 'Enter_Subject_Sequence', left_row_limit = 10, *args, **kwargs):
        ttk.Labelframe.__init__(self, parent, *args, **kwargs)
        self.view_name = view_name
        self.parent = parent
        self.ROW = 1
        if controller is None:
            self.controller = BC.Blastn_Controller()
        else :
            self.controller = controller
        #View object registers with controller with it's string name and self as the reference
        self.model_vars = self.controller.register_view(self.view_name, self)
        
        self.outer_label = ttk.Label(self, text = self.view_name, font=('Arial', '14'), relief = 'raised', foreground = 'light sky blue', background = 'white')
        self.config(labelwidget = self.outer_label)
        self.left_row_limit = left_row_limit 
        #All the references the controller will need to handle
        self.controller.buildMargins(self, self.left_row_limit) 
        self.buildEnter()

    #Widget Layout
    def buildEnter(self):    
        """Builds Enter Query Sequence up to Job Title """    
        
        ttk.Label(self, text='Enter accession number(s), gi(s), or FASTA sequence(s)', 
                 font=('Arial', '12', 'bold')).grid(row = self.ROW , column = 1, columnspan=4, sticky ='w')
        self.clear_button = tk.Button(self, text='Clear', font=('Arial', '9', 'underline'),command = 
                                      (lambda view = self: self.controller.clear_query(view)))
        self.clear_button.grid(row = self.ROW, column =5, sticky = 'E')
        ttk.Label(self, text = 'Subrange:', font=('Arial', '12', 'bold', 'underline')
                 ).grid(row = self.ROW, column = 6, columnspan = 2, sticky = 'E')
        self.ROW += 1
        
        self.query_box = scrolledtext.ScrolledText(self, width = 70, height = 7, wrap=tk.CHAR)
        self.query_box.grid(row = self.ROW, column = 1, rowspan = 6, columnspan = 5)
        self.model_vars['textbox'] = self.query_box
        #Event generated only refers to scrolledtext need a reference to load_query_button
         
        self.query_box.bind('<Key>', lambda event, view = self : self.controller.disable_upload_button(event, view))

        tk.Label(self, text = 'From:').grid(row = self.ROW, column = 6, sticky = 'E')

        self.query_from = ttk.Entry(self, textvariable = self.model_vars['from'], font=('Arial', 10), width = 15)
        self.query_from.grid(row = self.ROW, column = 7, columnspan = 2, sticky = 'W')
        
        self.ROW+=2
        
        tk.Label(self, text = 'To:').grid(row = self.ROW, column = 6, sticky = 'E')
        self.query_to = tk.Entry(self, textvariable = self.model_vars['to'], font=('Arial', 10), width = 15)
        self.query_to.grid(row = self.ROW, column = 7, columnspan =2 , sticky = 'W')
    
        self.ROW+=5
        #There are objects that inherit from this one that will need to know this value for genetic code widget
        self.upload_file_row = self.ROW
        
        ttk.Label(self, text ='Or, Upload File:', font=('Arial', 10, 'bold')).grid(row = self.ROW, column=1, sticky = 'E')
        
        self.load_query_button = ttk.Button(self, text='Choose File', command = 
                                            (lambda view = self: self.controller.load_handler(view)))
        self.load_query_button.grid(row = self.ROW, column = 2)
        self.load_status = ttk.Label(self, text='No file chosen', font=('Arial', '10'))
        self.load_status.grid(row = self.ROW , column = 3, columnspan = 7, sticky = 'W')


if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    frame = Enter_Sequence(root)
    frame.grid(row = 0, column = 0)
    root.mainloop()       
    
