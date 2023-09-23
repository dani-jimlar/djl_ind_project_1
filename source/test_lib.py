#from source.lib import print_mean, print_median, print_min, print_max
import lib
import pandas as pd

def test_print_mean(selected):
    ''' doc string'''
    assert lib.print_mean(selected) == "The mean is 740.56"

def test_print_median(selected):
    '''doc string'''
    assert lib.print_median(selected) == "The median is 185.5"

def test_print_max(selected):
    '''doc string'''
    assert lib.print_max(selected) == "The max is 22782"

def test_print_min(selected):
    '''doc string'''
    #print(lib.print_min(selected))
    assert lib.print_min(selected) == "The min is 0"

if __name__ == "__main__":
    # Print dataset infoß
    #sel = pd.read_csv("source/imp_edos_2.csv", encoding="ISO-8859-1").iloc[:,3]
    sel = pd.read_csv("imp_edos_2.csv", encoding="ISO-8859-1").iloc[:,3]
    #print(sel)
    test_print_mean(sel)
    #test_print_median(sel)
    #test_print_max(sel)

    #assert lib.print_min(sel) == "The min is 0"

    test_print_min(sel)
    #min_val = lib.print_min(sel)
    #assert min_val == 0