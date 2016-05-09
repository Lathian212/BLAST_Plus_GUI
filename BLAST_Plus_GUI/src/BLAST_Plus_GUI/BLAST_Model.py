""" Author: Jonathan S. Kwiat

    This module contains the 'model' which has the tk Global variables linked to the view widgets. The appropriate dictionary
    for each view model if delivered to each view object by the Blastn_Controller method 
    self.controller.register_view(self.view_name, self).
    
    This model module also contains the data necessary to intialize some of the view objects such as combo objects with their
    appropriate values.
"""
import tkinter as tk
from tkinter import ttk
import Blastn_Controller as BC

class BLAST_Model(object):
    def __init__(self, controller, *args, **kwargs):
        #Default label frame width reset by setter in controller
        self.frame_width = 1000
        
        #Let's say store and declare all tk.Vars in model
        #Use dictionary with key : value pairs with key being what needs to be on command line taken from BLASTn_Help
        #All keys are deinfed in apendix C of BLAST® Command Line Applications User Manual, http://www.ncbi.nlm.nih.gov/books/NBK279690/

        #Note 'textbox' needs to associated with a reference to the textbox widget itself which is easier and more 
        #comprehensible to do in each view object.
        self.Enter_Subject_Sequence = { 'textbox' : None, 'from' : tk.StringVar(), 'to' : tk.StringVar(), 'up_file' : None}
        
        """This is the view object which contains the query search and the save file."""
        self.Enter_Query_Sequence = { 'textbox' : None, 'from' : tk.StringVar(), 'to' : tk.StringVar(), 'up_file' : None, 
                                     'save_file' : None, '-outfmt' : None, 'if_subject' : tk.BooleanVar()}
        #These are the data values for the output selection combobox
        self.Enter_Query_Sequence['blastn_outputfmt'] = ['pairwise'  , 'query-anchored showing identities'  , 
                    'query-anchored no identities'  , 'flat query-anchored, show identities'  , 
                    'flat query-anchored, no identities'  , 'XML Blast output'  , 'tabular'  , 'tabular with comment lines'  , 
                    'Text ASN.1'  , 'Binary ASN.1'  , 'Comma-separated values'  , 'BLAST archive format (ASN.1)'  , 
                    'JSON Seqalign output'  , 'JSON Blast output'  , 'XML2 Blast output']
        
        """Choose search set: Picks the database and included/excluded organisms. db_box gets set in Choose_Search_Set"""
        #db_box_reference is associate with the database combobox in the view not here. 
        self.Choose_Search_Set = {'radio_button' : tk.IntVar(), 'db_box_reference' : None, '-db' : tk.StringVar(),  
                                  'organisms' : [],  '-entrez_query' : tk.StringVar()}
        #Set radio_button to 3 which is the default (which selects database nt)
        self.Choose_Search_Set['radio_button'].set(3)
        #Labels for database search combobox
        self.Choose_Search_Set['db_box'] = ['Human genomic plus transcript (Human G+T)','Mouse genomic plus transcript (Mouse G+T)', 
                'Nucleotide collection (nr/nt)','Reference RNA sequences (refseq_rna)',
                'Reference genomic sequences (refseq_genomic)', 'RefSeq Representative genomes (refseq_representative_genomes)', 
                'NCBI Genomes (chromosome)', 'Expressed sequence tags (est)',
                'Genomic surveys sequences (gss)' , 'High throughput genomic sequences (HTGS)', 'Patent sequences (pat)', 
                'Protein Data Bank (pdb)','Human ALU repeat elements (alu_repeats)', 'Sequence tagged sites (dbsts)', 
                'Whole-genome shotgun contigs (wgs)', 'Transcriptome Shotgun Assembly (TSA)', 
                '16S ribosomal RNA sequences (Bacteria and Archaea)', 'Sequences Read Archive (SRA)']
        
        """blastn has four different types that need to be selected and added to -task """
        self.Program_Selection = ['blastn-short', 'megablast', 'dc-megablast', 'blastn'] 
        
        """Blast_Button doesn't have any real variables with it but the control invoked by pushing the button needs the following
            data.
        """
        self.BLAST_Button = { 'blast_fourth_text_piece' : ['Short Query Sequence (blastn-short)', 
                                                           'Megablast (Optimize for highly similar sequences)', 
                                                           'Discontiguous megablast (Optimize for highly similar sequences)', 
                                                           'Blastn (Optimize for somewhat similar sequences)']
                           }
        
        """General_Parameters view object: -evalue, and word_size """
        self.General_Parameters = {'expect_threshold' : tk.StringVar(), 'word_size' : tk.StringVar()}
        #Data for the word_size combo box
        self.General_Parameters['wordValues'] = ['16', '20', '24', '28', '32', '48', '64', '128', '256']
        #Default expect_threshold is 10 so set it here.
        self.General_Parameters['expect_threshold'].set(10)
        
        """Scoring Parameter variables: match-mistmatch costs: gap insertion-extension costs """
        self.Scoring_Parameters = {}
        #Note if the key is not present in the dictionary as below it is added to the dictionary
        #These numbers reflect the reward for a match and the penalty for a mismatch
        self.Scoring_Parameters['match_mismatch'] = ['1,-2', '1,-3', '1,-4', '2,-3', '4,-5', '1,-1']
        #The matching tk.StringVar() will be used by the mapper in the control module to retrieve the values
        self.Scoring_Parameters['tkVar_match_mismatch'] = tk.StringVar()
        #Below values are for gap and gap extension costs.
        self.Scoring_Parameters['gap_costs'] = ['Linear', 'Existence:5 Extension:2', 'Existence:2 Extension:2', 
                                                'Existence:1 Extension:2', 'Existence:0 Extension:2', 
                                                'Existence:3 Extension:1', 'Existence:2 Extension:1', 
                                                'Existence:1 Extension:1']
        self.Scoring_Parameters['tkVar_gap_costs'] = tk.StringVar()
        
        """lower case masking is the only type of filtering the command line supports that the ncbi blastn web page also supports.
            Note: The command line does however support a lot of other advanced filtering options but they were not included
            because of time constrains.
        """
        self.Filters_and_Masking = {}
        self.Filters_and_Masking['if_mask_lower'] = tk.BooleanVar()
        self.Filters_and_Masking['if_mask_lower'].set(False)
        
        
        
        

if __name__ == "__main__":
    controller = BC.Blastn_Controller()


