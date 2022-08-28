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
