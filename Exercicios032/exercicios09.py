'''9) Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas
em dias. Obs: Considere os anos com 365 dias e os meses com 30 dias'''
idade = int(input("Informe sua idade em anos: "))
idade2 = int(input("Informe sua idade em meses: "))
idade3 = int(input("Informe sua idade em dias: "))

total_dias = (idade * 365) + (idade2 * 30) + idade3

print(f"O valor de sua idade em dias: {total_dias}")
