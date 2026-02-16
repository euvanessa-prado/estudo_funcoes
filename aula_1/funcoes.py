"""Funções matemáticas básicas."""

valor1_teste = 50
valor2_teste = 60


def soma(valor1: float, valor2: float) -> float:
    """Soma dois números."""
    resultado = valor1 + valor2
    return resultado


total = soma(valor1_teste, valor2_teste)
print(total)


def multiplicacao(valor2_multiplicacao: float, valor4_multiplicacao: float) -> float:
    """Multiplica dois números."""
    resultado_multiplicacao = valor2_multiplicacao * valor4_multiplicacao
    return resultado_multiplicacao


print(multiplicacao(valor1_teste, valor2_teste))

    