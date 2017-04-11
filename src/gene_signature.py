"""
Created on Tuesday April 11 15:39:35 2016
@author: The KnowEnG dev team
"""

def cosine_similarity(run_parameters):
    """ gene prioritization """
    from gene_signature_toolbox import run_cosine_similarity
    run_cosine_similarity(run_parameters)


SELECT = {
    "cosine_similarity": cosine_similarity
    }

def main():
    """
    This is the main function to perform gene signture.
    """
    import sys
    from knpackage.toolbox import get_run_directory_and_file
    from knpackage.toolbox import get_run_parameters

    run_directory, run_file = get_run_directory_and_file(sys.argv)
    run_parameters = get_run_parameters(run_directory, run_file)
    SELECT[run_parameters["method"]](run_parameters)

if __name__ == "__main__":
    main()
