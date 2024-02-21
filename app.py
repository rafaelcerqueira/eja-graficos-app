import streamlit as st

# icone da página
st.set_page_config(
    page_title='Matrículas da Educação de Jovens e Adultos (EJA) na Bahia',
    page_icon=':books:'
)

# Header
st.header('Dados de Matrículas da Educação de Jovens e Adultos (EJA) na Bahia')

# Menu Lateral
st.sidebar.title('Menu')
st.sidebar.header('Selecione a opção desejada:')
localidade = st.sidebar.selectbox('Localidade', ('Bahia', 'Salvador'))
matriculas = st.sidebar.radio('Matrículas', ('Por cor e raça', 'Por faixa etária', 'Por sexo'))

if matriculas == 'Por sexo':
    categorias = st.sidebar.selectbox('Selecione a categoria:', ('Total', 'Cor e raça', 'Faixa etária'))

ano = st.sidebar.selectbox('Ano', (2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022))

# Texto introdutório
st.sidebar.markdown('''Este aplicativo tem como objetivo apresentar os dados de matrículas da Educação de Jovens e Adultos (EJA) na Bahia.''')

st.sidebar.markdown('''Todos os dados foram obtidos através do site do [Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP)](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/inep-data/estatisticas-censo-escolar).''')

# Renderiza os gráficos:
# Bahia: ------------------------------------
if localidade == 'Bahia':
    if ano == 2013:
        if matriculas == 'Por cor e raça':
            from dados_cor_raca_bahia import cria_graficos_cor_raca
            grafico_cor_raca_bahia = cria_graficos_cor_raca(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Cor e Raça em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_cor_raca_bahia[i])

        elif matriculas == 'Por faixa etária':
            from dados_faixa_etaria_bahia import cria_graficos_faixa_etaria
            grafico_faixa_etaria_bahia = cria_graficos_faixa_etaria(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Faixa Etária em ' + str(ano) + ' - ' + localidade)
            for i in range(len(grafico_faixa_etaria_bahia)):
                st.plotly_chart(grafico_faixa_etaria_bahia[i])

        elif matriculas == 'Por sexo':
            if categorias == 'Total':
                from dados_por_sexo_bahia import cria_grafico_matriculas_por_sexo
                grafico_matriculas_por_sexo = cria_grafico_matriculas_por_sexo(localidade=localidade, matriculas=matriculas, ano=ano)
                st.subheader('Matrículas por Sexo em ' + str(ano) + ' - ' + localidade)
                for i in range(4):
                    st.plotly_chart(grafico_matriculas_por_sexo[i])
            elif categorias == 'Cor e raça':
                'Ainda não há dados para cor e raça.'
            elif categorias == 'Faixa etária':
                'Ainda não há dados para faixa etária.'
        else:
            'Ainda não há dados para este ano.'
    elif ano == 2014:
        if matriculas == 'Por cor e raça':
            from dados_cor_raca_bahia import cria_graficos_cor_raca
            grafico_cor_raca_bahia = cria_graficos_cor_raca(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Cor e Raça em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_cor_raca_bahia[i])

        elif matriculas == 'Por faixa etária':
            from dados_faixa_etaria_bahia import cria_graficos_faixa_etaria
            grafico_faixa_etaria_bahia = cria_graficos_faixa_etaria(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Faixa Etária em ' + str(ano) + ' - ' + localidade)
            for i in range(len(grafico_faixa_etaria_bahia)):
                st.plotly_chart(grafico_faixa_etaria_bahia[i])

        elif matriculas == 'Por sexo':
            if categorias == 'Total':
                from dados_por_sexo_bahia import cria_grafico_matriculas_por_sexo
                grafico_matriculas_por_sexo = cria_grafico_matriculas_por_sexo(localidade=localidade, matriculas=matriculas, ano=ano)
                st.subheader('Matrículas por Sexo em ' + str(ano) + ' - ' + localidade)
                for i in range(4):
                    st.plotly_chart(grafico_matriculas_por_sexo[i])
            elif categorias == 'Cor e raça':
                'Ainda não há dados para cor e raça.'
            elif categorias == 'Faixa etária':
                'Ainda não há dados para faixa etária.'
        else:
            'Ainda não há dados para este ano.'
    elif ano == 2015:
        if matriculas == 'Por cor e raça':
            from dados_cor_raca_bahia import cria_graficos_cor_raca
            grafico_cor_raca_bahia = cria_graficos_cor_raca(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Cor e Raça em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_cor_raca_bahia[i])

        elif matriculas == 'Por faixa etária':
            from dados_faixa_etaria_bahia import cria_graficos_faixa_etaria
            grafico_faixa_etaria_bahia = cria_graficos_faixa_etaria(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Faixa Etária em ' + str(ano) + ' - ' + localidade)
            for i in range(len(grafico_faixa_etaria_bahia)):
                st.plotly_chart(grafico_faixa_etaria_bahia[i])

        elif matriculas == 'Por sexo':
            from dados_por_sexo_bahia import cria_grafico_matriculas_por_sexo
            grafico_matriculas_por_sexo = cria_grafico_matriculas_por_sexo(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Sexo em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_matriculas_por_sexo[i])
        else:
            'Ainda não há dados para este ano.'
    elif ano == 2016:
        if matriculas == 'Por cor e raça':
            from dados_cor_raca_bahia import cria_graficos_cor_raca
            grafico_cor_raca_bahia = cria_graficos_cor_raca(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Cor e Raça em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_cor_raca_bahia[i])

        elif matriculas == 'Por faixa etária':
            from dados_faixa_etaria_bahia import cria_graficos_faixa_etaria
            grafico_faixa_etaria_bahia = cria_graficos_faixa_etaria(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Faixa Etária em ' + str(ano) + ' - ' + localidade)
            for i in range(len(grafico_faixa_etaria_bahia)):
                st.plotly_chart(grafico_faixa_etaria_bahia[i])

        elif matriculas == 'Por sexo':
            from dados_por_sexo_bahia import cria_grafico_matriculas_por_sexo
            grafico_matriculas_por_sexo = cria_grafico_matriculas_por_sexo(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Sexo em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_matriculas_por_sexo[i])
        else:
            'Ainda não há dados para este ano.'
    elif ano == 2017:
        if matriculas == 'Por cor e raça':
            from dados_cor_raca_bahia import cria_graficos_cor_raca
            grafico_cor_raca_bahia = cria_graficos_cor_raca(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Cor e Raça em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_cor_raca_bahia[i])

        elif matriculas == 'Por faixa etária':
            from dados_faixa_etaria_bahia import cria_graficos_faixa_etaria
            grafico_faixa_etaria_bahia = cria_graficos_faixa_etaria(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Faixa Etária em ' + str(ano) + ' - ' + localidade)
            for i in range(len(grafico_faixa_etaria_bahia)):
                st.plotly_chart(grafico_faixa_etaria_bahia[i])

        elif matriculas == 'Por sexo':
            from dados_por_sexo_bahia import cria_grafico_matriculas_por_sexo
            grafico_matriculas_por_sexo = cria_grafico_matriculas_por_sexo(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Sexo em ' + str(ano) + ' - ' + localidade)
            for i in range(3):
                st.plotly_chart(grafico_matriculas_por_sexo[i])
        else:
            'Ainda não há dados para este ano.'
    elif ano == 2018:
        if matriculas == 'Por cor e raça':
            from dados_cor_raca_bahia import cria_graficos_cor_raca
            grafico_cor_raca_bahia = cria_graficos_cor_raca(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Cor e Raça em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_cor_raca_bahia[i])

        elif matriculas == 'Por faixa etária':
            from dados_faixa_etaria_bahia import cria_graficos_faixa_etaria
            grafico_faixa_etaria_bahia = cria_graficos_faixa_etaria(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Faixa Etária em ' + str(ano) + ' - ' + localidade)
            for i in range(len(grafico_faixa_etaria_bahia)):
                st.plotly_chart(grafico_faixa_etaria_bahia[i])

        elif matriculas == 'Por sexo':
            from dados_por_sexo_bahia import cria_grafico_matriculas_por_sexo
            grafico_matriculas_por_sexo = cria_grafico_matriculas_por_sexo(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Sexo em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_matriculas_por_sexo[i])
        else:
            'Ainda não há dados para este ano.'
    elif ano == 2019:
        if matriculas == 'Por cor e raça':
            from dados_cor_raca_bahia import cria_graficos_cor_raca
            grafico_cor_raca_bahia = cria_graficos_cor_raca(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Cor e Raça em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_cor_raca_bahia[i])

        elif matriculas == 'Por faixa etária':
            from dados_faixa_etaria_bahia import cria_graficos_faixa_etaria
            grafico_faixa_etaria_bahia = cria_graficos_faixa_etaria(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Faixa Etária em ' + str(ano) + ' - ' + localidade)
            for i in range(len(grafico_faixa_etaria_bahia)):
                st.plotly_chart(grafico_faixa_etaria_bahia[i])

        elif matriculas == 'Por sexo':
            from dados_por_sexo_bahia import cria_grafico_matriculas_por_sexo
            grafico_matriculas_por_sexo = cria_grafico_matriculas_por_sexo(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Sexo em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_matriculas_por_sexo[i])
        else:
            'Ainda não há dados para este ano.'
    elif ano == 2020:
        if matriculas == 'Por cor e raça':
            from dados_cor_raca_bahia import cria_graficos_cor_raca
            grafico_cor_raca_bahia = cria_graficos_cor_raca(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Cor e Raça em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_cor_raca_bahia[i])

        elif matriculas == 'Por faixa etária':
            from dados_faixa_etaria_bahia import cria_graficos_faixa_etaria
            grafico_faixa_etaria_bahia = cria_graficos_faixa_etaria(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Faixa Etária em ' + str(ano) + ' - ' + localidade)
            for i in range(len(grafico_faixa_etaria_bahia)):
                st.plotly_chart(grafico_faixa_etaria_bahia[i])

        elif matriculas == 'Por sexo':
            from dados_por_sexo_bahia import cria_grafico_matriculas_por_sexo
            grafico_matriculas_por_sexo = cria_grafico_matriculas_por_sexo(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Sexo em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_matriculas_por_sexo[i])
        else:
            'Ainda não há dados para este ano.'
    elif ano == 2021:
        if matriculas == 'Por cor e raça':
            from dados_cor_raca_bahia import cria_graficos_cor_raca
            grafico_cor_raca_bahia = cria_graficos_cor_raca(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Cor e Raça em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_cor_raca_bahia[i])

        elif matriculas == 'Por faixa etária':
            from dados_faixa_etaria_bahia import cria_graficos_faixa_etaria
            grafico_faixa_etaria_bahia = cria_graficos_faixa_etaria(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Faixa Etária em ' + str(ano) + ' - ' + localidade)
            for i in range(len(grafico_faixa_etaria_bahia)):
                st.plotly_chart(grafico_faixa_etaria_bahia[i])

        elif matriculas == 'Por sexo':
            from dados_por_sexo_bahia import cria_grafico_matriculas_por_sexo
            grafico_matriculas_por_sexo = cria_grafico_matriculas_por_sexo(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Sexo em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_matriculas_por_sexo[i])
        else:
            'Ainda não há dados para este ano.'
    elif ano == 2022:
        if matriculas == 'Por cor e raça':
            from dados_cor_raca_bahia import cria_graficos_cor_raca
            grafico_cor_raca_bahia = cria_graficos_cor_raca(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Cor e Raça em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_cor_raca_bahia[i])

        elif matriculas == 'Por faixa etária':
            from dados_faixa_etaria_bahia import cria_graficos_faixa_etaria
            grafico_faixa_etaria_bahia = cria_graficos_faixa_etaria(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Faixa Etária em ' + str(ano) + ' - ' + localidade)
            for i in range(len(grafico_faixa_etaria_bahia)):
                st.plotly_chart(grafico_faixa_etaria_bahia[i])

        elif matriculas == 'Por sexo':
            from dados_por_sexo_bahia import cria_grafico_matriculas_por_sexo
            grafico_matriculas_por_sexo = cria_grafico_matriculas_por_sexo(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Sexo em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_matriculas_por_sexo[i])
        else:
            'Ainda não há dados para este ano.'

# Salvador: ------------------------------------
elif localidade == 'Salvador':
    if ano == 2013:
        if matriculas == 'Por cor e raça':
            from dados_cor_raca_salvador import cria_graficos_cor_raca
            grafico_cor_raca_salvador = cria_graficos_cor_raca(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Cor e Raça em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_cor_raca_salvador[i])

        elif matriculas == 'Por faixa etária':
            from dados_faixa_etaria_salvador import cria_graficos_faixa_etaria
            grafico_faixa_etaria_salvador = cria_graficos_faixa_etaria(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Faixa Etária em ' + str(ano) + ' - ' + localidade)
            for i in range(len(grafico_faixa_etaria_salvador)):
                st.plotly_chart(grafico_faixa_etaria_salvador[i])

        elif matriculas == 'Por sexo':
            from dados_por_sexo_salvador import cria_grafico_matriculas_por_sexo
            grafico_matriculas_por_sexo = cria_grafico_matriculas_por_sexo(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Sexo em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_matriculas_por_sexo[i])
        else:
            'Ainda não há dados para este ano.'

    elif ano == 2014:
        if matriculas == 'Por cor e raça':
            from dados_cor_raca_salvador import cria_graficos_cor_raca
            grafico_cor_raca_salvador = cria_graficos_cor_raca(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Cor e Raça em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_cor_raca_salvador[i])

        elif matriculas == 'Por faixa etária':
            from dados_faixa_etaria_salvador import cria_graficos_faixa_etaria
            grafico_faixa_etaria_salvador = cria_graficos_faixa_etaria(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Faixa Etária em ' + str(ano) + ' - ' + localidade)
            for i in range(len(grafico_faixa_etaria_salvador)):
                st.plotly_chart(grafico_faixa_etaria_salvador[i])

        elif matriculas == 'Por sexo':
            from dados_por_sexo_salvador import cria_grafico_matriculas_por_sexo
            grafico_matriculas_por_sexo = cria_grafico_matriculas_por_sexo(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Sexo em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_matriculas_por_sexo[i])
        else:
            'Ainda não há dados para este ano.'
    elif ano == 2015:
        if matriculas == 'Por cor e raça':
            from dados_cor_raca_salvador import cria_graficos_cor_raca
            grafico_cor_raca_salvador = cria_graficos_cor_raca(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Cor e Raça em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_cor_raca_salvador[i])

        elif matriculas == 'Por faixa etária':
            from dados_faixa_etaria_salvador import cria_graficos_faixa_etaria
            grafico_faixa_etaria_salvador = cria_graficos_faixa_etaria(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Faixa Etária em ' + str(ano) + ' - ' + localidade)
            for i in range(len(grafico_faixa_etaria_salvador)):
                st.plotly_chart(grafico_faixa_etaria_salvador[i])

        elif matriculas == 'Por sexo':
            from dados_por_sexo_salvador import cria_grafico_matriculas_por_sexo
            grafico_matriculas_por_sexo = cria_grafico_matriculas_por_sexo(
                localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Sexo em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_matriculas_por_sexo[i])
        else:
            'Ainda não há dados para este ano.'
    elif ano == 2016:
        if matriculas == 'Por cor e raça':
            from dados_cor_raca_salvador import cria_graficos_cor_raca
            grafico_cor_raca_salvador = cria_graficos_cor_raca(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Cor e Raça em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_cor_raca_salvador[i])

        elif matriculas == 'Por faixa etária':
            from dados_faixa_etaria_salvador import cria_graficos_faixa_etaria
            grafico_faixa_etaria_salvador = cria_graficos_faixa_etaria(
                localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Faixa Etária em ' + str(ano) + ' - ' + localidade)
            for i in range(len(grafico_faixa_etaria_salvador)):
                st.plotly_chart(grafico_faixa_etaria_salvador[i])

        elif matriculas == 'Por sexo':
            from dados_por_sexo_salvador import cria_grafico_matriculas_por_sexo
            grafico_matriculas_por_sexo = cria_grafico_matriculas_por_sexo(
                localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Sexo em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_matriculas_por_sexo[i])

        else:
            'Ainda não há dados para este ano.'

    elif ano == 2017:
        if matriculas == 'Por cor e raça':
            from dados_cor_raca_salvador import cria_graficos_cor_raca
            grafico_cor_raca_salvador = cria_graficos_cor_raca(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Cor e Raça em ' + str(ano) + ' - ' + localidade)
            for i in range(3):
                st.plotly_chart(grafico_cor_raca_salvador[i])

        elif matriculas == 'Por faixa etária':
            from dados_faixa_etaria_salvador import cria_graficos_faixa_etaria
            grafico_faixa_etaria_salvador = cria_graficos_faixa_etaria(
                localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Faixa Etária em ' + str(ano) + ' - ' + localidade)
            for i in range(len(grafico_faixa_etaria_salvador)):
                st.plotly_chart(grafico_faixa_etaria_salvador[i])

        elif matriculas == 'Por sexo':
            from dados_por_sexo_salvador import cria_grafico_matriculas_por_sexo
            grafico_matriculas_por_sexo = cria_grafico_matriculas_por_sexo(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Sexo em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_matriculas_por_sexo[i])
        else:
            'Ainda não há dados para este ano.'
    elif ano == 2018:
        if matriculas == 'Por cor e raça':
            from dados_cor_raca_salvador import cria_graficos_cor_raca
            grafico_cor_raca_salvador = cria_graficos_cor_raca(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Cor e Raça em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_cor_raca_salvador[i])

        elif matriculas == 'Por faixa etária':
            from dados_faixa_etaria_salvador import cria_graficos_faixa_etaria
            grafico_faixa_etaria_salvador = cria_graficos_faixa_etaria(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Faixa Etária em ' + str(ano) + ' - ' + localidade)
            for i in range(len(grafico_faixa_etaria_salvador)):
                st.plotly_chart(grafico_faixa_etaria_salvador[i])

        elif matriculas == 'Por sexo':
            from dados_por_sexo_salvador import cria_grafico_matriculas_por_sexo
            grafico_matriculas_por_sexo = cria_grafico_matriculas_por_sexo(
                localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Sexo em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_matriculas_por_sexo[i])
        else:
            'Ainda não há dados para este ano.'
    elif ano == 2019:
        if matriculas == 'Por cor e raça':
            from dados_cor_raca_salvador import cria_graficos_cor_raca
            grafico_cor_raca_salvador = cria_graficos_cor_raca(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Cor e Raça em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_cor_raca_salvador[i])

        elif matriculas == 'Por faixa etária':
            from dados_faixa_etaria_salvador import cria_graficos_faixa_etaria
            grafico_faixa_etaria_salvador = cria_graficos_faixa_etaria(
                localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Faixa Etária em ' + str(ano) + ' - ' + localidade)
            for i in range(len(grafico_faixa_etaria_salvador)):
                st.plotly_chart(grafico_faixa_etaria_salvador[i])

        elif matriculas == 'Por sexo':
            from dados_por_sexo_salvador import cria_grafico_matriculas_por_sexo
            grafico_matriculas_por_sexo = cria_grafico_matriculas_por_sexo(
                localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Sexo em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_matriculas_por_sexo[i])
        else:
            'Ainda não há dados para este ano.'
    elif ano == 2020:
        if matriculas == 'Por cor e raça':
            from dados_cor_raca_salvador import cria_graficos_cor_raca
            grafico_cor_raca_salvador = cria_graficos_cor_raca(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Cor e Raça em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_cor_raca_salvador[i])

        elif matriculas == 'Por faixa etária':
            from dados_faixa_etaria_salvador import cria_graficos_faixa_etaria
            grafico_faixa_etaria_salvador = cria_graficos_faixa_etaria(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Faixa Etária em ' + str(ano) + ' - ' + localidade)
            for i in range(len(grafico_faixa_etaria_salvador)):
                st.plotly_chart(grafico_faixa_etaria_salvador[i])

        elif matriculas == 'Por sexo':
            from dados_por_sexo_salvador import cria_grafico_matriculas_por_sexo
            grafico_matriculas_por_sexo = cria_grafico_matriculas_por_sexo(
                localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Sexo em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_matriculas_por_sexo[i])
        else:
            'Ainda não há dados para este ano.'
    elif ano == 2021:
        if matriculas == 'Por cor e raça':
            from dados_cor_raca_salvador import cria_graficos_cor_raca
            cria_graficos_cor_raca = cria_graficos_cor_raca(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Cor e Raça em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(cria_graficos_cor_raca[i])

        elif matriculas == 'Por faixa etária':
            from dados_faixa_etaria_salvador import cria_graficos_faixa_etaria

            grafico_faixa_etaria_salvador = cria_graficos_faixa_etaria(localidade=localidade, matriculas=matriculas,
                                                                       ano=ano)
            st.subheader('Matrículas por Faixa Etária em ' + str(ano) + ' - ' + localidade)
            for i in range(len(grafico_faixa_etaria_salvador)):
                st.plotly_chart(grafico_faixa_etaria_salvador[i])

        elif matriculas == 'Por sexo':
            from dados_por_sexo_salvador import cria_grafico_matriculas_por_sexo
            grafico_matriculas_por_sexo = cria_grafico_matriculas_por_sexo(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Sexo em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_matriculas_por_sexo[i])
        else:
            'Ainda não há dados para este ano.'
    elif ano == 2022:
        if matriculas == 'Por cor e raça':
            from dados_cor_raca_salvador import cria_graficos_cor_raca
            grafico_cor_raca_salvador = cria_graficos_cor_raca(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Cor e Raça em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_cor_raca_salvador[i])

        elif matriculas == 'Por faixa etária':
            from dados_faixa_etaria_salvador import cria_graficos_faixa_etaria

            grafico_faixa_etaria_salvador = cria_graficos_faixa_etaria(localidade=localidade, matriculas=matriculas,
                                                                       ano=ano)
            st.subheader('Matrículas por Faixa Etária em ' + str(ano) + ' - ' + localidade)
            for i in range(len(grafico_faixa_etaria_salvador)):
                st.plotly_chart(grafico_faixa_etaria_salvador[i])

        elif matriculas == 'Por sexo':
            from dados_por_sexo_salvador import cria_grafico_matriculas_por_sexo
            grafico_matriculas_por_sexo = cria_grafico_matriculas_por_sexo(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Sexo em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_matriculas_por_sexo[i])
        else:
            'Ainda não há dados para este ano.'
else:
    'Ainda não há dados para este ano.'
