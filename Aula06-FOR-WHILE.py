# Exemplo 1: Usando o FOR com a função range()
print("--- CONTAGEM REGRESSIVA (FOR) ---")

# O range(5, 0, -1) conta de 5 até 1, diminuindo 1 por vez
for numero in range(5, 0, -1):
    print("Faltam", numero, "segundos!")
print("Fogo! 🚀\n")
#Exemplo 2: Usando o WHILE com o comando BREAK
print("--- SISTEMA DE SENHA (WHILE) ---")
while True:
    senha = input("Digite uma senha secreta(ou SAIR para fechar): ")
    if senha == "1234@":
        print("Acesso permitido! Bem-vindo")
        break #O break interrompe e destroi o loop imediatamente
    elif senha == "sair":
        print("Encerrando o programa")
        break
    else:
        print("Senha incorreta, tente novamente.\n")
print("----------------------------------")
