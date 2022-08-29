#IBGE familiar hahaha 
#Quem é o mais velho da familia, o mais novo, e porcentagem de masculino e feminino. (2 casais)


mediaDasIdades = float
porcentagemMasculina = float
porcentagemFeminina = float

sexoInformadoM = 0
sexoInformadoF = 0
sexoMasculino = 0
sexoFeminino = 0

idadeInformada = 0
somaIdades = 0
maisVelho = 0
maisNovo = 999

familia = 0

while familia < 4:
  idadeInformada = int(input("informe sua idade: "))
  sexoInformadoM = float(input("informe sexo: Masculino digite (1) para sim / e  (0) para não > "))
  sexoInformadoF = float(input("informe sexo: Feminino digite (1) para sim / e  (0) para não > "))
  familia = familia + 1
  if idadeInformada > maisVelho:
    maisVelho = idadeInformada
  if idadeInformada < maisNovo:
    maisNovo = idadeInformada
  if sexoInformadoM == 1:
    sexoMasculino = sexoMasculino + 1
  if sexoInformadoF == 1:
    sexoFeminino = sexoFeminino + 1

  somaIdades = somaIdades + idadeInformada
  

mediaDasIdades = somaIdades / 4
porcentagemMasculina = (sexoMasculino / 4) * 100
porcentagemFeminina = (sexoFeminino / 4) * 100

print("/n", "Resultados")

print("A média das idades é de: ", mediaDasIdades, "anos")
print("O mais velho da Família tem: ", maisVelho, "anos")
print("O mais novo da Família tem: ", maisNovo, "anos")
print("A porcentagem de Homens na Família é de: ", porcentagemMasculina, "%")
print("A porcentagem de mulheres na Família é de: ", porcentagemFeminina, "%")


