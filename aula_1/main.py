from ler_csv import ler_csv,calc_vendas_categoria,somar_produtos

path_arquivo = "vendas.csv"
lista_produtos = ler_csv(path_arquivo)
vendas_calculadas_nao_entregues = calc_vendas_categoria(lista_produtos)
total = somar_produtos(vendas_calculadas_nao_entregues)
print(total)
