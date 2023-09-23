from source import lib
import pandas as pd
import requests


def test_print_min(selected):
    '''doc string'''
    #print(lib.print_min(selected))
    assert lib.print_min(selected) == "The min is 0"


def test_github_file_existence():
    name = "dani-jimlar" 
    repo = "djl_ind_project_1"  
    path_to_file = "source/bar_plot2.png"  
    url = f"https://api.github.com/repos/{name}/{repo}/contents/{path_to_file}"
    response1 = requests.get(url)
    assert response1.status_code == 200

if __name__ == "__main__":
    sel = pd.read_csv("source/imp_edos_2.csv", encoding="ISO-8859-1").iloc[:,3]
    test_github_file_existence()
    test_print_min(sel)    