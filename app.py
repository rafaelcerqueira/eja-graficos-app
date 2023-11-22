import streamlit as st
import plotly.express as px
import json
import pandas as pd

from leitor_de_dados import LeitorDeDados

#Menu lateral
st.header("Dados de Matrículas da EJA na Bahia")

st.sidebar.title("Modalidade e Ano")

modalidade = st.sidebar.radio("Modalidade", ["Matrículas por cor e raça", "Matrículas por faixa etária", "Matrículas por sexo"])
ano_bahia = st.sidebar.selectbox("Bahia", [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
ano_salvador = st.sidebar.selectbox("Salvador", [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])

# Acessa a classe LeitorDeDados
leitor = LeitorDeDados()


# se o usuário escolher a opção "Matrículas por sexo" e o ano de 2013, exiba o gráfico
if modalidade == "Matrículas por sexo" and ano_bahia == 2013:
    # lê os dados de matrículas da Bahia
    dados = leitor.ler_dados_sexo_percentual_bahia('dados_2013', 'json_dados_percentual_total_por_sexo_2013.json')

    dados = json.loads(dados)

    # cria um dataframe com os dados
    df = pd.DataFrame(dados, index=[0])
    df = df.transpose().reset_index()
    df.columns = ['sexo', 'total']

    # exiba o valor da porcentagem no gráfico
    fig = px.bar(df, x='sexo', y='total', color='sexo', text='total')

    # exiba o gráfico
    # exiba um subtitulo no gráfico
    st.subheader("Percentual total por sexo na Bahia em 2013")
    st.plotly_chart(fig)

else:
    #exiba um Hello World
    st.write("Hello World")