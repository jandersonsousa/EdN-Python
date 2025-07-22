""""
1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""
ValorReais = 100.00
TaxaDolar = 5.20
TaxaEuro = 6.15

ValorDolar = ValorReais / TaxaDolar
ValorEuro = ValorReais / TaxaEuro

print(f"O valor de R$: {ValorReais} em Dólares é $: {ValorDolar:.2f}")
print()
print(f"O valor de R$: {ValorReais} em Euros é $: {ValorEuro:.2f}")
print()