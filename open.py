import requests
import webbrowser
import subprocess
from constants import  Constants

def open_app(search_term):
    keys = Constants.App_name.keys()
    print(f"Opening the {search_term}")
    if search_term not in Constants.App_name.keys():
        webbrowser.open(search_term)
    else:
        subprocess.call(f'open -a {Constants.App_name.get(search_term)}',shell=True)

