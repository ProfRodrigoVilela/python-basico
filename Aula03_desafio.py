# 1. Receba o nome do usuário
nome_bruto = input("Digite seu nome completo: ")

# 2. Substitua os traços por espaços
nome_sem_tracos = nome_bruto.replace("-", " ")

# 3. Converta tudo para maiúsculo
nome_cracha = nome_sem_tracos.upper()

# 4. Descubra o tamanho do nome
tamanho = len(nome_cracha)

# 5. Imprima o resultado final
print("CRACHÁ GERADO: " + nome_cracha)
print("Caracteres utilizados: ", tamanho)
