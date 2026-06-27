# ====================================================
# PROVÃO PRÁTICO PYTHON - GABARITO COMPLETO
# Técnico em Desenvolvimento Web e Mobile
# ====================================================

# Importação do módulo random
import random

# ====================================================
# VARIÁVEIS GLOBAIS
# ====================================================

# Lista para armazenar alunos
alunos = []

# Dicionário para armazenar produtos
estoque = {}

# ====================================================
# FUNÇÕES DO SISTEMA 1
# CADASTRO E SORTEIO DE ALUNOS
# ====================================================

def cadastrar_aluno():

    nome = input("Nome do aluno: ")

    alunos.append(nome)

    print("Aluno cadastrado com sucesso!")


def listar_alunos():

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:

        print("\nLISTA DE ALUNOS")

        for aluno in alunos:
            print(aluno)

        print(f"Total: {len(alunos)} aluno(s)")


def sortear_aluno():

    if len(alunos) == 0:

        print("Cadastre alunos primeiro.")

    else:

        sorteado = random.choice(alunos)

        print(f"Aluno sorteado: {sorteado}")

# ====================================================
# FUNÇÕES DO SISTEMA 2
# CONTROLE DE ESTOQUE
# ====================================================

def cadastrar_produto():

    nome = input("Nome do produto: ")

    quantidade = int(input("Quantidade: "))

    estoque[nome] = quantidade

    print("Produto cadastrado.")


def consultar_produto():

    nome = input("Produto para consulta: ")

    if nome in estoque:

        print(f"Quantidade disponível: {estoque[nome]}")

    else:

        print("Produto não encontrado.")


def atualizar_estoque():

    nome = input("Produto: ")

    if nome in estoque:

        nova_qtd = int(input("Nova quantidade: "))

        estoque[nome] = nova_qtd

        print("Estoque atualizado.")

    else:

        print("Produto não encontrado.")


def listar_produtos():

    if len(estoque) == 0:

        print("Nenhum produto cadastrado.")

    else:

        print("\nESTOQUE")

        for produto, quantidade in estoque.items():

            print(f"{produto} -> {quantidade}")

# ====================================================
# FUNÇÕES DO SISTEMA 3
# SISTEMA DE NOTAS
# ====================================================

def calcular_media(n1, n2, n3):

    media = (n1 + n2 + n3) / 3

    return media


def sistema_notas():

    nome = input("Nome do aluno: ")

    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    media = calcular_media(
        nota1,
        nota2,
        nota3
    )

    print(f"\nAluno: {nome}")
    print(f"Média: {media:.2f}")

    if media >= 7:

        print("Situação: APROVADO")

    elif media >= 5:

        print("Situação: RECUPERAÇÃO")

    else:

        print("Situação: REPROVADO")

# ====================================================
# FUNÇÕES DO SISTEMA 4
# JOGO DA ADIVINHAÇÃO
# ====================================================

def jogo_adivinhacao():

    numero_secreto = random.randint(1, 10)

    tentativas = 0

    print("\nTente acertar o número entre 1 e 10!")

    while True:

        chute = int(input("Seu palpite: "))

        tentativas += 1

        if chute == numero_secreto:

            print("Parabéns! Você acertou!")

            print(f"Tentativas: {tentativas}")

            break

        elif chute < numero_secreto:

            print("O número secreto é MAIOR.")

        else:

            print("O número secreto é MENOR.")

# ====================================================
# MENU PRINCIPAL
# ====================================================

while True:

    print("\n")
    print("=" * 50)
    print("SISTEMA INTEGRADO - PROVÃO PYTHON")
    print("=" * 50)

    print("1 - Cadastro de Alunos")
    print("2 - Listar Alunos")
    print("3 - Sortear Aluno")

    print("4 - Cadastrar Produto")
    print("5 - Consultar Produto")
    print("6 - Atualizar Estoque")
    print("7 - Listar Produtos")

    print("8 - Sistema de Notas")

    print("9 - Jogo da Adivinhação")

    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    # ==========================
    # ESTRUTURAS CONDICIONAIS
    # ==========================

    if opcao == "1":

        cadastrar_aluno()

    elif opcao == "2":

        listar_alunos()

    elif opcao == "3":

        sortear_aluno()

    elif opcao == "4":

        cadastrar_produto()

    elif opcao == "5":

        consultar_produto()

    elif opcao == "6":

        atualizar_estoque()

    elif opcao == "7":

        listar_produtos()

    elif opcao == "8":

        sistema_notas()

    elif opcao == "9":

        jogo_adivinhacao()

    elif opcao == "0":

        print("Sistema encerrado.")

        break

    else:

        print("Opção inválida!")
