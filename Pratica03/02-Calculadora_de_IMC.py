""""
2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, 
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
"""
peso = float(input("Digite seu peso kg: "))
altura = float(input("Informe sua altura: "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")
print()

if imc < 18.5:
    status = "Abaixo do peso"
elif imc < 25:
    status = "Peso normal"
elif imc < 30:
    status = "Sobrepeso"
else:
    status = "Obesidade"

print(f"Seu IMC é {imc:.2f}. Classificação: {status}")
