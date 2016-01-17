'''
Created on Jan 13, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk
import BLASTn_Funcs_Dicts as bd
import Organism_Exclude as oe

class Choose_Search_Set():
    def __init__(self, parent):
        self.ROW = 1
        self.parent = parent
        self.outer_label = ttk.Label(root, text = 'Choose Search Set', font=('Arial', '14'), relief = 'raised', foreground = 'light sky blue', background = 'white')
        self.lFrame = ttk.Labelframe(parent)
        self.lFrame.config(labelwidget = self.outer_label) 
        self.buildMargins()
        self.buildSearchSet()
        

        
        
        self.lFrame.grid(row = 0, column = 0)
    
    
    def buildMargins(self):
        """This method makes cells along the top and right side of the frame so that gridding can easier when it's time to place widgets""" 
        for col in range(10):
            ttk.Label(self.lFrame, text= '%s' % (col+1) , width =10).grid(row = 0, column = (col+1))
        for row in range(100):
            ttk.Label(self.lFrame, text= '%s' % row, width = 3).grid(row = row, column = 0)
            
    def buildSearchSet(self):
        """Adds all the widgets except the organism selection box to the label frame"""
        ttk.Label(self.lFrame, text='Database', font=('Arial', '12', 'bold')
                  ).grid(row = self.ROW, column = 1, columnspan = 1, sticky = 'W')
        
        #Radio buttons linked to combo box each sets the other
        self.radio_int = tk.IntVar()
        self.R1 = tk.Radiobutton(self.lFrame, text="Human genomic + transcript", font=('Arial', '12'),
                             variable=self.radio_int, value=1, command=self.radio_db)
        self.R1.grid(row = self.ROW, column = 2, columnspan = 3, sticky = 'w')
        
        self.R2 = tk.Radiobutton(self.lFrame, text="Mouse genomic + transcript", font=('Arial', '12'),
                             variable=self.radio_int, value=2, command=self.radio_db)
        self.R2.grid(row = self.ROW, column = 5, columnspan = 3, sticky = 'w')
        
        self.R3 = tk.Radiobutton(self.lFrame, text="Others (nr etc.)", font=('Arial', '12'),
                             variable=self.radio_int, value=3, command=self.radio_db)
        self.R3.grid(row = self.ROW, column = 8, columnspan = 3, sticky = 'w')
        self.radio_int.set(1)
        self.ROW+=1
        
        #Combobox for select the database linked to the radio buttons
        self.combo_db_Var = tk.StringVar()
        self.db_box = ttk.Combobox(self.lFrame, values= bd.db_box,  textvariable = self.combo_db_Var, state='readonly', width = 50)
        #XML format is suggested by NCBI so make it default
        self.db_box.current(0)
        self.db_box.bind("<<ComboboxSelected>>", self.combo_db_handler)
        self.db_box.grid(row = self.ROW, column = 2, columnspan = 8, sticky = 'W', padx = 10)
        self.ROW+=1
        #Save a space to put in a fat row if 'Organism' include/exclude needs to be displayed
        self.row_organism = self.ROW
        #This part needs to expand downards vertical as the '+' button is pressed
        self.buildOrganismExlude()
        self.ROW+=1 
        
        ttk.Label(self.lFrame, text = 'Exclude', font = ('Arial', '10', 'bold')).grid(row = self.ROW, column = 1)
        self.check_models = tk.BooleanVar()
        self.check_modelsB = tk.Checkbutton(self.lFrame, text = 'Models(XM/XP)', font=('Arial', 9, 'bold'),
                                      variable = self.check_models)
        self.check_modelsB.grid(row = self.ROW, column = 2)
    
        self.check_env_samp = tk.BooleanVar()
        self.check_env_sampB = tk.Checkbutton(self.lFrame, text = 'Uncultured/evironmental sample sequences', font=('Arial', 9, 'bold'),
                                      variable = self.check_env_samp)
        self.check_env_sampB.grid(row = self.ROW, column = 3, columnspan = 4)
        self.ROW+=1
        ttk.Label(self.lFrame, text = 'Optional', font = ('Arial', '10'), foreground = 'light sky blue').grid(row = self.ROW, column =1)
        self.ROW+=1
        ttk.Label(self.lFrame, text = 'Limit to', font = ('Arial', '10', 'bold')).grid(row = self.ROW, column = 1)
        self.check_sequences = tk.BooleanVar()
        self.check_sequencesB = tk.Checkbutton(self.lFrame, text = 'Sequences from type material', font=('Arial', 9, 'bold'),
                                      variable = self.check_sequences)
        self.check_sequencesB.grid(row = self.ROW, column = 2, columnspan = 2)
        self.ROW+=1
        ttk.Label(self.lFrame, text = 'Optional', font = ('Arial', '10'), foreground = 'light sky blue').grid(row = self.ROW, column =1)
        self.ROW+=1
        ttk.Label(self.lFrame, text = 'Entrez Query', font = ('Arial', '10', 'bold')).grid(row = self.ROW, column = 1)
        self.entrez_query = ttk.Entry(self.lFrame, width = 50)
        self.entrez_query.grid(row = self.ROW, column = 2, columnspan = 4)
        
    def buildOrganismExlude(self):
        self.organism_frame = ttk.Frame(self.lFrame)
        ttk.Label(self.organism_frame, text = 'Organism', font = ('Arial', '10', 'bold')).grid(row = 0, column =0)
        ttk.Label(self.organism_frame, text = 'Optional', font = ('Arial', '10'), foreground = 'light sky blue').grid(row = 1, column =0)
        self.organism_list = []
        self.organism_list.append(oe.Organism_Exclude(self.organism_frame, row = 0))
        self.organism_list[0].grid(row = 0, column = 1)
        self.plus_org = ttk.Button(self.organism_frame, text = '+', width = 3, command = self.addOrganismEntry)
        self.plus_org.grid(row = 0, column = 2)
        
    def addOrganismEntry(self):
        print('called')
        newRow = self.organism_list[-1].row + 1
        print(self.organism_list[-1].row )
        self.organism_list.append(oe.Organism_Exclude(self.organism_frame, newRow))
        self.organism_list[-1].grid(row = newRow, column = 1)
    #Handlers
    def radio_db(self):
        """Linked to combo_db_handler"""
        if self.radio_int.get() == 1 :
            self.db_box.current(0)
            self.organism_frame.grid_forget()
        elif self.radio_int.get() == 2 :
            self.db_box.current(1)
            self.organism_frame.grid_forget()
        else :
            self.db_box.current(2)
            if not self.organism_frame.winfo_ismapped() :
                self.organism_frame.grid(row = self.row_organism, column = 1, columnspan = 10, sticky = 'W')
    
    def combo_db_handler(self, event):
        if self.db_box.current() == 0 :
            self.radio_int.set(1)
            self.organism_frame.forget()
        elif self.db_box.current() == 1 :
            self.radio_int.set(2)
            self.organism_frame.forget()
        else :
            self.radio_int.set(3)
            if not self.organism_frame.winfo_ismapped() :
                self.organism_frame.grid(row = self.row_organism, column = 1, columnspan = 10, sticky = 'W')
        
        print(self.combo_db_Var.get())
    

    

    
if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    
    frame = Choose_Search_Set(root)
    
    root.mainloop()