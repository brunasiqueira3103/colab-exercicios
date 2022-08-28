#Exercício: Crie um programa em Python que peça dois números ao usuário.
#Em seguida, você vai mostrar a soma, subtração, multiplicação, divisão, exponenciação e resto da divisão do primeiro número pelo segundo.

num1 = int(input("digite o primeiro numero: "))
num2 = int(input("digite o segundo numero: "))

print("Soma: ", num1 + num2, "\n")
print("Subtração: ", num1 - num2, "\n")
print("multiplicação: ", num1 * num2, "\n")
print("Divisão: ", num1 / num2,"\n")
print("Exponenciação: ", num1 ** num2, "\n")
print("Resto de divisão: ", num1 % num2,"\n")

##### saída
#digite o primeiro numero: 10
#digite o segundo numero: 20
#Soma:  30                                    (+)
#Subtração:  -10                              (-)
#multiplicação:  200                          (*)
#Divisão:  0.5                                (/)
#Exponenciação:  100000000000000000000        (**)
#Resto de divisão:  10                        (%)


n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
print('Soma: {} + {} = {}'.format(n1, n2, n1+n2))
print('Subtração: {} - {} = {}'.format(n1, n2, n1-n2))
print('Multiplicação: {} * {} = {}'.format(n1, n2, n1*n2))
print('Divisão: {} / {} = {}'.format(n1, n2, n1/n2))
print('Exponenciação: {} ** {} = {}'.format(n1, n2, n1**n2))
print('Resto da divisão: {} % {} = {}'.format(n1, n2, n1%n2))

##### saída
#Digite um número: 3
#Digite outro número: 3
#Soma: 3.0 + 3.0 = 6.0
#Subtração: 3.0 - 3.0 = 0.0
#Multiplicação: 3.0 * 3.0 = 9.0
#Divisão: 3.0 / 3.0 = 1.0
#Exponenciação: 3.0 ** 3.0 = 27.0
#Resto da divisão: 3.0 % 3.0 = 0.0



