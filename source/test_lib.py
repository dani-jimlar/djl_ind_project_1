#from source.lib import print_mean, print_median, print_min, print_max
from source import lib
import pandas as pd


def test_print_min(selected):
    '''doc string'''
    #print(lib.print_min(selected))
    assert lib.print_min(selected) == "The min is 0"

if __name__ == "__main__":
    # Print dataset infoß
    #sel = pd.read_csv("source/imp_edos_2.csv", encoding="ISO-8859-1").iloc[:,3]
    sel = pd.read_csv("source/imp_edos_2.csv", encoding="ISO-8859-1").iloc[:,3]
    #print(sel)
    #test_print_max(sel)
    #test_print_median(sel)
    #test_print_max(sel)
    #assert lib.print_min(sel) == "The min is 0"

    test_print_min(sel)
    #min_val = lib.print_min(sel)
    #assert min_val == 0