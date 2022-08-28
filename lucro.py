#Um comerciante quer vender seus produtos com um lucro de 45% caso o valor da compra for menor que R$30,00. 
#Caso contrário, o lucro deverá ser de 30%. Faça um programa que recebe o valor do produto e devolve o valor da venda.


compra = int((input("informe valor da compra: ")))

valorDeReferencia =  30

if compra <= valorDeReferencia:
  produtoComLucro45 = compra * 1.45
  print('produto deve ser vendido por: ', produtoComLucro45, "reais")
else:
  produtoComLucro30 = compra * 1.30
  print('produto deve ser vendido por: ', produtoComLucro30, "reais")

### saída
#informe valor da compra: 50
#produto deve ser vendido por:  65.0 reais
