# streamlit_app.py
import geopandas as gpd
import streamlit as st
import matplotlib.pyplot as plt

gdf = gpd.read_file("dados/gadm41_PRT_0.shp")
distritos = gdf["Distrito"].unique()

filtro = st.selectbox("Seleciona o Distrito", distritos)
gdf_filtrado = gdf[gdf["Distrito"] == filtro]

st.write("Estatísticas de Área:")
st.write(gdf_filtrado["Area_km2"].describe())

st.pyplot(gdf_filtrado.plot(column="Area_km2", legend=True).figure)
