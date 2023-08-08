'''1) Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o
valor com o acréscimo dos 10% da gorjeta do garçom'''

vl = int(input("Informe o valor da conta a ser pago:"))

acres = vl * 10/100

print("o valor da conta + 15% do garçom é:", (vl + acres))
