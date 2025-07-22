""""
4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, 
incluindo o resultado final arredondado para duas casas decimais.
"""

Distancia = 300
CombustGasto = 25

KmPorLitro = Distancia / CombustGasto

print(f"Distância percorrida: {Distancia} km")
print(f"Combustível gasto: {CombustGasto} Litros")
print(f"Consumo médio do combustível é de: {KmPorLitro:.2f} km/l")
print()
