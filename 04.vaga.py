""" 4. Para preencher uma vaga em uma empresa, o candidato do sexo masculino 
deverá ser brasileiro, ter 18 anos ou mais e estar em dia com o serviço militar. 
Faça um programa que solicite os dados desse candidato, faça a expressão lógica 
que verifique as três condições e determine se ele está apto ou não para assumir a vaga.
"""


# imprimindo título do programa
print("Requisitos do cargo")

# solicita dados do candidato
sexo = input("Sexo [F/M]........................ ")
nacionalidade = input("Nacionalidade..................... ")
idade = int(input("Idade............................. "))
servicoMilitar = input("Em dia com serviço militar [S/N].. ")

# verificando se o candidato está apto
if sexo == "M" and nacionalidade == "brasileiro" and idade >= 18 and servicoMilitar == "S":
    print("Apto para assumir a vaga")
else:
    print("Inapto para assumir a vaga")