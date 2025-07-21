""" 2. Um banco concederá um crédito especial aos seus clientes de acordo com o 
saldo médio do último ano. Faça um programa que solicite o saldo do médio do cliente, 
calcule o valor do crédito e exiba uma mensagem com saldo médio e o valor do crédito. 
Utilize a tabela a seguir como referência.

	 Saldo médio		Percentual do saldo médio
	 De 0 a 100			    0%
	De 101 a 200			10%
	De 201 a 300			20%
	Acima de 301			30%
"""

# Imprimindo o nome do programa
print("Crédito Especial\n")

saldo_medio = float(input("Saldo médio...... "))

# Verificando o percentual de crédito com base no saldo médio
if saldo_medio >= 0 and saldo_medio <= 100:
   percentual = 0.0
elif saldo_medio >= 101 and saldo_medio <= 200:
   percentual = 10.0
elif saldo_medio >= 201 and saldo_medio <= 300:
   percentual = 20.0
elif saldo_medio >= 301:
   percentual = 30.0
   
# Calculando o crédito
if percentual > 0.0:
    credito = saldo_medio * percentual / 100

# Apresenta os resultados ao usuário
print(f"Percentual....... {percentual:.2f}")
print(f"Valor do crédito. {credito:.2f}")