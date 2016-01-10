'''
Created on Jan 9, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import CallBack_Handlers as cb
import BLASTn_Funcs_Dicts as fd
from tkinter import scrolledtext

class BLASTn(ttk.Frame):
    #Attached to radio buttons for switching between Blast types.
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        #Globals
        #Save a reference to canvas_frame so this class' frame can be destroyed and recreated.
        self.parent = parent
        #Most of the widgets need to be hooked up to Tkinter Global Vars
        bnTkVars = fd.blastn_dict
        #Inialize dictionary with Tk String Vars
        bnTkVars = fd.makeBlastnOptionDict(bnTkVars)
        #Widget wiring
        
        #self.ROW needs to be kept track of so code can be moved around and all the griding doesn't need to be adjusted
        self.ROW = 3
        #Below tkinter boolean keeps track of align two or more sequences checkbutton, initializes to false.
        self.checkBut = tk.BooleanVar()
        #IntVar for radio button selection for blast type it's function handler will map it to a StringVar in the 
        #option dictionary
        self.blastn_type = tk.IntVar()
        #Set up widgets by calling methods, grouped into convenient blocks.                             )
        self.buildMargins()
        self.buildEnterQuery()
        
    def buildMargins(self):
        """This method makes cells along the top and right side of the frame so that gridding can easier when it's time to place widgets""" 
        for col in range(10):
            ttk.Label(self, text= '%s' % (col+1) , width =10).grid(row = 0, column = (col+1))
        for row in range(100):
            ttk.Label(self, text= '%s' % row, width = 3).grid(row = row, column = 0)
    
    #Widget Layout
    def buildEnterQuery(self):        
        
        ttk.Label(self, text='Enter Query Sequence:', font=('Arial', '14', 'underline')).grid(row = self.ROW , column = 1, 
                                                                                                    columnspan=4, sticky = 'w')
        self.ROW += 1
        
        ttk.Label(self, text='Enter accession number(s), gi(s), or FASTA sequence(s)', 
                 font=('Arial', '12', 'bold')).grid(row = self.ROW , column = 1, columnspan=4, sticky ='w')
        clear_button = tk.Button(self, text='Clear', font=('Arial', '9', 'underline'))
        clear_button.grid(row = self.ROW, column =5, sticky = 'E')
        ttk.Label(self, text='Query subrange:', font=('Arial', '12', 'bold', 'underline')
                 ).grid(row = self.ROW, column = 7, columnspan = 2, sticky = 'E')
        self.ROW += 1
        
        query_box = scrolledtext.ScrolledText(self, width = 70, height = 7, wrap=tk.CHAR)
        query_box.grid(row = self.ROW, column = 1, rowspan = 6, columnspan = 5)
        

        """
        # textvariable needs to be assigned to global and clear button linked to it.
        # Also it needs to be scrollable in case the user puts a lot into it
        query_box = tk.Text(self, font=('Arial', 10), width = 74, height = 5, highlightbackground = 'black', 
                            highlightcolor = 'yellow')
        query_box.grid(row = self.ROW, column = 1, columnspan = 6, rowspan = 5, sticky = 'w')
        tk.Label(self, text = 'From').grid(row = self.ROW, column = 8)
        query_from = tk.Entry(self, font=('Arial', 10), width = 8)
        query_from.grid(row = self.ROW, column = 9)
        self.ROW+=1
        tk.Label(self, text = 'To').grid(row = self.ROW, column = 8)
        query_to = tk.Entry(self, font=('Arial', 10), width = 8)
        query_to.grid(row = self.ROW, column = 9)
        self.ROW+=4
        tk.Label(self, text ='Or, upload file', font=('Arial', 12, 'bold')).grid(row = self.ROW, column=1, sticky = 'E')
        load_query_button = tk.Button(self, text='Choose File', command = (lambda : self.loadHandler()))
        load_query_button.grid(row = self.ROW, column = 2)
        load_status = tk.Label(self, text='No file chosen', font=('Arial', '10'))
        load_status.grid(row = self.ROW , column = 3)
        self.ROW+=1
        tk.Label(self, text ='Pick save file and format', font=('Arial', 12, 'bold')).grid(row = self.ROW, 
                                                                                                 column=1, sticky = 'E')
        save_query_button = tk.Button(self, text='Choose File', command = (lambda : self.saveHandler()))
        save_query_button.grid(row = self.ROW, column = 2)
        save_status = tk.Label(self, text='No file chosen', font=('Arial', '10'))
        save_status.grid(row = self.ROW , column = 3)
        #textvariable needs to be associate with the right value of the right key in the blast Dictionary
        #bd is the blastFuncsDictionaries module
        save_output_button = ttk.Combobox(self, values= bd.blastn_outputfmt, textvariable= None, state='readonly',)
        #XML format is suggested by NCBI so make it default
        save_output_button.current(5)
        #Save current ROW as global to class so if need to pop in additional widget func knows where
        self.row_for_outputFmt = self.ROW
        #If 6,7 or 10 picked additional options must open up
        save_output_button.bind("<<ComboboxSelected>>", self.outputFmtHandler(self.row_for_outputFmt))
        save_output_button.grid(row = self.ROW, column = 8, columnspan = 3)
        self.ROW+=1
        tk.Label(self, text ='Job Title', font=('Arial', 12, 'bold')).grid(row = self.ROW, column=1, sticky = 'E')
        job_title = tk.Entry(self, font=('Arial', 10))
        job_title.grid(row = self.ROW, column = 2, columnspan = 8)
        job_title.configure(width=80)
        self.ROW+=1
        self.makeVSpace(self)
        check_button = tk.Checkbutton(self, text = 'Align two or more sequences', font=('Arial', 12, 'bold'),
                                      variable = self.checkBut, command = self.align2OrMore)
        check_button.grid(row = self.ROW, column = 1)
        self.ROW+=1
        """
    def buildEnterSubject(self):
        #This is a lot of duplicate code perhaps a method could construct it.
        self.makeVSpace(self)
        #Left side padding (calculated rowspan by printing out self.ROW at end of this block)
        tk.Label(self, text = '     ').grid(row = self.ROW, column = 0, rowspan = 15)
        
        tk.Label(self, text='Enter Subject Sequence:', font=('Arial', '14', 'underline')).grid(row = self.ROW , column = 1, 
                                                                                                    columnspan=4, sticky = 'w')
        self.ROW += 1
        tk.Label(self, text='Enter accession number(s), gi(s), or FASTA sequence(s)', 
                 font=('Arial', '12', 'bold')).grid(row = self.ROW , column = 1, columnspan=4, sticky ='w')
        clear_button = tk.Button(self, text='Clear', font=('Arial', '9', 'underline'))
        clear_button.grid(row = self.ROW, column =4)
        tk.Label(self, text='Subject subrange', font=('Arial', '12', 'bold', 'underline')
                 ).grid(row = self.ROW, column = 5, columnspan = 4, sticky = 'w')
        self.ROW += 1
        # textvariable needs to be assigned to global and clear button linked to it.
        # Also it needs to be scrollable in case the user puts a lot into it
        query_box = tk.Text(self, font=('Arial', 10), width = 74, height = 5, highlightbackground = 'black', 
                            highlightcolor = 'yellow')
        query_box.grid(row = self.ROW, column = 1, columnspan = 6, rowspan = 5, sticky = 'w')
        tk.Label(self, text = 'From').grid(row = self.ROW, column = 8)
        query_from = tk.Entry(self, font=('Arial', 10), width = 8)
        query_from.grid(row = self.ROW, column = 9)
        self.ROW+=1
        tk.Label(self, text = 'To').grid(row = self.ROW, column = 8)
        query_to = tk.Entry(self, font=('Arial', 10), width = 8)
        query_to.grid(row = self.ROW, column = 9)
        self.ROW+=4
        tk.Label(self, text ='Or, upload file', font=('Arial', 12, 'bold')).grid(row = self.ROW, column=1, sticky = 'E')
        load_query_button = tk.Button(self, text='Choose File', command = (lambda : self.loadHandler()))
        load_query_button.grid(row = self.ROW, column = 2)
        load_status = tk.Label(self, text='No file chosen', font=('Arial', '10'))
        load_status.grid(row = self.ROW , column = 3)
        self.ROW+=1
    def buildChooseSearchSet(self):
        pass
    def buildPrgSelection(self):
        #This will need a helper method to map the int values onto -task.
        """ Program selection embodied in the command line option:  -task <String, Permissible values: 'blastn' 'blastn-short' 'dc-megablast'
                'megablast' 'rmblastn' > Task to execute Default = `megablast' """
        self.makeVSpace(self)
        #Left side padding (calculated rowspan by printing out self.ROW at end of this block)
        tk.Label(self, text = '     ').grid(row = self.ROW, column = 0, rowspan = 15)
        
        tk.Label(self, text='Program Selection:', font=('Arial', '14', 'underline')).grid(row = self.ROW , column = 1, 
                                                                                                    columnspan=4, sticky = 'w')
        self.ROW+=1
        tk.Label(self, text='Optimize for:', font=('Arial', '12', 'bold')).grid(row = self.ROW , column = 1, 
                                                                                            columnspan=2, sticky = 'w')
        
        R1 = tk.Radiobutton(self, text="Highly similar sequences (megablast)", font=('Arial', '12'),
                             variable=self.blastn_type, value=1, command=self.blastnTypeHandler)
        R1.grid(row = self.ROW, column = 2, columnspan = 4, sticky = 'w')
        self.ROW+=1
        R2 = tk.Radiobutton(self, text="More dissimilar sequences (discontiguous megablast)", font=('Arial', '12'),
                             variable=self.blastn_type, value=2, command=self.blastnTypeHandler)
        R2.grid(row = self.ROW, column = 2, columnspan = 4, sticky = 'w')
        self.ROW+=1
        R3 = tk.Radiobutton(self, text="Somewhat similar sequences (blastn)", font=('Arial', '12'),
                             variable=self.blastn_type, value=3, command=self.blastnTypeHandler)
        R3.grid(row = self.ROW, column = 2, columnspan = 4, sticky = 'w')
        self.blastn_type.set(1)
        self.ROW+=1
        print('At end of prg selection self.ROW = ' + str(self.ROW))

if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    BLASTn(root).grid(row = 0, column = 0)
    root.mainloop()