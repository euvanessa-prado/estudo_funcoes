import csv
path_arquivo = 'vendas.csv'



##### modo 1 #####
def ler_csv(nome_arquivo_csv:str) ->list[dict]:
    """funcao que le um csv e retorna uma lista de dicionários"""
    with open(nome_arquivo_csv, mode="r", encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
    
        return  list(leitor)

#### modo 2 ######


def calc_vendas_categoria(lista: list[dict]) -> list[dict]:
    """Função que filtra uma lista de dicionários por categoria, preço e entrega"""
    lista_produto_calc = []
    
    for linha in lista:
        # Filtra por entregue = False
        if linha.get("entregue") == "False":
            
            lista_produto_calc.append(linha)
    
    return lista_produto_calc




def somar_produtos(lista:list[dict]) -> list[dict]:
    lista_somada =0
    
    for linha in lista:
        lista_somada += float(linha.get("price"))
    return lista_somada
