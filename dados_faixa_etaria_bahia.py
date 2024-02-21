import plotly.express as px
import pandas as pd
import json

from leitor_de_dados import LeitorDeDados

leitor = LeitorDeDados()

def carrega_dados_json(localidade, matriculas, ano):

    if localidade == 'Bahia' and matriculas == 'Por faixa etária':
        if ano == 2013:
            total_matriculas = leitor.ler_dados_faixa_etaria_bahia('dados_2013', 'dados_total_matriculas_faixa_etaria_2013.json')
            percentual_total = leitor.ler_dados_faixa_etaria_bahia('dados_2013', 'dados_percentual_matriculas_faixa_etaria_2013.json')
            total_dependencia_administrativa = leitor.ler_dados_faixa_etaria_bahia('dados_2013', 'dados_matriculas_faixa_etaria_dependencia_administrativa_2013.json')
            percentual_dependencia_administrativa = leitor.ler_dados_faixa_etaria_bahia('dados_2013', 'dados_percentual_matriculas_faixa_etaria_dependencia_adm_2013.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa

        elif ano == 2014:
            total_matriculas = leitor.ler_dados_faixa_etaria_bahia('dados_2014', 'dados_total_matriculas_faixa_etaria_2014.json')
            percentual_total = leitor.ler_dados_faixa_etaria_bahia('dados_2014', 'dados_percentual_matriculas_faixa_etaria_2014.json')
            total_dependencia_administrativa = leitor.ler_dados_faixa_etaria_bahia('dados_2014', 'dados_matriculas_faixa_etaria_dependencia_administrativa_2014.json')
            percentual_dependencia_administrativa = leitor.ler_dados_faixa_etaria_bahia('dados_2014', 'dados_percentual_matriculas_faixa_etaria_dependencia_adm_2014.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa

        elif ano == 2015:
            total_matriculas = leitor.ler_dados_faixa_etaria_bahia('dados_2015', 'dados_total_matriculas_faixa_etaria_2015.json')
            percentual_total = leitor.ler_dados_faixa_etaria_bahia('dados_2015', 'dados_percentual_matriculas_faixa_etaria_2015.json')
            total_dependencia_administrativa = leitor.ler_dados_faixa_etaria_bahia('dados_2015', 'dados_matriculas_faixa_etaria_dependencia_administrativa_2015.json')
            percentual_dependencia_administrativa = leitor.ler_dados_faixa_etaria_bahia('dados_2015', 'dados_percentual_matriculas_faixa_etaria_dependencia_adm_2015.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa

        elif ano == 2016:
            total_matriculas = leitor.ler_dados_faixa_etaria_bahia('dados_2016',
                                                                   'dados_total_matriculas_faixa_etaria_2016.json')
            percentual_total = leitor.ler_dados_faixa_etaria_bahia('dados_2016',
                                                                   'dados_percentual_matriculas_faixa_etaria_2016.json')
            total_dependencia_administrativa = leitor.ler_dados_faixa_etaria_bahia('dados_2016',
                                                                                   'dados_matriculas_faixa_etaria_dependencia_administrativa_2016.json')
            percentual_dependencia_administrativa = leitor.ler_dados_faixa_etaria_bahia('dados_2016',
                                                                                        'dados_percentual_matriculas_faixa_etaria_dependencia_adm_2016.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa

        elif ano == 2017:
            total_matriculas = leitor.ler_dados_faixa_etaria_bahia('dados_2017',
                                                                   'dados_total_matriculas_faixa_etaria_2017.json')
            percentual_total = leitor.ler_dados_faixa_etaria_bahia('dados_2017',
                                                                   'dados_percentual_matriculas_faixa_etaria_2017.json')
            total_dependencia_administrativa = leitor.ler_dados_faixa_etaria_bahia('dados_2017',
                                                                                   'dados_matriculas_faixa_etaria_dependencia_administrativa_2017.json')
            percentual_dependencia_administrativa = leitor.ler_dados_faixa_etaria_bahia('dados_2017',
                                                                                        'dados_percentual_matriculas_faixa_etaria_dependencia_adm_2017.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa

        elif ano == 2018:
            total_matriculas = leitor.ler_dados_faixa_etaria_bahia('dados_2018',
                                                                   'dados_total_matriculas_faixa_etaria_2018.json')
            percentual_total = leitor.ler_dados_faixa_etaria_bahia('dados_2018',
                                                                   'dados_percentual_matriculas_faixa_etaria_2018.json')
            total_dependencia_administrativa = leitor.ler_dados_faixa_etaria_bahia('dados_2018',
                                                                                   'dados_matriculas_faixa_etaria_dependencia_administrativa_2018.json')
            percentual_dependencia_administrativa = leitor.ler_dados_faixa_etaria_bahia('dados_2018',
                                                                                        'dados_percentual_matriculas_faixa_etaria_dependencia_adm_2018.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa

        elif ano == 2019:
            total_matriculas = leitor.ler_dados_faixa_etaria_bahia('dados_2019',
                                                                   'dados_total_matriculas_faixa_etaria_2019.json')
            percentual_total = leitor.ler_dados_faixa_etaria_bahia('dados_2019',
                                                                   'dados_percentual_matriculas_faixa_etaria_2019.json')
            total_dependencia_administrativa = leitor.ler_dados_faixa_etaria_bahia('dados_2019',
                                                                                   'dados_matriculas_faixa_etaria_dependencia_administrativa_2019.json')
            percentual_dependencia_administrativa = leitor.ler_dados_faixa_etaria_bahia('dados_2019',
                                                                                        'dados_percentual_matriculas_faixa_etaria_dependencia_adm_2019.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa

        elif ano == 2020:
            total_matriculas = leitor.ler_dados_faixa_etaria_bahia('dados_2020',
                                                                   'dados_total_matriculas_faixa_etaria_2020.json')
            percentual_total = leitor.ler_dados_faixa_etaria_bahia('dados_2020',
                                                                   'dados_percentual_matriculas_faixa_etaria_2020.json')
            total_dependencia_administrativa = leitor.ler_dados_faixa_etaria_bahia('dados_2020',
                                                                                   'dados_matriculas_faixa_etaria_dependencia_administrativa_2020.json')
            percentual_dependencia_administrativa = leitor.ler_dados_faixa_etaria_bahia('dados_2020',
                                                                                        'dados_percentual_matriculas_faixa_etaria_dependencia_adm_2020.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa

        elif ano == 2021:
            total_matriculas = leitor.ler_dados_faixa_etaria_bahia('dados_2021', 'dados_total_matriculas_faixa_etaria_2021.json')
            percentual_total = leitor.ler_dados_faixa_etaria_bahia('dados_2021', 'dados_percentual_matriculas_faixa_etaria_2021.json')
            total_dependencia_administrativa = leitor.ler_dados_faixa_etaria_bahia('dados_2021', 'dados_matriculas_faixa_etaria_dependencia_administrativa_2021.json')
            percentual_dependencia_administrativa = leitor.ler_dados_faixa_etaria_bahia('dados_2021', 'dados_percentual_matriculas_faixa_etaria_dependencia_adm_2021.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa

        elif ano == 2022:
            total_matriculas = leitor.ler_dados_faixa_etaria_bahia('dados_2022',
                                                                   'dados_total_matriculas_faixa_etaria_2022.json')
            percentual_total = leitor.ler_dados_faixa_etaria_bahia('dados_2022',
                                                                   'dados_percentual_matriculas_faixa_etaria_2022.json')
            total_dependencia_administrativa = leitor.ler_dados_faixa_etaria_bahia('dados_2022',
                                                                                   'dados_matriculas_faixa_etaria_dependencia_administrativa_2022.json')
            percentual_dependencia_administrativa = leitor.ler_dados_faixa_etaria_bahia('dados_2022',
                                                                                        'dados_percentual_matriculas_faixa_etaria_dependencia_adm_2022.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa


def cria_graficos_faixa_etaria(localidade, matriculas, ano):
    localidade = localidade
    matriculas = matriculas
    ano = ano

    total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa = carrega_dados_json(localidade=localidade, matriculas=matriculas, ano=ano)[0], carrega_dados_json(localidade=localidade, matriculas=matriculas, ano=ano)[1], carrega_dados_json(localidade=localidade, matriculas=matriculas, ano=ano)[2], carrega_dados_json(localidade=localidade, matriculas=matriculas, ano=ano)[3]

    total_matriculas = json.loads(total_matriculas)
    percentual_total = json.loads(percentual_total)
    total_dependencia_administrativa = json.loads(total_dependencia_administrativa)
    percentual_dependencia_administrativa = json.loads(percentual_dependencia_administrativa)

    # fig
    df_total_matriculas = pd.DataFrame(total_matriculas, index=[0])
    df_total_matriculas = df_total_matriculas.transpose().reset_index()
    df_total_matriculas.columns = ['Faixa etária', 'Total de matrículas']
    total_matriculas = df_total_matriculas['Total de matrículas'].sum()

    # fig2
    df_percentual_total = pd.DataFrame(percentual_total, index=[0])
    df_percentual_total = df_percentual_total.transpose().reset_index()
    df_percentual_total.columns = ['Faixa etária', 'Percentual de matrículas']


    # fig3
    df_total_dependencia_administrativa = pd.DataFrame(total_dependencia_administrativa).transpose()
    df_total_dependencia_administrativa = df_total_dependencia_administrativa.astype(int)

    # fig4
    df_percentual_dependencia_administrativa = pd.DataFrame(percentual_dependencia_administrativa).transpose()
    df_percentual_dependencia_administrativa = df_percentual_dependencia_administrativa.replace('%', '', regex=True).astype(float)

    # cria um gráfico de acordo com os dados do dataframe df_total_matriculas
    fig = px.bar(
        df_total_matriculas,
        x='Faixa etária',
        y='Total de matrículas',
        color='Faixa etária',
        title=f'Matrículas por Faixa Etária - Total: {total_matriculas}',


    )
    fig.update_layout(height=600, width=800)
    fig.update_traces(
        texttemplate='%{value}',
        textposition='inside'
    )

    fig2 = px.bar(
        df_percentual_total,
        x='Faixa etária',
        y='Percentual de matrículas',
        color='Faixa etária',
        title=f'Percentual de Matrículas por Faixa Etária',
    )
    fig2.update_layout(height=600, width=800)
    fig2.update_traces(
        texttemplate='%{value}%',
        textposition='inside'
    )

    fig3 = px.bar(
        df_total_dependencia_administrativa,
        x=['15 a 17 anos', '18 a 19 anos', '20 a 24 anos', '25 a 29 anos', '30 a 34 anos', '35 a 39 anos', '40 anos ou mais', 'Até 14 anos'],
        y=['Estadual', 'Municipal', 'Privada', 'Federal'],

        title=f'Matrículas por Faixa Etária - Dependência Administrativa',
    )
    fig3.update_xaxes(title_text='Faixa etária')
    fig3.update_yaxes(title_text='Dependência Administrativa')
    fig3.update_layout(
        height=600,
        width=800,
        hoverlabel=dict(
            bgcolor="#363e63",
            font_size=12,
            font_family="Rockwell"
        ),
        legend=dict(title='Faixa etária')
    )
    fig3.update_traces(
        hovertemplate='Faixa etária: <br>Matrículas: %{value} <br>Dependência Administrativa: %{y}',
        texttemplate='%{value}',
        textposition='inside'
    )


    fig4 = px.bar(
        df_percentual_dependencia_administrativa,
        x=['15 a 17 anos', '18 a 19 anos', '20 a 24 anos', '25 a 29 anos', '30 a 34 anos', '35 a 39 anos', '40 anos ou mais', 'Até 14 anos'],
        y=['Estadual', 'Municipal', 'Privada', 'Federal'],

        title=f'Percentual de Matrículas por Faixa Etária - Dependência Administrativa',
    )
    fig4.update_xaxes(title_text='Faixa etária')
    fig4.update_yaxes(title_text='Dependência Administrativa')
    fig4.update_layout(
        height=600,
        width=800,
        hoverlabel=dict(
            bgcolor="#363e63",
            font_size=12,
            font_family="Rockwell"
        ),
        legend=dict(title='Faixa etária')
    )
    fig4.update_traces(
        hovertemplate='Faixa etária: <br>Matrículas: %{value} <br>Dependência Administrativa: %{y}',
        texttemplate='%{value}%',
        textposition='inside'
    )

    return fig, fig2, fig3, fig4

