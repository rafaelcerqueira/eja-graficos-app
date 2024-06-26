import plotly.express as px
import pandas as pd
import json

from leitor_de_dados import LeitorDeDados
leitor = LeitorDeDados()

def carrega_dados_json(localidade, matriculas, ano):

    if localidade == 'Nordeste' and matriculas == 'Por cor e raça':
        if ano == 2013:
            total_matriculas = leitor.ler_dados_cor_raca_nordeste('dados_2013', 'total_matriculas_por_cor_raca.json')

            percentual_total = leitor.ler_dados_cor_raca_nordeste('dados_2013', 'matriculas_por_cor_raca_porcentagem_total.json')

            total_dependencia_administrativa = leitor.ler_dados_cor_raca_nordeste('dados_2013', 'matriculas_por_cor_raca.json')

            percentual_dependencia_administrativa = leitor.ler_dados_cor_raca_nordeste('dados_2013', 'porcentagem_matriculas_por_cor_raca.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa

        elif ano == 2017:
            total_matriculas = leitor.ler_dados_cor_raca_nordeste('dados_2017', 'total_matriculas_por_cor_raca.json')

            percentual_total = leitor.ler_dados_cor_raca_nordeste('dados_2017', 'matriculas_por_cor_raca_porcentagem_total.json')

            total_dependencia_administrativa = leitor.ler_dados_cor_raca_nordeste('dados_2017', 'matriculas_por_cor_raca.json')

            percentual_dependencia_administrativa = leitor.ler_dados_cor_raca_nordeste('dados_2017', 'porcentagem_matriculas_por_cor_raca.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa

        elif ano == 2022:
            total_matriculas = leitor.ler_dados_cor_raca_nordeste('dados_2022', 'total_matriculas_por_cor_raca.json')

            percentual_total = leitor.ler_dados_cor_raca_nordeste('dados_2022',
                                                                  'matriculas_por_cor_raca_porcentagem_total.json')

            total_dependencia_administrativa = leitor.ler_dados_cor_raca_nordeste('dados_2022',
                                                                                  'matriculas_por_cor_raca.json')

            percentual_dependencia_administrativa = leitor.ler_dados_cor_raca_nordeste('dados_2022',
                                                                                       'porcentagem_matriculas_por_cor_raca.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa


# Cria os gráficos:

def cria_graficos_cor_raca(localidade, matriculas, ano):
    localidade = localidade
    matriculas = matriculas
    ano = ano

    # Dados de Matrículas por Cor e Raça
    total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa = carrega_dados_json(matriculas=matriculas, localidade=localidade, ano=ano)[0], carrega_dados_json(matriculas=matriculas, localidade=localidade, ano=ano)[1], carrega_dados_json(matriculas=matriculas, localidade=localidade, ano=ano)[2], carrega_dados_json(matriculas=matriculas, localidade=localidade, ano=ano)[3]


    total_matriculas = json.loads(total_matriculas)
    percentual_total = json.loads(percentual_total)
    total_dependencia_administrativa = json.loads(total_dependencia_administrativa)
    percentual_dependencia_administrativa = json.loads(percentual_dependencia_administrativa)

    # DataFrame:
    # fig
    df_total_matriculas = pd.DataFrame(total_matriculas, index=[0])
    df_total_matriculas = df_total_matriculas.transpose().reset_index()
    df_total_matriculas.columns = ['Cor e raça', 'Total']

    # acessa os dados do DataFrame df_total_matriculas e retorna o somatório de todas as matrículas:
    total_matriculas = df_total_matriculas['Total'].sum()

    # fig2
    df_percentual_total = pd.DataFrame(percentual_total, index=[0])
    df_percentual_total = df_percentual_total.transpose().reset_index()
    df_percentual_total.columns = ['Cor e raça', 'Percentual']

    # fig3
    df_total_dependencia_administrativa = pd.DataFrame(total_dependencia_administrativa).transpose()
    df_total_dependencia_administrativa = df_total_dependencia_administrativa.astype(int)

    # fig4
    df_percentual_dependencia_administrativa = pd.DataFrame(percentual_dependencia_administrativa).transpose()
    df_percentual_dependencia_administrativa = df_percentual_dependencia_administrativa.replace('%', '', regex=True).astype(float)

    # cria o gráfico de barras
    fig = px.bar(
        df_total_matriculas,
        x='Cor e raça',
        y='Total',
        color='Cor e raça',
        color_discrete_sequence=['#FB8C00', '#F4511E', '#7CB342', '#00897B', '#F06292', '#78909C'],
        title='Matrículas por Cor e Raça' + ' - Total: ' + str(total_matriculas)
    )
    fig.update_layout(height=600, width=800)
    fig.update_traces(
        texttemplate='%{value}',
        textposition='inside'
    )

    fig2 = px.bar(
        df_percentual_total,
        x='Cor e raça',
        y='Percentual',
        color='Cor e raça',
        color_discrete_sequence=['#FB8C00', '#F4511E', '#7CB342', '#00897B', '#F06292', '#78909C'],
        title='Percentual Total de Matrículas por Cor e Raça'
    )
    fig2.update_layout(height=600, width=800)
    fig2.update_traces(
        texttemplate='%{value}%',
        textposition='inside'
    )

    fig3 = px.bar(
        df_total_dependencia_administrativa,
        x=['Branca', 'Preta', 'Parda', 'Amarela', 'Indígena', 'Não declarada'],
        y=['Estadual', 'Municipal', 'Privada', 'Federal'],
        color_discrete_sequence=['#FB8C00', '#F4511E', '#7CB342', '#00897B', '#F06292', '#78909C'],
        title='Total de Matrículas por Cor e Raça e Dependência Administrativa'
    )
    fig3.update_xaxes(title_text='Cor e Raça')
    fig3.update_yaxes(title_text='Dependência Administrativa')
    fig3.update_layout(
        height=600,
        width=800,
        hoverlabel=dict(bgcolor="#363e63", font_size=12, font_family="Rockwell"),
        legend=dict(title='Cor e raça')

    )
    # Ajustando os rótulos do hover
    fig3.update_traces(
        hovertemplate="Cor e Raça<br>Total=%{value}<br>Dep. Adm.=%{y}",
        texttemplate='%{value}',
        textposition='inside'

    )

    fig4 = px.bar(
        df_percentual_dependencia_administrativa,
        x=['Branca', 'Preta', 'Parda', 'Amarela', 'Indígena', 'Não declarada'],
        y=['Estadual', 'Municipal', 'Privada', 'Federal'],
        color_discrete_sequence=['#FB8C00', '#F4511E', '#7CB342', '#00897B', '#F06292', '#78909C'],
        title='Percentual de Matrículas por Cor e Raça e Dependência Administrativa'
    )
    fig4.update_xaxes(title_text='Cor e Raça')
    fig4.update_yaxes(title_text='Dependência Administrativa')
    fig4.update_layout(
        height=600,
        width=800,
        hoverlabel=dict(bgcolor="#363e63", font_size=12, font_family="Rockwell"),
        legend=dict(title='Cor e raça')

    )
    # Ajustando os rótulos do hover
    fig4.update_traces(
        hovertemplate="Cor e Raça<br>Total=%{value}<br>Dep. Adm.=%{y}",
        texttemplate='%{value}%',
        textposition='inside'
    )

    return fig, fig2, fig3, fig4
