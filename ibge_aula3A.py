#Start Capgemini  - Lógica e Algoritmos I 
#Aula 03 - loop

porcentagemMenorIdade = float
mediaDasIdades = float
qtdMenoresIdade = float

somaIdades = 0
idadeInformada = 0
qtdEntrevistado = 0
maisNovo = 999
maisVelho = 0

while qtdEntrevistado < 5:
  idadeInformada = int(input("Informe a idade: "))

  if idadeInformada > maisVelho:
    maisVelho = idadeInformada
  if idadeInformada < maisNovo:
    maisNovo = idadeInformada
  if idadeInformada < 18:
    qtdMenoresIdade = idadeInformada
  somaIdades = somaIdades + idadeInformada
  qtdEntrevistado = qtdEntrevistado + 1


print("Mais novo tem : ", maisNovo, "de idade")
print("Mais velho tem : ", maisVelho, "de idade")

mediaDasIdades = somaIdades / 5
print("A média de idades é de : ", mediaDasIdades, "anos")

porcentagemMenorIdade = (qtdMenoresIdade / 5) * 10
print("A menores de idade é de : ", porcentagemMenorIdade, "%")
