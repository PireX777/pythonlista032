'''3) Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros'''

peso = int(input("Digite seu peso em quilos:"))
altura = float(input("Digite sua altura em metros:"))

ps = peso * 1000

alt = altura * 100

print("O seu peso em gramas é:", ps)
print("O sua altura em metros é:", alt)





