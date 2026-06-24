# --- GABARITO: DESAFIO SIMULADOR DE DADOS ---

import random

# Definindo a função que faz o sorteio
def rolar_dado():
    numero = random.randint(1, 6)
    return numero

print("--- JOGO DE DADOS ---")

# Loop contínuo para o usuário jogar quantas vezes quiser
while True:
    acao = input("Digite 'jogar' para rolar o dado ou 'sair' para encerrar: ")
    
    if acao == 'sair':
        print("Saindo do jogo... Até mais!")
        break # Quebra o loop
    elif acao == 'jogar':
        resultado = rolar_dado() # Chama a função
        print(f"🎲 Você rolou um: {resultado}\n")
    else:
        print("Comando inválido. Tente novamente.\n")
