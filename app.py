import streamlit as st
import pandas as pd
import plotly.express as px
from aurassure_bot import gerar_relatorio

st.set_page_config(
    page_title="Air Quality Dashboard",
    layout="wide"
)

st.title("🌍 Air Quality Dashboard")

# seleção de data
col1, col2 = st.columns(2)

mes = col1.selectbox(
    "Mês",
    ["01","02","03","04","05","06","07","08","09","10","11","12"]
)

ano = col2.selectbox(
    "Ano",
    ["2024","2025","2026"]
)

if st.button("Gerar relatório"):

    st.info("Coletando dados do Aurassure...")

    caminho = gerar_relatorio(mes,ano)

    df = pd.read_csv(caminho)

    st.success("Relatório carregado!")

    # métricas
    col1,col2 = st.columns(2)

    col1.metric("PM2.5 médio", round(df["pm25"].mean(),2))
    col2.metric("Número de cidades", len(df))

    st.divider()

    # gráfico
    fig = px.bar(
        df,
        x="cidade",
        y="pm25",
        title="PM2.5 por cidade"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # mapa
    fig_map = px.scatter_mapbox(
        df,
        lat="lat",
        lon="lon",
        size="pm25",
        hover_name="cidade",
        zoom=4
    )

    fig_map.update_layout(mapbox_style="open-street-map")

    st.plotly_chart(fig_map, use_container_width=True)

    st.dataframe(df)