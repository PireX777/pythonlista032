''''5) Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois
números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a
multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão
do primeiro pelo segundo número'''
num1 = int(input("Informe um número A:"))
num2 = int(input("Informe um número B:"))

soma = num1 + num2
sub = num1 - num2
sub2 = num2 - num1
div = num1 / num2
mul = num1 * num2
res = num1 % num2

print(f"A soma dos dois números é: {soma}")
print(f"A subtração do primeiro pelo segundo número é:{sub}")
print(f"A divisão do primeiro pelo segundo número é:{div}")
print(f"A subtração do segundo pelo primeiro número é:{sub2}")
print(f"A multiplicação dos dois números é:{mul}")
print(f"O resto da divisão do primeiro pelo segundo número é:{res}")
