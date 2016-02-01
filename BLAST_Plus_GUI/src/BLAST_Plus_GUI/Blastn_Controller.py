'''
Created on Jan 24, 2016

@author: lathian
'''
class Blastn_Controller(object):
    """Controller, handlers of All the GUI widgets in the view with a dictionary to hold all the tk global variables and references to make a mapping to
    the blastn_dict, which holds the command line options, when the BLAST button is pushed. Also the subprocess method """
    def __init__(self):
            # A dictionary containing all the valid options for the blastn command line tool. Note -h, -help, -version might need to be
        # removed. Most of these cannot be set from the GUI but are left here for ideas for extension of the code perhaps in a menu bar.
        self.blastn_dict = { '-h' : None, '-help' : None, '-import_search_strategy' : None,
        '-export_search_strategy' : None, '-task_name' : None, '-db_name' : None,
        '-dbsize_letters' : None, '-gilist' : None, '-seqidlist' : None,
        '-negative_gilist' : None, '-entrez_query_query' : None,
        '-db_soft_mask_algorithm' : None, '-db_hard_mask_algorithm' : None,
        '-subject_input_file' : None, '-subject_loc' : None, '-query_file' : None,
        '-out_file' : None, '-evalue' : None, '-word_size_value' : None,
        '-gapopen_penalty' : None, '-gapextend_penalty' : None,
        '-perc_identity_value' : None, '-qcov_hsp_perc_value' : None,
        '-max_hsps_value' : None, '-xdrop_ungap_value' : None, '-xdrop_gap_value' : None,
        '-xdrop_gap_final_value' : None, '-searchsp_value' : None,
        '-sum_stats_value' : None, '-penalty' : None, '-reward' : None, '-no_greedy' : None,
        '-min_raw_gapped_score_value' : None, '-template_type' : None,
        '-template_length_value' : None, '-dust_options' : None,
        '-filtering_db_database' : None,
        '-window_masker_taxid_masker_taxid' : None,
        '-window_masker_db_masker_db' : None, '-soft_masking_masking' : None,
        '-ungapped' : None, '-culling_limit_value' : None, '-best_hit_overhang_value' : None,
        '-best_hit_score_edge_value' : None, '-window_size_value' : None,
        '-off_diagonal_range_value' : None, '-use_index' : None, '-index_name' : None,
        '-lcase_masking' : None, '-query_loc' : None, '-strand' : None, '-parse_deflines' : None,
        '-outfmt' : None, '-show_gis' : None, '-num_descriptions_value' : None,
        '-num_alignments_value' : None, '-line_length_length' : None, '-html' : None,
        '-max_target_seqs_sequences' : None, '-num_threads_value' : None, '-remote' : None,
        '-version' : None, }
        
        self.frame_refs = { 'Enter_Query_Sequence' : None, 'Enter_Subject_Sequence' : None, 'Choose_Search_Set' : None, 'Program_Selection' : None,
                                  'BLAST' : None, 'General_Parameters' : None, 'Scoring_Parameters' : None, 'Filters_andMasking' : None }
        
        self.wiring_vars = {}
        
    #Handlers
    
    #Enter Query Sequence
    
    #Enter Subject sequence
    
    #Choose Search set
    
    #Program selection
    
    #BLAST
    
    #General parameters
    
    #Scoring parameters
    
    #Filters and masking