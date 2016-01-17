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
from Enter_Sequence import Enter_Sequence

class Enter_Query_Sequence(Enter_Sequence):
    def __init__(self, parent, SubOrQuery):
        Enter_Sequence.__init__(self, parent, SubOrQuery)
        self.buildQuery()
        
    def buildQuery(self):    
        """Tacks on to Enter_Sequence Save, Save Format, and Job Title """    
        
        self.ROW+=2
        
        ttk.Label(self, text ='Save File:', font=('Arial', 10, 'bold')).grid(row = self.ROW, 
                                                                                                 column=1, sticky = 'E')
        self.save_query_button = ttk.Button(self, text='Choose File', command = (lambda : self.saveHandler()))
        self.save_query_button.grid(row = self.ROW, column = 2)
        self.save_status = ttk.Label(self, text='No file chosen', font=('Arial', '10'))
        self.save_status.grid(row = self.ROW , column = 3, columnspan = 7, sticky = 'W')
        
        self.ROW+=2

        ttk.Label(self, text ='Save Format:', font=('Arial', 10, 'bold')).grid(row = self.ROW, 
                                                                                         column=1, sticky = 'E')
        
        #bd is the blastFuncsDictionaries module
        self.comboVar = tk.StringVar()
        self.save_output_box = ttk.Combobox(self, values= bd.blastn_outputfmt,  textvariable = self.comboVar, state='readonly', width = 30)
        #XML format is suggested by NCBI so make it default
        self.save_output_box.current(5)
        self.save_output_box.bind("<<ComboboxSelected>>", self.outputFmtHandler)
        self.save_output_box.grid(row = self.ROW, column = 2, columnspan = 4, sticky = 'W', padx = 10)
        #Save current ROW as global to class so if need to pop in additional widget func knows where
        self.row_for_outputFmt = self.ROW
        #If 6,7 or 10 picked additional options must open up

        
        
        self.ROW+=2
        ttk.Label(self, text ='Job Title', font=('Arial', 12, 'bold')).grid(row = self.ROW, column=1, sticky = 'E')
        self.job_title = ttk.Entry(self, font=('Arial', 10))
        self.job_title.grid(row = self.ROW, column = 2, columnspan = 8, sticky = 'W', padx = 10)
        self.job_title.configure(width=80)
        self.ROW+=2
        
        #check_button = tk.Checkbutton(self, text = 'Align two or more sequences', font=('Arial', 12, 'bold'),
        #                              variable = self.checkBut, command = self.align2OrMore)
        #check_button.grid(row = self.ROW, column = 1)
        #self.ROW+=1

    #Callback Handlers
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
        
    def save_handler(self):
        savefilename = asksaveasfilename()
    
    def outputFmtHandler(self, event):
        print(self.save_output_box.current())
        print(self.comboVar.get())

if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    
    frame = Enter_Query_Sequence(root, 'Query')
    frame.grid(row = 0, column = 0)
    
    root.mainloop()        
    