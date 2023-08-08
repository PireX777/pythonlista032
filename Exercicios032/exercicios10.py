'''10) Escreva um algoritmo pergunte o número total de eleitores de um município, o número de votos brancos, nulos
e válidos e apresente como resposta o percentual que cada um representa em relação ao total de eleitores.'''

a = int(input("Informe o total de eleitores do município: "))
b = int(input("Informe o total de votos brancos do município: "))
c = int(input("Informe o total de votos nulos do município: "))
d = int(input("Informe o total de votos validos do município: "))

percentualb = (b / a) * 100
percentualn = (c / a) * 100
percentualv = (d / a) * 100

print(f"Percentual de votos em branco: {percentualb:.2f}%")
print(f"Percentual de votos nulos: {percentualn:.2f}%")
print(f"Percentual de votos válidos: {percentualv:.2f}%")