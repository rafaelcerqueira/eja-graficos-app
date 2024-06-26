import plotly.express as px
import pandas as pd
import json

from leitor_de_dados import LeitorDeDados
leitor = LeitorDeDados()

def carrega_dados_json(localidade, matriculas, ano):

    if localidade == 'Nordeste' and matriculas == 'Por sexo':
        if ano == 2013:
            total_matriculas = leitor.ler_dados_sexo_nordeste('dados_2013', 'total_matriculas_por_sexo.json')

            percentual_total = leitor.ler_dados_sexo_nordeste('dados_2013', 'percentual_total_por_sexo.json')

            total_dependencia_administrativa = leitor.ler_dados_sexo_nordeste('dados_2013', 'matriculas_por_sexo_por_dependencia_administrativa.json')

            percentual_dependencia_administrativa = leitor.ler_dados_sexo_nordeste('dados_2013', 'percentual_por_sexo_dependencia_administrativa.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa

        elif ano == 2017:
            total_matriculas = leitor.ler_dados_sexo_nordeste('dados_2017', 'total_matriculas_por_sexo.json')

            percentual_total = leitor.ler_dados_sexo_nordeste('dados_2017', 'percentual_total_por_sexo.json')

            total_dependencia_administrativa = leitor.ler_dados_sexo_nordeste('dados_2017',
                                                                              'matriculas_por_sexo_por_dependencia_administrativa.json')

            percentual_dependencia_administrativa = leitor.ler_dados_sexo_nordeste('dados_2017',
                                                                                   'percentual_por_sexo_dependencia_administrativa.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa

        elif ano == 2022:
            total_matriculas = leitor.ler_dados_sexo_nordeste('dados_2022', 'total_matriculas_por_sexo.json')

            percentual_total = leitor.ler_dados_sexo_nordeste('dados_2022', 'percentual_total_por_sexo.json')

            total_dependencia_administrativa = leitor.ler_dados_sexo_nordeste('dados_2022',
                                                                              'matriculas_por_sexo_por_dependencia_administrativa.json')

            percentual_dependencia_administrativa = leitor.ler_dados_sexo_nordeste('dados_2022',
                                                                                   'percentual_por_sexo_dependencia_administrativa.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa
        else:
            'Ainda não há dados para este ano.'


def cria_grafico_matriculas_por_sexo(localidade, matriculas, ano):
    localidade = localidade
    matriculas = matriculas
    ano = ano

    total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa = carrega_dados_json(localidade=localidade, matriculas=matriculas, ano=ano)[0], carrega_dados_json(localidade=localidade, matriculas=matriculas, ano=ano)[1], carrega_dados_json(localidade=localidade, matriculas=matriculas, ano=ano)[2], carrega_dados_json(localidade=localidade, matriculas=matriculas, ano=ano)[3]

    total_matriculas = json.loads(total_matriculas)
    percentual_total = json.loads(percentual_total)
    total_dependencia_administrativa = json.loads(total_dependencia_administrativa)
    percentual_dependencia_administrativa = json.loads(percentual_dependencia_administrativa)

    #fig
    df_total_matriculas = pd.DataFrame(total_matriculas, index=[0])
    df_total_matriculas = df_total_matriculas.transpose().reset_index()
    df_total_matriculas.columns = ['Sexo', 'Total de Matrículas']

    #fig2
    df_percentual_total = pd.DataFrame(percentual_total, index=[0])
    df_percentual_total = df_percentual_total.transpose().reset_index()
    df_percentual_total.columns = ['Sexo', 'Percentual']

    #fig3
    df_total_dependencia_administrativa = pd.DataFrame(total_dependencia_administrativa).transpose()
    df_total_dependencia_administrativa = df_total_dependencia_administrativa.astype(int)

    #fig4
    df_percentual_dependencia_administrativa = pd.DataFrame(percentual_dependencia_administrativa).transpose()
    df_percentual_dependencia_administrativa = df_percentual_dependencia_administrativa.replace('%', '', regex=True).astype(float)

    # somatorio:
    total_matriculas = df_total_matriculas['Total de Matrículas'].sum()

    # acessa do dataframe df_percentual_dependencia_administrativa e pega o valor da primeira linha e segunda e terceira coluna
    # que é o total de matrículas por sexo e dependência administrativa
    total_matriculas_estadual = df_total_dependencia_administrativa.iloc[0, 1]


    fig = px.bar(
        df_total_matriculas,
        x='Sexo',
        y='Total de Matrículas',
        color='Sexo',
        text='Total de Matrículas',
        title=f'Matrículas por Sexo' + ' - ' + f'Total: {total_matriculas}'
    )
    fig.update_traces(texttemplate='%{text:.3s}', textposition='inside')
    fig.update_layout(height=600, width=800)

    fig2 = px.bar(
        df_percentual_total,
        x='Sexo',
        y='Percentual',
        color='Sexo',
        text='Percentual',
        title='Percentual de Matrículas por Sexo'
    )
    fig.update_layout(height=600, width=800)
    fig2.update_traces(texttemplate='%{value}%', textposition='inside')

    fig3 = px.bar(
        df_total_dependencia_administrativa,
        x=['Feminino', 'Masculino'],
        y=['Estadual', 'Municipal', 'Privada', 'Federal'],
        title='Matrículas por Sexo e Dependência Administrativa'
    )

    fig3.update_layout(
        height=600,
        width=800,
        hoverlabel=dict(bgcolor="#363e63", font_size=12, font_family="Rockwell"),
        legend=dict(title='Sexo')
    )
    fig3.update_xaxes(title_text='Sexo')
    fig3.update_yaxes(title_text='Dependência Administrativa')
    fig3.update_traces(
        hovertemplate="Sexo <br> Total=%{value} <br> Dependência Administrativa=%{y}",
        texttemplate='%{value}',
        textposition='inside'
    )

    fig4 = px.bar(
        df_percentual_dependencia_administrativa,
        x=['Feminino', 'Masculino'],
        y=['Estadual', 'Municipal', 'Privada', 'Federal'],
        title='Percentual de Matrículas por Sexo e Dependência Administrativa',
        labels={'x': 'Sexo', 'y': 'Dependência administrativa', 'value': 'Total de matrículas', 'color': 'Sexo'},
    )
    fig4.update_layout(
        height=600,
        width=800,
        hoverlabel=dict(bgcolor="#363e63", font_size=12, font_family="Rockwell"),
        legend=dict(title='Sexo')

    )
    fig4.update_xaxes(title_text='Sexo')
    fig4.update_yaxes(title_text='Dependência Administrativa')
    fig4.update_traces(
        hovertemplate="Sexo <br> Percentual=%{value}% <br> Dependência Administrativa=%{y}",
        texttemplate='%{value}%',
        textposition='inside',

    )

    return fig, fig2, fig3, fig4