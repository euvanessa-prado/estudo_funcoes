"""Pipeline ETL para processar dados de vendas."""

import pandas as pd
import os
import glob


def extract(pasta: str) -> pd.DataFrame:
    """Lê todos os arquivos JSON de uma pasta e combina em um DataFrame."""
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


def calculo_transformacao(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula o valor total de cada venda (Quantidade × Venda)."""
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df


def carregar_dados(df: pd.DataFrame, formato_saida: list):
    """Exporta o DataFrame em múltiplos formatos (csv, parquet)."""
    for formato in formato_saida:
        if formato == 'csv':
            df.to_csv('dados_saida.csv', index=False)
        if formato == 'parquet':
            df.to_parquet('dados_saida.parquet', index=False)
            
def pipeline_calcular_kpi_de_vendas_consolidado(pasta:str,formato_saida:list):
    data_frame = extract(pasta)
    calc_transformado = calculo_transformacao(data_frame)
    carregar_dados_transf = carregar_dados(calc_transformado, formato_saida)