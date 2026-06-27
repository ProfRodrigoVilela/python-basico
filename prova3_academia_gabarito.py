# ================================================================
# SISTEMA ACADEMIA FITNESS
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
planos = {}
treinos = {}
pagamentos = []

# =========================
# FUNÇÕES DE ALUNOS
# =========================

def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    idade = int(input("Idade: "))

    aluno = {
        "nome": nome,
        "idade": idade
    }

    alunos.append(aluno)

    print("Aluno cadastrado com sucesso!")


def listar_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        print("\nLISTA DE ALUNOS")
        print("-" * 30)

        for aluno in alunos:
            print("Nome:", aluno["nome"])
            print("Idade:", aluno["idade"], "anos")
            print("-" * 30)

        print("Total de alunos:", len(alunos))


def sortear_aluno():
    if len(alunos) == 0:
        print("Cadastre alunos primeiro.")
    else:
        escolhido = random.choice(alunos)
        print("Aluno sorteado:", escolhido["nome"])


def buscar_aluno():
    nome = input("Nome para busca: ")
    encontrado = False

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            print("\nAluno encontrado!")
            print("Nome:", aluno["nome"])
            print("Idade:", aluno["idade"])
            encontrado = True
            break

    if not encontrado:
        print("Aluno não encontrado.")

# =========================
# FUNÇÕES DE PLANOS
# =========================

def cadastrar_plano():
    nome = input("Nome do aluno: ")

    print("\nPlanos disponíveis:")
    print("1 - Básico   -> R$ 89,90")
    print("2 - Intermediário -> R$ 129,90")
    print("3 - Premium  -> R$ 199,90")

    opcao = input("Escolha o plano (1/2/3): ")

    if opcao == "1":
        plano = "Básico"
        valor = 89.90
    elif opcao == "2":
        plano = "Intermediário"
        valor = 129.90
    elif opcao == "3":
        plano = "Premium"
        valor = 199.90
    else:
        print("Opção inválida.")
        return

    planos[nome] = {
        "plano": plano,
        "valor": valor
    }

    print("Plano cadastrado com sucesso!")


def consultar_plano():
    nome = input("Nome do aluno: ")

    if nome in planos:
        dados = planos[nome]
        print("\nAluno:", nome)
        print("Plano:", dados["plano"])
        print("Mensalidade: R$", dados["valor"])
    else:
        print("Plano não encontrado para este aluno.")


def listar_planos():
    if len(planos) == 0:
        print("Nenhum plano cadastrado.")
    else:
        print("\nPLANOS ATIVOS")
        print("-" * 30)

        for nome, dados in planos.items():
            print("Aluno:", nome)
            print("Plano:", dados["plano"])
            print("Valor: R$", dados["valor"])
            print("-" * 30)

# =========================
# FUNÇÕES DE TREINOS
# =========================

def registrar_treino():
    nome = input("Nome do aluno: ")

    print("\nTipos de treino:")
    print("A - Peito e Tríceps")
    print("B - Costas e Bíceps")
    print("C - Pernas e Ombros")

    tipo = input("Tipo de treino (A/B/C): ").upper()

    if tipo not in ["A", "B", "C"]:
        print("Tipo inválido.")
        return

    duracao = int(input("Duração em minutos: "))

    treinos[nome] = {
        "tipo": tipo,
        "duracao": duracao
    }

    print("Treino registrado!")


def consultar_treino():
    nome = input("Nome do aluno: ")

    if nome in treinos:
        dados = treinos[nome]
        print("\nAluno:", nome)
        print("Treino:", dados["tipo"])
        print("Duração:", dados["duracao"], "minutos")
    else:
        print("Nenhum treino registrado para este aluno.")


def listar_treinos():
    if len(treinos) == 0:
        print("Nenhum treino registrado.")
    else:
        print("\nTREINOS REGISTRADOS")
        print("-" * 30)

        for nome, dados in treinos.items():
            print("Aluno:", nome)
            print("Treino:", dados["tipo"])
            print("Duração:", dados["duracao"], "min")
            print("-" * 30)

# =========================
# FUNÇÕES DE PAGAMENTOS
# =========================

def registrar_pagamento():
    nome = input("Nome do aluno: ")

    if nome not in planos:
        print("Aluno sem plano cadastrado.")
        return

    valor = planos[nome]["valor"]

    pagamento = {
        "aluno": nome,
        "valor": valor,
        "plano": planos[nome]["plano"]
    }

    pagamentos.append(pagamento)

    print("Pagamento de R$", valor, "registrado para", nome)


def aplicar_desconto():
    if len(pagamentos) == 0:
        print("Nenhum pagamento registrado.")
        return

    ultimo = pagamentos[-1]

    desconto = random.choice([5, 10, 15])

    valor_desconto = ultimo["valor"] * (desconto / 100)
    total = ultimo["valor"] - valor_desconto

    print("\nAluno:", ultimo["aluno"])
    print("Plano:", ultimo["plano"])
    print("Valor original: R$", ultimo["valor"])
    print("Desconto sorteado:", desconto, "%")
    print("Valor com desconto: R$", round(total, 2))


def relatorio_pagamentos():
    if len(pagamentos) == 0:
        print("Nenhum pagamento encontrado.")
        return

    total = 0

    print("\nRELATÓRIO DE PAGAMENTOS")
    print("-" * 30)

    for p in pagamentos:
        print(p["aluno"], "-", p["plano"], "- R$", p["valor"])
        total += p["valor"]

    print("-" * 30)
    print("TOTAL ARRECADADO: R$", round(total, 2))

# =========================
# RELATÓRIO GERAL
# =========================

def relatorio_geral():
    print("\nRELATÓRIO GERAL DA ACADEMIA")
    print("-" * 40)
    print("Total de alunos cadastrados:", len(alunos))
    print("Total de planos ativos:", len(planos))
    print("Total de treinos registrados:", len(treinos))
    print("Total de pagamentos:", len(pagamentos))

    total = 0

    for p in pagamentos:
        total += p["valor"]

    print("Receita total: R$", round(total, 2))

# =========================
# SUBMENUS
# =========================

def menu_alunos():
    while True:
        print("\n=== MENU ALUNOS ===")
        print("1 - Cadastrar Aluno")
        print("2 - Listar Alunos")
        print("3 - Buscar Aluno")
        print("4 - Sortear Aluno")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_aluno()
        elif op == "2":
            listar_alunos()
        elif op == "3":
            buscar_aluno()
        elif op == "4":
            sortear_aluno()
        elif op == "0":
            break
        else:
            print("Opção inválida.")


def menu_planos():
    while True:
        print("\n=== MENU PLANOS ===")
        print("1 - Cadastrar Plano")
        print("2 - Consultar Plano")
        print("3 - Listar Planos")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_plano()
        elif op == "2":
            consultar_plano()
        elif op == "3":
            listar_planos()
        elif op == "0":
            break
        else:
            print("Opção inválida.")


def menu_treinos():
    while True:
        print("\n=== MENU TREINOS ===")
        print("1 - Registrar Treino")
        print("2 - Consultar Treino")
        print("3 - Listar Treinos")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            registrar_treino()
        elif op == "2":
            consultar_treino()
        elif op == "3":
            listar_treinos()
        elif op == "0":
            break
        else:
            print("Opção inválida.")


def menu_pagamentos():
    while True:
        print("\n=== MENU PAGAMENTOS ===")
        print("1 - Registrar Pagamento")
        print("2 - Aplicar Desconto")
        print("3 - Relatório de Pagamentos")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            registrar_pagamento()
        elif op == "2":
            aplicar_desconto()
        elif op == "3":
            relatorio_pagamentos()
        elif op == "0":
            break
        else:
            print("Opção inválida.")

# =========================
# MENU PRINCIPAL
# =========================

while True:
    print("\n" + "=" * 50)
    print("   SISTEMA ACADEMIA FITNESS")
    print("=" * 50)
    print("1 - Gestão de Alunos")
    print("2 - Gestão de Planos")
    print("3 - Controle de Treinos")
    print("4 - Pagamentos")
    print("5 - Relatório Geral")
    print("0 - Encerrar")

    opcao = input("Escolha: ")

    if opcao == "1":
        menu_alunos()
    elif opcao == "2":
        menu_planos()
    elif opcao == "3":
        menu_treinos()
    elif opcao == "4":
        menu_pagamentos()
    elif opcao == "5":
        relatorio_geral()
    elif opcao == "0":
        print("Sistema encerrado. Até logo!")
        break
    else:
        print("Opção inválida.")
