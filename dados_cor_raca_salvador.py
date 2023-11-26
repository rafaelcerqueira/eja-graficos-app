import plotly.express as px
import json
import pandas as pd

# importe a classe LeitorDeDados
from leitor_de_dados import LeitorDeDados
# instanca a classe
leitor = LeitorDeDados()

def carrega_dados_json(localidade, matriculas, ano):

    if localidade == 'Salvador' and matriculas == 'Por cor e raça':
        if ano == 2013:
            total_matriculas = leitor.ler_dados_cor_raca_salvador('dados_2013', 'dados_total_matriculas_por_raca_2013.json')
            percentual_total = leitor.ler_dados_cor_raca_salvador('dados_2013', 'dados_matriculas_raca_porcentagem_total_2013.json')
            total_dependencia_administrativa = leitor.ler_dados_cor_raca_salvador('dados_2013', 'dados_matriculas_dependencia_2013.json')
            percentual_dependencia_administrativa = leitor.ler_dados_cor_raca_salvador('dados_2013', 'dados_porcentagem_matriculas_dependencia_2013.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa

        elif ano == 2014:
            total_matriculas = leitor.ler_dados_cor_raca_salvador('dados_2014', 'dados_total_matriculas_por_raca_2014.json')
            percentual_total = leitor.ler_dados_cor_raca_salvador('dados_2014', 'dados_matriculas_raca_porcentagem_total_2014.json')
            total_dependencia_administrativa = leitor.ler_dados_cor_raca_salvador('dados_2014', 'dados_matriculas_dependencia_2014.json')
            percentual_dependencia_administrativa = leitor.ler_dados_cor_raca_salvador('dados_2014', 'dados_porcentagem_matriculas_dependencia_2014.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa
        elif ano == 2015:
            total_matriculas = leitor.ler_dados_cor_raca_salvador('dados_2015', 'dados_total_matriculas_por_raca_2015.json')
            percentual_total = leitor.ler_dados_cor_raca_salvador('dados_2015', 'dados_matriculas_raca_porcentagem_total_2015.json')
            total_dependencia_administrativa = leitor.ler_dados_cor_raca_salvador('dados_2015', 'dados_matriculas_dependencia_2015.json')
            percentual_dependencia_administrativa = leitor.ler_dados_cor_raca_salvador('dados_2015', 'dados_porcentagem_matriculas_dependencia_2015.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa
        elif ano == 2016:
            total_matriculas = leitor.ler_dados_cor_raca_salvador('dados_2016', 'dados_total_matriculas_por_raca_2016.json')
            percentual_total = leitor.ler_dados_cor_raca_salvador('dados_2016', 'dados_matriculas_raca_porcentagem_total_2016.json')
            total_dependencia_administrativa = leitor.ler_dados_cor_raca_salvador('dados_2016', 'dados_matriculas_dependencia_2016.json')
            percentual_dependencia_administrativa = leitor.ler_dados_cor_raca_salvador('dados_2016', 'dados_porcentagem_matriculas_dependencia_2016.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa
        elif ano == 2017:
            total_matriculas = leitor.ler_dados_cor_raca_salvador('dados_2017', 'dados_total_matriculas_por_raca_2017.json')
            percentual_total = leitor.ler_dados_cor_raca_salvador('dados_2017', 'dados_matriculas_raca_porcentagem_total_2017.json')
            total_dependencia_administrativa = leitor.ler_dados_cor_raca_salvador('dados_2017', 'dados_matriculas_dependencia_2017.json')
            percentual_dependencia_administrativa = leitor.ler_dados_cor_raca_salvador('dados_2017', 'dados_porcentagem_matriculas_dependencia_2017.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa
        elif ano == 2018:
            total_matriculas = leitor.ler_dados_cor_raca_salvador('dados_2018', 'dados_total_matriculas_por_raca_2018.json')
            percentual_total = leitor.ler_dados_cor_raca_salvador('dados_2018', 'dados_matriculas_raca_porcentagem_total_2018.json')
            total_dependencia_administrativa = leitor.ler_dados_cor_raca_salvador('dados_2018', 'dados_matriculas_dependencia_2018.json')
            percentual_dependencia_administrativa = leitor.ler_dados_cor_raca_salvador('dados_2018', 'dados_porcentagem_matriculas_dependencia_2018.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa
        elif ano == 2019:
            total_matriculas = leitor.ler_dados_cor_raca_salvador('dados_2019', 'dados_total_matriculas_por_raca_2019.json')
            percentual_total = leitor.ler_dados_cor_raca_salvador('dados_2019', 'dados_matriculas_raca_porcentagem_total_2019.json')
            total_dependencia_administrativa = leitor.ler_dados_cor_raca_salvador('dados_2019', 'dados_matriculas_dependencia_2019.json')
            percentual_dependencia_administrativa = leitor.ler_dados_cor_raca_salvador('dados_2019', 'dados_porcentagem_matriculas_dependencia_2019.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa
        elif ano == 2020:
            total_matriculas = leitor.ler_dados_cor_raca_salvador('dados_2020', 'dados_total_matriculas_por_raca_2020.json')
            percentual_total = leitor.ler_dados_cor_raca_salvador('dados_2020', 'dados_matriculas_raca_porcentagem_total_2020.json')
            total_dependencia_administrativa = leitor.ler_dados_cor_raca_salvador('dados_2020', 'dados_matriculas_dependencia_2020.json')
            percentual_dependencia_administrativa = leitor.ler_dados_cor_raca_salvador('dados_2020', 'dados_porcentagem_matriculas_dependencia_2020.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa
        elif ano == 2021:
            total_matriculas = leitor.ler_dados_cor_raca_salvador('dados_2021', 'dados_total_matriculas_por_raca_2021.json')
            percentual_total = leitor.ler_dados_cor_raca_salvador('dados_2021', 'dados_matriculas_raca_porcentagem_total_2021.json')
            total_dependencia_administrativa = leitor.ler_dados_cor_raca_salvador('dados_2021', 'dados_matriculas_dependencia_2021.json')
            percentual_dependencia_administrativa = leitor.ler_dados_cor_raca_salvador('dados_2021', 'dados_porcentagem_matriculas_dependencia_2021.json')

            return total_matriculas, percentual_total, total_dependencia_administrativa, percentual_dependencia_administrativa

        elif ano == 2022:
            total_matriculas = leitor.ler_dados_cor_raca_salvador('dados_2022', 'dados_total_matriculas_por_raca_2022.json')
            percentual_total = leitor.ler_dados_cor_raca_salvador('dados_2022', 'dados_matriculas_raca_porcentagem_total_2022.json')
            total_dependencia_administrativa = leitor.ler_dados_cor_raca_salvador('dados_2022', 'dados_matriculas_dependencia_2022.json')
            percentual_dependencia_administrativa = leitor.ler_dados_cor_raca_salvador('dados_2022', 'dados_porcentagem_matriculas_dependencia_2022.json')

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

    # fig2
    df_percentual_total = pd.DataFrame(percentual_total, index=[0])
    df_percentual_total = df_percentual_total.transpose().reset_index()
    df_percentual_total.columns = ['Cor e raça', 'Percentual']

    # fig3
    df_total_dependencia_administrativa = pd.DataFrame(total_dependencia_administrativa,).transpose()
    df_total_dependencia_administrativa = df_total_dependencia_administrativa.astype(int)

    # fig4
    df_percentual_dependencia_administrativa = pd.DataFrame(percentual_dependencia_administrativa).transpose()
    df_percentual_dependencia_administrativa = df_percentual_dependencia_administrativa.replace('%', '', regex=True).astype(float)

    # acessa os dados do DataFrame df_total_matriculas e retorna o somatório de todas as matrículas
    total_matriculas = df_total_matriculas['Total'].sum()

    # cria o gráfico de barras

    # exibe o total de matrículas junto ao título do gráfico

    fig = px.bar(df_total_matriculas, x='Cor e raça', y='Total', color='Cor e raça', title='Matrículas por Cor e Raça' + ' - Total: ' + str(total_matriculas))
    fig.update_layout(height=600, width=800)
    fig.update_traces(
        texttemplate='%{value}',  # Formatação sem casas decimais
        textposition='inside'  # Posição do texto dentro das barras
    )

    fig2 = px.bar(df_percentual_total, x='Cor e raça', y='Percentual', color='Cor e raça', title='Percentual Total de Matrículas por Cor e Raça')
    fig2.update_layout(height=600, width=800)
    fig2.update_traces(
        texttemplate='%{value}%',  # Formatação sem casas decimais
        textposition='inside'  # Posição do texto dentro das barras
    )

    fig3 = px.bar(
        df_total_dependencia_administrativa,
        x=['Branca', 'Preta', 'Parda', 'Amarela', 'Indígena', 'Não declarada'],
        y=['Estadual', 'Municipal', 'Privada', 'Federal'],
        color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA'],
        title='Total de Matrículas por Cor e Raça e Dependência Administrativa'
    )
    fig3.update_xaxes(title_text='Cor e Raça')
    fig3.update_yaxes(title_text='Dependência Administrativa')
    fig3.update_layout(
        height=600,
        width=800,
        hoverlabel=dict(bgcolor="#363e63", font_size=12, font_family="Rockwell"),
        legend_title_text='Legenda Personalizada',
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
        color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA'],
        title='Percentual de Matrículas por Cor e Raça e Dependência Administrativa'
    )
    fig4.update_xaxes(title_text='Cor e Raça')
    fig4.update_yaxes(title_text='Dependência Administrativa')
    fig4.update_layout(
        height=600,
        width=800,
        hoverlabel=dict(bgcolor="#363e63", font_size=12, font_family="Rockwell"),
        legend_title_text='Legenda Personalizada',
        legend=dict(title='Cor e raça')
    )
    # Ajustando os rótulos do hover
    fig4.update_traces(
        hovertemplate="Cor e Raça<br>Total=%{value}<br>Dep. Adm.=%{y}",
        texttemplate='%{value}%',
        textposition='inside'
    )

    return fig, fig2, fig3, fig4
