import requests
import json

# acessa endereco raw do repositorio no github
url = 'https://raw.githubusercontent.com/rafaelcerqueira/resultados-matriculas-eja-json/main/'

class LeitorDeDados:
    def __init__(self):
        pass
    
    # dados da Bahia:
    def ler_dados_cor_raca_bahia(self, ano, nome_arquivo):
        response = requests.get(url + 'bahia/' + ano + '/' + nome_arquivo)
        dados = json.loads(response.text)
        dados = json.dumps(dados)
        
        return dados
    
    def ler_dados_faixa_etaria_bahia(self, ano, nome_arquivo):
        response = requests.get(url + 'bahia/' + ano + '/' + nome_arquivo)
        dados = json.loads(response.text)
        dados = json.dumps(dados)
        
        return dados
    
    def ler_dados_sexo_bahia(self, ano, nome_arquivo):
        response = requests.get(url + 'bahia/' + ano + '/' + nome_arquivo)
        dados = json.loads(response.text)
        
        # converte o tipo dict para json em 'dados'
        dados = json.dumps(dados)
        
        return dados
    
    # dados de Salvador:
    def ler_dados_cor_raca_salvador(self, ano, nome_arquivo):
        response = requests.get(url + 'salvador/' + ano + '/' + nome_arquivo)
        dados = json.loads(response.text)
        dados = json.dumps(dados)
        
        return dados
    
    def ler_dados_faixa_etaria_salvador(self, ano, nome_arquivo):
        response = requests.get(url + 'salvador/' + ano + '/' + nome_arquivo)
        dados = json.loads(response.text)
        dados = json.dumps(dados)
        
        return dados
    
    def ler_dados_sexo_salvador(self, ano, nome_arquivo):
        response = requests.get(url + 'salvador/' + ano + '/' + nome_arquivo)
        dados = json.loads(response.text)
        dados = json.dumps(dados)
        
        return dados
    

# instancia a classe

leitor = LeitorDeDados()
