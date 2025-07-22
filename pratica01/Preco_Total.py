""""
4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. 
* Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3

* O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
"""

NomeProduto = "Cadeira Infantil"
PrecoUnd = 12.40
Quant = 3

PrecoTotal = Quant * PrecoUnd

print()
print("Produto:", NomeProduto)
print(f"Preço unitário: R$ {PrecoUnd:.2f}")
print("Quantidade:", Quant)
print(f"Preço total: R$ {PrecoTotal:.2f}")
print()

