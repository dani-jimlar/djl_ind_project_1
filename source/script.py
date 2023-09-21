"""
This script uses functions from lib.py to generate a brief analysis of a dataset
"""
import pandas as pd 
import source.lib 
dt= pd.read_csv("source/imp_edos_2.csv", encoding="ISO-8859-1")
# Print dataset info
print_ds_info(dt)
# view and save graph
view_data_vis(dt)
save_data_vis(dt)

#Print descriptive statistics of just one variable.
selected=dt.iloc[:,3]

print_mean(selected)

print_median(selected)

print_max(selected)

print_min(selected)

print_1_qt(selected)

print_3_qt(selected)
