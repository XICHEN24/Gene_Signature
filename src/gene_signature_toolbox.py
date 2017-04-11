"""
@author: The KnowEnG dev team
"""
import os
import pandas as pd 
import numpy as np

import knpackage.toolbox as kn
from sklearn.metrics.pairwise import cosine_similarity


def run_cosine_similarity(run_parameters):
	""" perform gene signature using cosine similarity
    Args:
        run_parameters: parameter set dictionary.
    """

	spreadsheet_name_1 = run_parameters['spreadsheet_name_full_path_1']
	spreadsheet_name_2 = run_parameters['spreadsheet_name_full_path_2']
	spreadsheet1 = kn.get_spreadsheet_df(spreadsheet_name_1)
	spreadsheet2 = kn.get_spreadsheet_df(spreadsheet_name_2)
	node_list_1 = spreadsheet1.index
	node_list_2 = spreadsheet2.index
	common_idx = kn.find_common_node_names(node_list_1, node_list_2)

	spreadsheet_value_1 = spreadsheet1.loc[common_idx, :].values
	spreadsheet_value_2 = spreadsheet2.loc[common_idx, :].values
	cos_arr = cosine_similarity(spreadsheet_value_1.T, spreadsheet_value_2.T)
	
	# Convert cosine values to 0 and 1
	max_row_idx = np.argmax(cos_arr, axis=1)
	cos_arr[range(len(spreadsheet1.columns)), max_row_idx] = int(1)
	cos_arr[cos_arr!=1] = int(0)

	file_path = os.path.join(
		run_parameters['results_directory'], 'gene_signature_cos_similarity.tsv')
	result_df = pd.DataFrame(
		cos_arr, index=spreadsheet1.columns, columns=spreadsheet2.columns)
	result_df.to_csv(file_path, header=True, index=True, sep='\t')


