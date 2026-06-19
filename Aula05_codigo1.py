print("--- SISTEMA ESCOLAR ---")
# 1. Criando um Dicionário com os dados do aluno
aluno = {
    "nome": input("Digite o nome do aluno: "),
    "disciplina": "Python Básico",
    "nota": float(input("Digite a nota final (ex: 8.5): "))
}
print("\n--- ANALISANDO RESULTADO ---")
print("Aluno:", aluno["nome"])
print("Nota:", aluno["nota"])

#2. Usando IF e ELSE para tomar uma decisão
#Se a nota for maior ou igual a 6.0, ele passar. SENÃO (else), reprova
if aluno["nota"] >= 6.0:
    print("SITUAÇÃO: APROVADO! Parabéns!")
else:
    print("SITUAÇÃO: REPROVADO. Precisa estudar mais.")

    
