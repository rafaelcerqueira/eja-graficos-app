import requests
import json

# acessa endereco raw do repositorio no github
url = 'https://raw.githubusercontent.com/rafaelcerqueira/resultados-matriculas-eja-json/main/'

# response = requests.get(url + 'bahia/dados_2013/json_dados_percentual_total_por_sexo_2013.json')

# crie uma classe que contenha várias funções para ler os dados

class LeitorDeDados:
    def __init__(self):
        pass
    
    def ler_dados_sexo_percentual(self, uf, ano, nome_arquivo):
        response = requests.get(url + uf + '/' + ano + '/' + nome_arquivo)
        dados = json.loads(response.text)
        return dados
    
    def ler_dados_sexo_percentual_bahia(self, ano, nome_arquivo):
        response = requests.get(url + 'bahia/' + ano + '/' + nome_arquivo)
        dados = json.loads(response.text)
        
        # converta o tipo dict para json em 'dados'
        dados = json.dumps(dados)
        
        return dados

# instancie a classe

leitor = LeitorDeDados()
