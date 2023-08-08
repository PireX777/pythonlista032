''''6) Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final
do mês'''
input("Qual o seu nome?")
sl =int(input("Qual o valor do seu salário fixo?"))
vd =int(input("Qual foi o total de vendas feitas no mês(em dinheiro)?"))
c = vd + (vd* 0.15)
tt = sl + c

print(f"O valor total do seu salário é: {tt}")
print(f"Salário bruto R$ {sl}")
print(f"total de vendas em R$: {vd}")
print(f"A comissão do vendeor R$: {c}")


