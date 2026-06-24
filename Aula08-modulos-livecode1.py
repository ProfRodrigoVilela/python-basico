# =====================================
# AULA 08 - FUNÇÕES E MÓDULOS EM PYTHON
# Exemplo: Sistema de Loja Virtual
# =====================================

# Importando um módulo pronto do Python
import random

print("=" * 40)
print("      LOJA DO PROFESSOR")
print("=" * 40)

# -------------------------------------
# FUNÇÃO 1 - Exibe mensagem de boas-vindas
# -------------------------------------
def exibir_mensagem():
    print("\nBem-vindo(a) à nossa loja!")
    print("Hoje você poderá ganhar um cupom surpresa!")

# -------------------------------------
# FUNÇÃO 2 - Calcula desconto
# Recebe:
# preco -> valor do produto
# percentual -> desconto em %
# Retorna:
# valor final com desconto
# -------------------------------------
def calcular_desconto(preco, percentual):
    desconto = preco * (percentual / 100)
    preco_final = preco - desconto
    return preco_final

# -------------------------------------
# CHAMANDO A PRIMEIRA FUNÇÃO
# -------------------------------------
exibir_mensagem()

# -------------------------------------
# Recebendo informações do usuário
# -------------------------------------
nome_produto = input("\nDigite o nome do produto: ")

valor_produto = float(
    input("Digite o valor do produto: R$ ")
)

# -------------------------------------
# Sorteando um cupom de desconto
# -------------------------------------
desconto_sorteado = random.choice([5, 10, 15, 20])
print(f"\n🎉 Parabéns! Você ganhou {desconto_sorteado}% de desconto!")
# -------------------------------------
# Chamando a função para calcular
# -------------------------------------
valor_final = calcular_desconto(
    valor_produto,
    desconto_sorteado
)
# Exibindo resultado
print("\n------ RESUMO DA COMPRA ------")
print(f"Produto: {nome_produto}")
print(f"Valor original: R$ {valor_produto:.2f}")
print(f"Desconto: {desconto_sorteado}%")
print(f"Valor final: R$ {valor_final:.2f}")
print("------------------------------")
