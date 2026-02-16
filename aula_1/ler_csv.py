"""Leitura e processamento de arquivos CSV."""

import csv

path_arquivo = 'vendas.csv'


def ler_csv(nome_arquivo_csv: str) -> list[dict]:
    """Lê um arquivo CSV e retorna lista de dicionários."""
    with open(nome_arquivo_csv, mode="r", encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)


def calc_vendas_categoria(lista: list[dict]) -> list[dict]:
    """Filtra produtos não entregues (entregue = False)."""
    lista_produto_calc = []
    
    for linha in lista:
        if linha.get("entregue") == "False":
            lista_produto_calc.append(linha)
    
    return lista_produto_calc


def somar_produtos(lista: list[dict]) -> float:
    """Soma os preços de todos os produtos."""
    lista_somada = 0
    
    for linha in lista:
        lista_somada += float(linha.get("price"))
    
    return lista_somada
