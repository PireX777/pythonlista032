''''4) Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na
tela o valor do índice de massa corporal desta pessoa (IMC).
Fórmula: IMC = peso / altura2
 - Obs: peso em quilos e altura em metros'''

peso = int(input("Digite seu peso em quilos:"))
altura = float(input("Digite sua altura em metros:"))

ps = peso * 1000

alt = altura * 100

imc = peso / (altura **2)

print(f"O seu peso em gramas é:{ps}")
print(f"O sua altura em metros é: {alt}")
print(f"O seu indíce de massa corporal é:{imc}")
