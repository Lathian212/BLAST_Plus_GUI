'''
Created on Jan 9, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import CallBack_Handlers as cb
import BLASTn_Funcs_Dicts as bd
from tkinter import scrolledtext


class BLASTn(ttk.Frame):
    #Attached to radio buttons for switching between Blast types.
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        #Globals
        #Save a reference to canvas_frame so this class' frame can be destroyed and recreated.
        self.parent = parent
        #Widget wiring
        self.query_from = tk.StringVar()
        self.query_to   = tk.StringVar()
        
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
        self.buildChooseSearchSet()
        
    def buildMargins(self):
        """This method makes cells along the top and right side of the frame so that gridding can easier when it's time to place widgets""" 
        for col in range(10):
            ttk.Label(self, text= '%s' % (col+1) , width =10).grid(row = 0, column = (col+1))
        for row in range(100):
            ttk.Label(self, text= '%s' % row, width = 3).grid(row = row, column = 0)
    
    #Widget Layout
    def buildEnterQuery(self):    
        """Builds Enter Query Sequence up to Job Title """    
        
        ttk.Label(self, text='Enter Query Sequence:', font=('Arial', '14', 'underline')).grid(row = self.ROW , column = 1, 
                                                                                                    columnspan=4, sticky = 'w')
        self.ROW += 1
        
        ttk.Label(self, text='Enter accession number(s), gi(s), or FASTA sequence(s)', 
                 font=('Arial', '12', 'bold')).grid(row = self.ROW , column = 1, columnspan=4, sticky ='w')
        self.clear_button = tk.Button(self, text='Clear', font=('Arial', '9', 'underline'), command = self.clear_query)
        self.clear_button.grid(row = self.ROW, column =5, sticky = 'E')
        ttk.Label(self, text='Query subrange:', font=('Arial', '12', 'bold', 'underline')
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
        
        ttk.Label(self, text ='Or, Upload File:', font=('Arial', 10, 'bold')).grid(row = self.ROW, column=1, sticky = 'E')
        
        self.load_query_button = ttk.Button(self, text='Choose File', command = (lambda : self.load_handler()))
        self.load_query_button.grid(row = self.ROW, column = 2)
        self.load_status = ttk.Label(self, text='No file chosen', font=('Arial', '10'))
        self.load_status.grid(row = self.ROW , column = 3, columnspan = 7, sticky = 'W')
        
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
        """
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
    blastn = BLASTn(root).grid(row = 0, column = 0)
    root.mainloop()

    