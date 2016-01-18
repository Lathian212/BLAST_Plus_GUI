'''
Created on Jan 17, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import CallBack_Handlers as cb
import BLASTn_Funcs_Dicts as bd
from tkinter import scrolledtext

class Enter_Sequence(ttk.Labelframe):
    def __init__(self, parent, SubOrQuery, left_row_limit = 10, *args, **kwargs):
        ttk.Labelframe.__init__(self, parent, *args, **kwargs)
        self.ROW = 1
        self.parent = parent
        #To identify the container as a Subject or Query container a String is passed in when constructor is called
        self.SubOrQuery = SubOrQuery
        self.outer_label = ttk.Label(self, text = 'Enter ' + self.SubOrQuery + ' Sequence', font=('Arial', '14'), relief = 'raised', foreground = 'light sky blue', background = 'white')
        self.config(labelwidget = self.outer_label)
        self.left_row_limit = left_row_limit 
        self.buildMargins() 
        self.buildEnter()

    #Widget Layout
    def buildMargins(self):
        """This method makes cells along the top and right side of the frame so that gridding can easier when it's time to place widgets""" 
        for col in range(10):
            ttk.Label(self, text= '%s' % (col+1) , width =10).grid(row = 0, column = (col+1))
        for row in range(self.left_row_limit):
            ttk.Label(self, text= '%s' % row, width = 3).grid(row = row, column = 0)
        

    def buildEnter(self):    
        """Builds Enter Query Sequence up to Job Title """    
        
        ttk.Label(self, text='Enter accession number(s), gi(s), or FASTA sequence(s)', 
                 font=('Arial', '12', 'bold')).grid(row = self.ROW , column = 1, columnspan=4, sticky ='w')
        self.clear_button = tk.Button(self, text='Clear', font=('Arial', '9', 'underline'), command = self.clear_query)
        self.clear_button.grid(row = self.ROW, column =5, sticky = 'E')
        ttk.Label(self, text = self.SubOrQuery + ' subrange:', font=('Arial', '12', 'bold', 'underline')
                 ).grid(row = self.ROW, column = 6, columnspan = 2, sticky = 'E')
        self.ROW += 1
        
        self.query_box = scrolledtext.ScrolledText(self, width = 70, height = 7, wrap=tk.CHAR)
        self.query_box.grid(row = self.ROW, column = 1, rowspan = 6, columnspan = 5)

        tk.Label(self, text = 'From:').grid(row = self.ROW, column = 6, sticky = 'E')
        self.query_from = ttk.Entry(self, font=('Arial', 10), width = 15)
        self.query_from.grid(row = self.ROW, column = 7, columnspan = 2, sticky = 'W')
        
        self.ROW+=2
        
        tk.Label(self, text = 'To:').grid(row = self.ROW, column = 6, sticky = 'E')
        self.query_to = tk.Entry(self, font=('Arial', 10), width = 15)
        self.query_to.grid(row = self.ROW, column = 7, columnspan =2 , sticky = 'W')
    
        self.ROW+=5
        #There are objects that inherit from this one that will need to know this value for genetic code widget
        self.upload_file_row = self.ROW
        
        ttk.Label(self, text ='Or, Upload File:', font=('Arial', 10, 'bold')).grid(row = self.ROW, column=1, sticky = 'E')
        
        self.load_query_button = ttk.Button(self, text='Choose File', command = self.load_handler)
        self.load_query_button.grid(row = self.ROW, column = 2)
        self.load_status = ttk.Label(self, text='No file chosen', font=('Arial', '10'))
        self.load_status.grid(row = self.ROW , column = 3, columnspan = 7, sticky = 'W')

    #Callback Handlers
    def get_row(self):
        """Returns how many rows the object spans"""
        return self.ROW
    def clear_query(self):
        input = self.query_box.get('1.0', 'end-1c')
        end = str((len(input)/1.0))
        self.query_box.delete('1.0', end)
    
    def get_query(self):
        input = self.query_box.get('1.0', 'end-1c')
        return input
    
    def get_query_loc(self):
        """Location on the query sequence in 1-based offsets (Format: start-stop)"""
        return(self.query_from.get()+'-'+self.query_to.get())
    
    def load_handler(self):
        filename = askopenfilename()
        self.load_status.configure(text = filename)

if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    
    frame = Enter_Sequence(root, 'Subject')
    frame.grid(row = 0, column = 0)
    #This is so frame.winfo_width() returns its actual dimension rather than 1
    root.update()
    print(frame.winfo_width())
    root.mainloop()       
    