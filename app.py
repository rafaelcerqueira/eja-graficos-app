import streamlit as st
import plotly.express as px
import json
import pandas as pd

from leitor_de_dados import LeitorDeDados

#Menu lateral
st.header("Dados de Matrículas da EJA na Bahia")

st.sidebar.title("Modalidade e Ano")

localidade = st.sidebar.radio("Localidade", ["Bahia", "Salvador"])

ano = st.sidebar.selectbox("Ano", [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
 
modalidade = st.sidebar.radio("Modalidade", ["Matrículas por cor e raça", "Matrículas por faixa etária", "Matrículas por sexo"])

if modalidade == "Matrículas por cor e raça":
    # exiba o radio button
    st.sidebar.selectbox("Cor e Raça", ["Total por dependência administrativa", "Percentual por dependência administrativa", "Percentual total", "Total de matrículas"])


# Acessa a classe LeitorDeDados
leitor = LeitorDeDados()


# se o usuário escolher a opção "Matrículas por sexo" e o ano de 2013, exiba o gráfico
# ano 2013 e modalidade "Matrículas por sexo"------------------------------------------
if modalidade == "Matrículas por sexo" and ano == 2013 and localidade == "Bahia":
    
    #----------------------------------------------------------------------------------
    # lê os dados de matrículas da Bahia
    dados_total_matriculas = leitor.ler_dados_sexo_bahia('dados_2013', 'dados_total_matriculas_por_sexo_2013.json')
    dados_percentual_total = leitor.ler_dados_sexo_bahia('dados_2013', 'json_dados_percentual_total_por_sexo_2013.json')
    dados_percentual_dependencia_administrativa = leitor.ler_dados_sexo_bahia('dados_2013', 'dados_percentual_por_sexo_dependencia_administrativa_2013.json')
    dados_total_matriculas_dep_adm = leitor.ler_dados_sexo_bahia('dados_2013', 'dados_matriculas_por_sexo_por_dependencia_administrativa_2013.json')
    
    #---------------------------------------------------------------------------------
    # lê arquivos json
    dados_percentual_total = json.loads(dados_percentual_total)
    dados_percentual_dependencia_administrativa = json.loads(dados_percentual_dependencia_administrativa)
    dados_total_matriculas_dep_adm = json.loads(dados_total_matriculas_dep_adm)
    dados_total_matriculas = json.loads(dados_total_matriculas)
        
    #---------------------------------------------------------------------------------
    # dataframe percentual total
    df_percentual_total = pd.DataFrame(dados_percentual_total, index=[0])
    df_percentual_total = df_percentual_total.transpose().reset_index()
    df_percentual_total.columns = ['sexo', 'total']
              
    # dataframe percentual dependência administrativa
    df_percentual_dependencia_administrativa = pd.DataFrame(dados_percentual_dependencia_administrativa).transpose()
    df_percentual_dependencia_administrativa = df_percentual_dependencia_administrativa.replace('%', '', regex=True).astype(float)
    

    # dataframe dados_total_matriculas_dep_adm e crie um dataframe
    df_total_matriculas_dep_adm = pd.DataFrame(dados_total_matriculas_dep_adm).transpose()
    df_total_matriculas_dep_adm = df_total_matriculas_dep_adm.astype(int)
    
    # dataframe dados_total_matriculas e crie um dataframe
    df_total_matriculas = pd.DataFrame(dados_total_matriculas, index=[0])
    df_total_matriculas = df_total_matriculas.transpose().reset_index()
    df_total_matriculas.columns = ['sexo', 'total']
    
    
    #---------------------------------------------------------------------------------
    # cria os gráficos
    
    # exibe o percentual total por sexo
    fig = px.bar(df_percentual_total, x='sexo', y='total', color='sexo', text='total', title='Percentual total de matrículas por sexo na Bahia em 2013')
    fig.update_layout(height=600, width=900)
    
    # exibe o percentual por dependência administrativa
    fig2 = px.bar(
        df_percentual_dependencia_administrativa,
        y=['Estadual', 'Federal', 'Municipal', 'Privada'],
        x=['Feminino', 'Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino'],
        barmode='stack',
        labels={'y': 'Dependência administrativa', 'x': 'Sexo', 'value': 'Percentual', 'color': 'Sexo'},
        title='Percentual por dependência administrativa na Bahia em 2013'
    )
    
    fig2.update_traces(texttemplate='%{value:.4s}', textposition='outside')
    fig2.update_layout(height=600, width=900)
    
    # exibe o total de matrículas por dependência administrativa
    fig3 = px.bar(
        df_total_matriculas_dep_adm,
        y=['Estadual', 'Municipal', 'Privada', 'Federal'],
        x=['Feminino', 'Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino'],
        labels={'x': 'Sexo', 'y': 'Dependência administrativa', 'value': 'Total de matrículas', 'color': 'Sexo'},
        barmode='stack',
        title='Total de matrículas por sexo e dependência administrativa na Bahia em 2013'
        )
    
    # exiba o total de matrículas por dependência administrativa dentro do gráfico
    fig3.update_traces(texttemplate='%{value:.3s}', textposition='outside')
    fig3.update_layout(height=600, width=900)
    
    # exibe o total de matrículas por sexo
    fig4 = px.bar(df_total_matriculas, x='sexo', y='total', color='sexo', text='total', title='Total de matrículas por sexo na Bahia em 2013')
    
    # exiba o total de matrículas por sexo dentro do gráfico
    fig4.update_traces(texttemplate='%{value:.3s}', textposition='outside')
    fig4.update_layout(height=600, width=900)
    
    #---------------------------------------------------------------------------------
    # renderiza o gráfico
    st.subheader("Percentual total por sexo na Bahia em 2013")
    st.plotly_chart(fig)
    st.subheader("Percentual por dependência administrativa na Bahia em 2013")
    st.plotly_chart(fig2)
    st.subheader("Total de matrículas por dependência administrativa na Bahia em 2013")
    st.plotly_chart(fig3)
    st.subheader("Total de matrículas por sexo na Bahia em 2013")
    st.plotly_chart(fig4)
    
    
elif modalidade == "Matrículas por sexo" and ano == 2013 and localidade == "Salvador":
    #----------------------------------------------------------------------------------
    # lê os dados de matrículas da Bahia
    dados_percentual_total = leitor.ler_dados_sexo_salvador('dados_2013', 'json_dados_percentual_total_por_sexo_2013.json')
    dados_percentual_dependencia_administrativa = leitor.ler_dados_sexo_salvador('dados_2013', 'dados_percentual_por_sexo_dependencia_administrativa_2013.json')
    dados_total_matriculas_dep_adm = leitor.ler_dados_sexo_salvador('dados_2013', 'dados_matriculas_por_sexo_por_dependencia_administrativa_2013.json')
    dados_total_matriculas = leitor.ler_dados_sexo_salvador('dados_2013', 'dados_total_matriculas_por_sexo_2013.json')
    
    
    #---------------------------------------------------------------------------------
    # lê arquivos json
    dados_percentual_total = json.loads(dados_percentual_total)
    dados_percentual_dependencia_administrativa = json.loads(dados_percentual_dependencia_administrativa)
    dados_total_matriculas_dep_adm = json.loads(dados_total_matriculas_dep_adm)
    dados_total_matriculas = json.loads(dados_total_matriculas)
        
    #---------------------------------------------------------------------------------
    # dataframe percentual total
    df_percentual_total = pd.DataFrame(dados_percentual_total, index=[0])
    df_percentual_total = df_percentual_total.transpose().reset_index()
    df_percentual_total.columns = ['sexo', 'total']
        
    # dataframe percentual dependência administrativa
    df_percentual_dependencia_administrativa = pd.DataFrame(dados_percentual_dependencia_administrativa).transpose()
    df_percentual_dependencia_administrativa = df_percentual_dependencia_administrativa.replace('%', '', regex=True).astype(float)
    
    # leia o arquivo dados_total_matriculas_dep_adm e crie um dataframe
    df_total_matriculas_dep_adm = pd.DataFrame(dados_total_matriculas_dep_adm).transpose()
    df_total_matriculas_dep_adm = df_total_matriculas_dep_adm.astype(int)
    
    # leia o arquivo dados_total_matriculas e crie um dataframe
    df_total_matriculas = pd.DataFrame(dados_total_matriculas, index=[0])
    df_total_matriculas = df_total_matriculas.transpose().reset_index()
    df_total_matriculas.columns = ['sexo', 'total']
    
    #---------------------------------------------------------------------------------
    # exibe o percentual total por sexo
    fig = px.bar(df_percentual_total, x='sexo', y='total', color='sexo', text='total', title='Percentual total de matrículas por sexo em Salvador em 2013')
    fig.update_layout(height=600, width=900)
    
    # exibe o percentual por dependência administrativa
    fig2 = px.bar(
        df_percentual_dependencia_administrativa,
        y=['Estadual', 'Federal', 'Municipal', 'Privada'],
        x=['Feminino', 'Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino'],
        barmode='stack',
        labels={'y': 'Dependência administrativa', 'x': 'Sexo', 'value': 'Percentual', 'color': 'Sexo'},
        title='Percentual por dependência administrativa em Salvador em 2013'
    )
    
    fig2.update_traces(texttemplate='%{value:.4s}', textposition='outside')
    fig2.update_layout(height=600, width=900)
    
    # exibe o total de matrículas por dependência administrativa
    fig3 = px.bar(
        df_total_matriculas_dep_adm,
        y=['Estadual', 'Municipal', 'Privada', 'Federal'],
        x=['Feminino', 'Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino'],
        labels={'x': 'Sexo', 'y': 'Dependência administrativa', 'value': 'Total de matrículas', 'color': 'Sexo'},
        barmode='stack',
        title='Total de matrículas por sexo e dependência administrativa em Salvador em 2013'
        )
    
    # exiba o total de matrículas por dependência administrativa dentro do gráfico
    fig3.update_traces(texttemplate='%{value:.3s}', textposition='outside')
    fig3.update_layout(height=600, width=900)
    
    fig4 = px.bar(df_total_matriculas, x='sexo', y='total', color='sexo', text='total', title='Total de matrículas por sexo em Salvador em 2013')
    
    fig4.update_traces(texttemplate='%{value:.3s}', textposition='outside')
    fig4.update_layout(height=600, width=900)   
    
    #---------------------------------------------------------------------------------
    # renderiza o gráfico
    st.subheader("Percentual total por sexo em Salvador em 2013")
    st.plotly_chart(fig)
    st.subheader("Percentual por dependência administrativa em Salvador em 2013")
    st.plotly_chart(fig2)
    st.subheader("Total de matrículas por dependência administrativa em Salvador em 2013")
    st.plotly_chart(fig3)
    st.subheader("Total de matrículas por sexo em Salvador em 2013")
    st.plotly_chart(fig4)