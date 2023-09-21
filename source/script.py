"""
This script uses functions from lib.py to generate a brief analysis of a dataset
"""
import lib 
import pandas as pd 


dt= pd.read_csv("/imp_edos_2.csv", encoding="ISO-8859-1")
my_data = pd.read_csv("source/imp_edos_2.csv", encoding="ISO-8859-1")
# Print dataset info
lib.print_ds_info(my_data)
# generate graph
lib.view_data_vis(my_data)
print('hello')
