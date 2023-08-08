''''8) Fazer um algoritmo que receba o preço de custo de um produto e mostre como resposta o valor de venda. Sabese que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário'''

pdt = int(input("Informe o valor de custo do produto: "))
pct = int(input("Informe o valor do percentual: "))

vd = pdt + (pdt * pct/100)

print(f"O valor de venda do produto é R$: {vd:.2f}")


