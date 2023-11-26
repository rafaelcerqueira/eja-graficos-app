import streamlit as st

# Header
st.header('Dados de Matrículas da Educação de Jovens e Adultos (EJA) na Bahia')

# Menu Lateral
st.sidebar.title('Menu')
st.sidebar.header('Selecione a opção desejada:')
localidade = st.sidebar.selectbox('Localidade', ('Bahia', 'Salvador'))
matriculas = st.sidebar.radio('Matrículas', ('Por cor e raça', 'Por faixa etária', 'Por sexo'))
ano = st.sidebar.selectbox('Ano', (2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022))

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
            'Ainda não há dados para este ano.'

        elif matriculas == 'Por sexo':
            from dados_por_sexo_bahia import cria_grafico_matriculas_por_sexo
            grafico_matriculas_por_sexo = cria_grafico_matriculas_por_sexo(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Sexo em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_matriculas_por_sexo[i])
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
            'Ainda não há dados para este ano.'

        elif matriculas == 'Por sexo':
            from dados_por_sexo_bahia import cria_grafico_matriculas_por_sexo
            grafico_matriculas_por_sexo = cria_grafico_matriculas_por_sexo(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Sexo em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(grafico_matriculas_por_sexo[i])
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
            'Ainda não há dados para este ano.'

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
            'Ainda não há dados para este ano.'

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
            'Ainda não há dados para este ano.'

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
            'Ainda não há dados para este ano.'

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
            'Ainda não há dados para este ano.'

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
            'Ainda não há dados para este ano.'

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
            'Ainda não há dados para este ano.'

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
            'Ainda não há dados para este ano.'

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
            'Ainda não há dados para este ano.'

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
            'Ainda não há dados para este ano.'

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
            'Ainda não há dados para este ano.'

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
            'Ainda não há dados para este ano.'

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
            'Ainda não há dados para este ano.'

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
            'Ainda não há dados para este ano.'

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
            'Ainda não há dados para este ano.'

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
            'Ainda não há dados para este ano.'

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
            from dados_por_sexo_salvador import cria_grafico_matriculas_por_sexo
            cria_grafico_matriculas_por_sexo = cria_grafico_matriculas_por_sexo(localidade=localidade, matriculas=matriculas, ano=ano)
            st.subheader('Matrículas por Cor e Raça em ' + str(ano) + ' - ' + localidade)
            for i in range(4):
                st.plotly_chart(cria_grafico_matriculas_por_sexo[i])

        elif matriculas == 'Por faixa etária':
            'Ainda não há dados para este ano.'

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
            'Ainda não há dados para este ano.'

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
