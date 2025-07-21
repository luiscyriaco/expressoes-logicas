""" 5. Faça um programa que solicite o último número da placa de um veículo e 
mostre em qual dia da semana ele não pode circular em função do rodízio de veículos.
"""

# imprimindo título do programa
print("Rodízio de veículos")

# solicita o último número da placa do veículo
placa = int(input("Último dígito da placa: "))

# determina o dia da semana com base no último número da placa
#           Dia  segunda  terça  quarta  quinta  sexta
# Final da placa  1 e 2    3 e 4  5 e 6   7 e 8   9 e 0
if placa == 1 or placa == 2:
    dia = "segunda-feira"
elif placa == 3 or placa == 4:
    dia = "terça-feira"
elif placa == 5 or placa == 6:
    dia = "quarta-feira"
elif placa == 7 or placa == 8:
    dia = "quinta-feira"
elif placa == 0 or placa == 9:
    dia = "sexta-feira"

# exibe o dia de rodízio
print("Dia de rodízio:", dia)