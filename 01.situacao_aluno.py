""" 1. Para ser aprovado em uma instituição de ensino, o aluno precisa de nota 
igual ou superior a 50 e a quantidade de faltas deve ser igual ou menor do que 15. 
Faça um programa que solicite nota e falta do aluno e verifique se ele está aprovado ou reprovado.
"""

#imprimindo o nome do programa
print("Situação do aluno\n")

nota = int(input("Nota [0 a 100]... "))
falta = int(input("Falta(s)......... "))

# Verificando a situação do aluno
if nota >= 50 and falta < 15:
    situacao = "Aluno aprovado"
else:
   situacao = "Aluno reprovado"

# Exibindo a situação do aluno
print(situacao)
