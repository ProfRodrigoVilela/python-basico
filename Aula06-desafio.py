# --- GABARITO: DESAFIO DA TABUADA (AULA 06) ---

print("--- TABUADA INTELIGENTE ---")
# Captura o número digitado pelo usuário (lembre-se do int!)
numero = int(input("Digite um número para ver a sua tabuada: "))

print(f"\nTabuada do {numero}:")
print("-------------------")

# O range(1, 11) vai gerar os números de 1 até 10 
# (o último número no range sempre é ignorado)
for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(numero, "x", multiplicador, "=", resultado)

print("-------------------")

# O range(1, 11) vai gerar os números de 1 até 10 
# (o último número no range sempre é ignorado)
for adicao in range(1, 11):
    resultado = numero + adicao
    # CORREÇÃO AQUI: Trocado 'multiplicador' por 'adicao' no print
    print(numero, "+", adicao, "=", resultado)
