""""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

Produto = "Camisa"
Preco = 50.00
PercentDesconto = 20

Desconto = Preco * (PercentDesconto/100)
PrecoFinal = Preco - Desconto

print(f"O preço do produto é: R${Preco:.2f}")
print(f"O preço do desconto é: R${Desconto:.2f}")
print(f"O preço final do produto é: R${PrecoFinal:.2f}")
print()
