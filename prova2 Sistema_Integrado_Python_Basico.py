# ================================================================
# SISTEMA INTEGRADO - PROJETO FINAL PYTHON BÁSICO
# Autor: Gabarito do Professor
# Conteúdos:
# - print / input
# - variáveis
# - listas e dicionários
# - if / elif / else
# - for / while / break
# - funções
# - parâmetros e return
# - import random
# ================================================================

import random

# =========================
# ESTRUTURAS DE DADOS
# =========================

alunos = []
boletins = {}
estoque = {}
vendas = []

# =========================
# FUNÇÕES DE ALUNOS
# =========================

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
            print("-", aluno)

def sortear_aluno():
    if len(alunos) == 0:
        print("Cadastre alunos primeiro.")
    else:
        escolhido = random.choice(alunos)
        print(f"Aluno sorteado: {escolhido}")

# =========================
# FUNÇÕES DE NOTAS
# =========================

def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def lancar_notas():
    nome = input("Nome do aluno: ")

    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))

    media = calcular_media(n1, n2, n3)

    if media >= 7:
        situacao = "APROVADO"
    elif media >= 5:
        situacao = "RECUPERAÇÃO"
    else:
        situacao = "REPROVADO"

    boletins[nome] = {
        "media": media,
        "situacao": situacao
    }

    print("Boletim registrado!")

def consultar_boletins():
    if len(boletins) == 0:
        print("Nenhum boletim cadastrado.")
    else:
        for nome, dados in boletins.items():
            print("-" * 30)
            print("Aluno:", nome)
            print("Média:", round(dados["media"], 2))
            print("Situação:", dados["situacao"])

# =========================
# FUNÇÕES DE ESTOQUE
# =========================

def cadastrar_produto():
    nome = input("Produto: ")
    qtd = int(input("Quantidade: "))

    estoque[nome] = qtd

    print("Produto cadastrado!")

def atualizar_estoque():
    nome = input("Produto: ")

    if nome in estoque:
        nova_qtd = int(input("Nova quantidade: "))
        estoque[nome] = nova_qtd
        print("Atualizado com sucesso!")
    else:
        print("Produto não encontrado.")

def consultar_produto():
    nome = input("Produto: ")

    if nome in estoque:
        print(f"Quantidade disponível: {estoque[nome]}")
    else:
        print("Produto não encontrado.")

def listar_produtos():
    if len(estoque) == 0:
        print("Nenhum produto cadastrado.")
    else:
        print("\nESTOQUE")
        for produto, qtd in estoque.items():
            print(produto, "->", qtd)

# =========================
# FUNÇÕES DE VENDAS
# =========================

def registrar_venda():
    cliente = input("Nome do cliente: ")
    valor = float(input("Valor da venda: R$ "))

    venda = {
        "cliente": cliente,
        "valor": valor
    }

    vendas.append(venda)

    print("Venda registrada!")

def aplicar_cupom():
    if len(vendas) == 0:
        print("Nenhuma venda cadastrada.")
        return

    ultima = vendas[-1]

    cupom = random.choice([5, 10, 15, 20])

    desconto = ultima["valor"] * (cupom / 100)
    total = ultima["valor"] - desconto

    print("\nCLIENTE:", ultima["cliente"])
    print("Valor original:", ultima["valor"])
    print("Cupom sorteado:", cupom, "%")
    print("Valor final:", round(total, 2))

def relatorio_vendas():
    if len(vendas) == 0:
        print("Nenhuma venda encontrada.")
        return

    total = 0

    print("\nRELATÓRIO DE VENDAS")

    for venda in vendas:
        print(venda["cliente"], "-", venda["valor"])
        total += venda["valor"]

    print("-" * 30)
    print("TOTAL VENDIDO: R$", round(total, 2))

# =========================
# RELATÓRIOS GERAIS
# =========================

def relatorio_geral():
    print("\nRELATÓRIO GERAL")
    print("-" * 40)

    print("Quantidade de alunos:", len(alunos))
    print("Quantidade de boletins:", len(boletins))
    print("Quantidade de produtos:", len(estoque))
    print("Quantidade de vendas:", len(vendas))

    total_vendas = 0

    for venda in vendas:
        total_vendas += venda["valor"]

    print("Valor total vendido:", round(total_vendas, 2))

# =========================
# MENU ALUNOS
# =========================

def menu_alunos():
    while True:

        print("\n=== MENU ALUNOS ===")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Sortear")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_aluno()

        elif op == "2":
            listar_alunos()

        elif op == "3":
            sortear_aluno()

        elif op == "0":
            break

        else:
            print("Opção inválida.")

# =========================
# MENU NOTAS
# =========================

def menu_notas():
    while True:

        print("\n=== MENU NOTAS ===")
        print("1 - Lançar Notas")
        print("2 - Consultar Boletins")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            lancar_notas()

        elif op == "2":
            consultar_boletins()

        elif op == "0":
            break

        else:
            print("Opção inválida.")

# =========================
# MENU ESTOQUE
# =========================

def menu_estoque():
    while True:

        print("\n=== MENU ESTOQUE ===")
        print("1 - Cadastrar Produto")
        print("2 - Atualizar Estoque")
        print("3 - Consultar Produto")
        print("4 - Listar Produtos")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_produto()

        elif op == "2":
            atualizar_estoque()

        elif op == "3":
            consultar_produto()

        elif op == "4":
            listar_produtos()

        elif op == "0":
            break

        else:
            print("Opção inválida.")

# =========================
# MENU VENDAS
# =========================

def menu_vendas():
    while True:

        print("\n=== MENU VENDAS ===")
        print("1 - Registrar Venda")
        print("2 - Aplicar Cupom")
        print("3 - Relatório de Vendas")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            registrar_venda()

        elif op == "2":
            aplicar_cupom()

        elif op == "3":
            relatorio_vendas()

        elif op == "0":
            break

        else:
            print("Opção inválida.")

# =========================
# MENU PRINCIPAL
# =========================

while True:

    print("\n" + "=" * 50)
    print("SISTEMA INTEGRADO PYTHON")
    print("=" * 50)

    print("1 - Gestão de Alunos")
    print("2 - Gestão de Notas")
    print("3 - Controle de Estoque")
    print("4 - Sistema de Vendas")
    print("5 - Relatório Geral")
    print("0 - Encerrar")

    opcao = input("Escolha: ")

    if opcao == "1":
        menu_alunos()

    elif opcao == "2":
        menu_notas()

    elif opcao == "3":
        menu_estoque()

    elif opcao == "4":
        menu_vendas()

    elif opcao == "5":
        relatorio_geral()

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")
