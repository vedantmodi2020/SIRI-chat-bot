import requests
import webbrowser
import subprocess
from Constants import  App_name

def open_app(search_term):
    keys = App_name.keys()
    print(f"Opening the {search_term}")
    if search_term not in App_name.keys():
        webbrowser.open(search_term)
    else:
        subprocess.call(f'open -a {App_name.get(search_term)}',shell=True)

