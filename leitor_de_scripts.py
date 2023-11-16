import pandas as pd
import json
import requests
# crie um leitor de scripts que acessa raw github

# https://github.com/rafaelcerqueira/dados-matriculas-eja/tree/main/dados-censo-educacao

url_raw = 'https://raw.githubusercontent.com/rafaelcerqueira/dados-matriculas-eja/main/dados-censo-educacao/'

class LeitorDeScripts:

    def __init__(self, url_raw):
        self.url = url_raw
    
    def le_script(self, local, ano, script):
        url = self.url + local + '/dados-' + ano +'/' + script
        r = requests.get(url)
        # return r.text
        
        return r.content.json()
        
    

leitor = LeitorDeScripts(url_raw).le_script('Bahia', '2013', 'matriculas_por_sexo.py' )

print(leitor)