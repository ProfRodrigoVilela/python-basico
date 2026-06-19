# --- LIVE CODE: Dicionários e Condicionais (IF/ELSE) ---

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

# 2. Usando IF e ELSE para tomar uma decisão
# Se a nota for maior ou igual a 6.0, ele passa. Senão (else), reprova.
if aluno["nota"] >= 6.0:
    print("SITUAÇÃO: APROVADO! Parabéns!")
else:
    print("SITUAÇÃO: REPROVADO. Precisa estudar mais.")
   
print("----------------------------")


print("\n-----------------------------------------")
print("        CABEÇALHO GERAL         ")
print("-------------------------------------------")
# Usando as F-Strings e acessando as chaves do dicionário
#
print(f"👤 Aluno(a): {aluno['nome']}")
print(f"📚 Disciplina: {aluno['disciplina']}")
print(f"🎯 Nota Final: {aluno['nota']}")


from datetime import datetime
data_formatada = datetime.now().strftime("%d/%m/%Y")
# Usando f-string para juntar o texto com a variável
print(f"📅Data {data_formatada}")
# Saída: Data 16/06/2026
print("-------------------------------------------")




