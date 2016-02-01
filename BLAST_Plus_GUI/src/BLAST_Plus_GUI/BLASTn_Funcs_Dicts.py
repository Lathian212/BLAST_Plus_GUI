'''
Created on Nov 3, 2015
I will create make functions for each of the 5 dictionaries necessary to store the tk.StringVar()'s for all the options
associated with each command line tool. These dictionaries are the 'wiring' hooking up each widget so that when the BLAST
button is pressed all the information on the page can be collected and sent to subprocess. Also, these dictionaries will allow
state information to be saved when flipping between the blast suite pages.

Supplemental list's, dictionaries and functions will also be here.
@author: Lathian
'''
import tkinter as tk



#The index of this list is the number that needs to be passed to the command line
#Options 6, 7, and 10 can be additionally configured to produce so I'm going to need to bind <<ComboboxSelected>> to handle it
blastn_outputfmt = ['pairwise'  , 'query-anchored showing identities'  , 'query-anchored no identities'  , 
                    'flat query-anchored, show identities'  , 'flat query-anchored, no identities'  , 'XML Blast output'  , 
                    'tabular'  , 'tabular with comment lines'  , 'Text ASN.1'  , 'Binary ASN.1'  , 'Comma-separated values'  , 
                    'BLAST archive format (ASN.1)'  , 'JSON Seqalign output'  , 'JSON Blast output'  , 'XML2 Blast output']
""" Just checking I did my regex correctly 
for i, val in enumerate(blastn_outputfmt):
    print(str(i) +'  '+val)
"""
"""Options 6, 7, and 10 can be additionally configured to produce
   a custom format specified by space delimited format specifiers.
   The supported format specifiers are: """
   


def makeBlastnOptionDict (dictionary):
    """Loads tkinter String Variables (StringVar) as the values of the option dictionary. Mostly there is a one to one
    mapping of each dictionary key to each GUI widget. When the BLAST button if pressed stepping through this dictionary
    will give the data necessary to pass to the command line tool."""
    for opt in dictionary:
        dictionary[opt] = tk.StringVar()
    return dictionary

#Labels for databse search Box
db_box = ['Human genomic plus transcript (Human G+T)', 'Mouse genomic plus transcript (Mouse G+T)', 'Nucleotide collection (nr/nt)',
              'Reference RNA sequences (refseq_rna)', 'Reference genomic sequences (refseq_genomic)', 
              'RefSeq Representative genomes (refseq_representative_genomes)', 'NCBI Genomes (chromosome)', 'Expressed sequence tags (est)',
              'Genomic surveys sequences (gss)' , 'High throughput genomic sequences (HTGS)', 'Patent sequences (pat)', 'Protein Data Bank (pdb)',
              'Human ALU repeat elements (alu_repeats)', 'Sequence tagged sites (dbsts)', 'Whole-genome shotgun contigs (wgs)', 
              'Transcriptome Shotgun Assembly (TSA)', '16S ribosomal RNA sequences (Bacteria and Archaea)', 'Sequences Read Archive (SRA)']

#For command line
db_abrv = ['"Human G+T"', '"Mouse G+T"', '"nr/nt"', 'refseq_rna', 'refseq_genomic', 'refseq_representative_genomes', 
                            'chromosome', 'est','gss' , 'HTGS', 'pat', 'pdb', 'alu_repeats', 'dbsts', 'wgs', 'TSA', '"Bacteria and Archaea"', 'SRA']

