
import requests
from script import aggregate_statistics


def test_github_file_existence():
    name = "nogibjj" 
    repo = "IDS706_DataEngineering_BarbaraFlores_Project1"  
    path_to_file = "output/Total_applicants.png"  
    url = f"https://api.github.com/repos/{name}/{repo}/contents/{path_to_file}"
    
    response1 = requests.get(url)
    
    assert response1.status_code == 200