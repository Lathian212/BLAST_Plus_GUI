'''
Created on Jan 13, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk
import BLASTn_Funcs_Dicts as BD
import Organism_Exclude as OE
import Helper_Functions as HF
import Blastn_Controller as BC

class Choose_Search_Set(ttk.Labelframe):
    def __init__(self, parent, controller, left_row_limit = 9, *args, **kwargs):
        ttk.Labelframe.__init__(self, parent, *args, **kwargs)
        self.parent = parent 
        self.ROW = 1
        self.controller = controller
        self.parent = parent
        self.outer_label = ttk.Label(self, text = 'Choose Search Set', font=('Arial', '14'), relief = 'raised', foreground = 'light sky blue',
                                      background = 'white')
        self.config(labelwidget = self.outer_label)
        self.left_row_limit = left_row_limit 
        HF.buildMargins(self, self.left_row_limit)
        self.buildSearchSet()
            
    def buildSearchSet(self):
        """Adds all the widgets except the organism selection box to the label frame"""
        ttk.Label(self, text='Database', font=('Arial', '12', 'bold')
                  ).grid(row = self.ROW, column = 1, columnspan = 1, sticky = 'W')
        
        #Radio buttons linked to combo box each sets the other
        self.radio_int = tk.IntVar()
        self.R1 = tk.Radiobutton(self, text="Human genomic + transcript", font=('Arial', '12'),
                             variable=self.radio_int, value=1, command=self.controller.radio_db)
        self.R1.grid(row = self.ROW, column = 2, columnspan = 3, sticky = 'w')
        
        self.R2 = tk.Radiobutton(self, text="Mouse genomic + transcript", font=('Arial', '12'),
                             variable=self.radio_int, value=2, command=self.controller.radio_db)
        self.R2.grid(row = self.ROW, column = 5, columnspan = 3, sticky = 'w')
        
        self.R3 = tk.Radiobutton(self, text="Others (nr etc.)", font=('Arial', '12'),
                             variable=self.radio_int, value=3, command=self.controller.radio_db)
        self.R3.grid(row = self.ROW, column = 8, columnspan = 3, sticky = 'w')
        self.radio_int.set(3)
        self.ROW+=1
        
        #Combobox for select the database linked to the radio buttons
        self.combo_db_Var = tk.StringVar()
        self.db_box = ttk.Combobox(self, values= BD.db_box,  textvariable = self.combo_db_Var, state='readonly', width = 50)
        #XML format is suggested by NCBI so make it default
        self.db_box.current(2)
        self.db_box.bind("<<ComboboxSelected>>", self.controller.combo_db_handler)
        self.db_box.grid(row = self.ROW, column = 2, columnspan = 8, sticky = 'W', padx = 10)
        self.ROW+=1
        #Save a space to put in a fat row if 'Organism' include/exclude needs to be displayed
        self.row_organism = self.ROW
        #This part needs to expand downards vertical as the '+' button is pressed
        self.buildOrganismExlude()
        self.organism_frame.grid(row = self.row_organism, column = 1, columnspan = 10, sticky = 'W')
        self.ROW+=1 
        
        ttk.Label(self, text = 'Exclude', font = ('Arial', '10', 'bold')).grid(row = self.ROW, column = 1)
        self.check_models = tk.BooleanVar()
        self.check_modelsB = tk.Checkbutton(self, text = 'Models(XM/XP)', font=('Arial', 9, 'bold'),
                                      variable = self.check_models)
        self.check_modelsB.grid(row = self.ROW, column = 2)
    
        self.check_env_samp = tk.BooleanVar()
        self.check_env_sampB = tk.Checkbutton(self, text = 'Uncultured/evironmental sample sequences', font=('Arial', 9, 'bold'),
                                      variable = self.check_env_samp)
        self.check_env_sampB.grid(row = self.ROW, column = 3, columnspan = 4)
        self.ROW+=1
        ttk.Label(self, text = 'Optional', font = ('Arial', '10'), foreground = 'light sky blue').grid(row = self.ROW, column =1)
        self.ROW+=1
        ttk.Label(self, text = 'Limit to', font = ('Arial', '10', 'bold')).grid(row = self.ROW, column = 1)
        self.check_sequences = tk.BooleanVar()
        self.check_sequencesB = tk.Checkbutton(self, text = 'Sequences from type material', font=('Arial', 9, 'bold'),
                                      variable = self.check_sequences)
        self.check_sequencesB.grid(row = self.ROW, column = 2, columnspan = 2)
        self.ROW+=1
        ttk.Label(self, text = 'Optional', font = ('Arial', '10'), foreground = 'light sky blue').grid(row = self.ROW, column =1)
        self.ROW+=1
        ttk.Label(self, text = 'Entrez Query', font = ('Arial', '10', 'bold')).grid(row = self.ROW, column = 1)
        self.entrez_query = ttk.Entry(self, width = 50)
        self.entrez_query.grid(row = self.ROW, column = 2, columnspan = 4)
        
    def buildOrganismExlude(self):
        self.organism_frame = ttk.Frame(self)
        ttk.Label(self.organism_frame, text = 'Organism', font = ('Arial', '10', 'bold')).grid(row = 0, column =0)
        ttk.Label(self.organism_frame, text = 'Optional', font = ('Arial', '10'), foreground = 'light sky blue').grid(row = 1, column =0)
        self.organism_list = []
        self.organism_list.append(OE.Organism_Exclude(self.organism_frame, row = 0))
        self.organism_list[0].grid(row = 0, column = 1, padx = 23)
        self.plus_org = ttk.Button(self.organism_frame, text = '+', width = 3, command = self.controller.addOrganismEntry)
        self.plus_org.grid(row = 0, column = 2)
        

    

    

    

    
if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    
    blast_controller = BC.Blastn_Controller()
    frame = Choose_Search_Set(root, blast_controller)
    frame.controller.view_refs['Choose_Search_Set'] = frame
    frame.grid(row = 0, column = 0)
    
    root.mainloop()