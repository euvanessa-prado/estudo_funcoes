
from etl import pipeline_calcular_kpi_de_vendas_consolidado


pasta:str = 'data'
formato:list = ['parquet']

pipeline_calcular_kpi_de_vendas_consolidado(pasta,formato)
