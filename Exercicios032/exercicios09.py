'''9) Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas
em dias. Obs: Considere os anos com 365 dias e os meses com 30 dias'''

id = int(input("Informe sua idade em anos: "))
id2 = int(input("Informe sua idade em meses: "))
id3 = int(input("Informe sua idade em dias: "))

id4 = 365 * id
ida2 = 30 * id2
idt = id4 + ida2 + id3

print(f"O valor de sua idade em dias: {idt}")
