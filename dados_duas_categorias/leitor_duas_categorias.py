import requests
import pandas as pd

urlBahia = 'https://raw.githubusercontent.com/rafaelcerqueira/dados-eja-matriculas/main/Bahia'
urlSalvador = 'https://raw.githubusercontent.com/rafaelcerqueira/dados-eja-matriculas/main/Salvador'


class LeitorDuasCategorias:
    def __init__(self, df):
        self.df = df

    def get_dados_cor_raca_sexo_bahia(self, ano):

        ano = str(ano)
        df_cor_raca_sexo = pd.read_csv(urlBahia + '/dados-' + ano + '/duas-categorias/cor-raca-sexo-' + ano + '.csv', sep=';')

        return df_cor_raca_sexo

    def get_dados_faixa_etaria_sexo_bahia(self, ano):

        ano = str(ano)
        df_faixa_etaria_sexo = pd.read_csv(urlBahia + '/dados-' + ano + '/duas-categorias/faixa-etaria-sexo-' + ano + '.csv', sep=';')

        return df_faixa_etaria_sexo

    def get_dados_cor_raca_sexo_salvador(self, ano):
        ano = str(ano)
        df_cor_raca_sexo = pd.read_csv(urlSalvador + '/dados-' + ano + '/duas-categorias/cor-raca-sexo-' + ano + '.csv', sep=';')

        return df_cor_raca_sexo

    def get_dados_faixa_etaria_sexo_salvador(self, ano):
        ano = str(ano)
        df_faixa_etaria_sexo = pd.read_csv(urlSalvador + '/dados-' + ano + '/duas-categorias/faixa-etaria-sexo-' + ano + '.csv', sep=';')

        return df_faixa_etaria_sexo
