# uma funcao que realiza o extract
import pandas as pd
import os
import glob


def extract(pasta:str)-> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


def calculo_transformacao(df:pd.DataFrame)-> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

def carregar_dados(df:pd.DataFrame, formato_saida:list):
    for formato in formato_saida:
        if formato == 'csv':
            df.to_csv('dados_saida.csv', index=False)
        if formato == 'parquet':
            df.to_parquet('dados_saida.parquet', index=False)

if __name__ == "__main__":
   pasta_argumento = 'data'
   data_frame = extract(pasta_argumento)
   calc_transformado = calculo_transformacao(data_frame)
   formato_saida:list = ["csv","parquet"]
   carregar_dados_transf = carregar_dados(calc_transformado,formato_saida)
