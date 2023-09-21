"""
This script uses functions from lib.py to generate a brief analysis of a dataset
"""

import pandas as pd 
from source.lib import print_ds_info 
from source.lib import view_data_vis 

from source.lib import save_data_vis 
#import sys
#sys.path.append('source')


dt= pd.read_csv("source/imp_edos_2.csv", encoding="ISO-8859-1")
# Print dataset info
print_ds_info(dt)
# view and save graph
view_data_vis(dt)
save_data_vis(dt)