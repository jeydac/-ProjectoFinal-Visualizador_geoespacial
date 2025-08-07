# app.py
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

def carregar_dados(caminho):
    print("A carregar ficheiro geoespacial...")
    gdf = gpd.read_file(caminho)
    print("Dados carregados com sucesso.")
    return gdf

def aplicar_filtros(gdf, coluna, valor):
    print(f"A aplicar filtro: {coluna} == {valor}")
    return gdf[gdf[coluna] == valor]

def mostrar_mapa(gdf, coluna_valor=None):
    print("A gerar mapa...")
    if coluna_valor:
        gdf.plot(column=coluna_valor, legend=True, figsize=(10, 8), cmap='viridis')
    else:
        gdf.plot(figsize=(10, 8))
    plt.title("Mapa Geoespacial")
    plt.show()

def estatisticas(gdf, coluna):
    print(f"Estatísticas da coluna '{coluna}':")
    print(gdf[coluna].describe())

if __name__ == "__main__":
    caminho = "dados/gadm41_PRT_shp/gadm41_PRT_3.shp"
    gdf = carregar_dados(caminho)

    # Filtros
    gdf_filtrado = aplicar_filtros(gdf, "NAME_1", "Porto")

    # # Estatísticas
    # estatisticas(gdf_filtrado, "Area_km2")

    # # Visualização
    mostrar_mapa(gdf_filtrado, "Porto")
