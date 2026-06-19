#Cria uma lista de strings chamada FRUTAS com 5 elementos
frutas = ['maça', 'banana', 'manga', 'kiwi', 'abacaxi']
print(frutas)

#Conta a quantidade de elementos na lista "frutas" e guarda a váriavel
# "total_frutas"
total_frutas = len(frutas)

# Exibe na tela o valor da variável 'total_frutas' (que é 5)
print("total de frutas na nossa lista é: ", total_frutas)

print("----------LISTA DE ALUNOS---------")
#Cria uma uma nova lista chamada "Alunos" com 5 nomes
alunos = ["Ana", "Carlos", "Maria", "Júlia", "Ricardo"]

alunos = ["Ana", "Carlos", "Maria", "Júlia", "Ricardo"]

# O \n força a quebra de linha entre os dois itens
print(f"{alunos[0]}\n{alunos[3]}") #opcional

print("--------APPEND para inserir no final da lista-----")

#INSERÇÃO: Adicionar o nome "Pedro" no final da lista
alunos.append('Pedro')

#MUDAR: muda a posição de Pedro ou de algum aluno
alunos.insert(1, "Pedro")
print(alunos)

#EXCLUSÃO: Remover um aluno da lista procurando pelo nome
#Pode colocar o nome do aluno dentro de aspas""
alunos.remove("Ana")
alunos.remove("Júlia")
print(alunos)
