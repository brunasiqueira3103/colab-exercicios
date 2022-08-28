peso=float(input("digite seu peso: "))
peso=peso
altura=float(input("digite sua altura: "))
altura=altura
imc= peso // altura**2

if imc < 18 :
  print("vc esta abaixo do peso segundo a tabela do imc:", imc)
elif imc < 25 :
      print("você no peso ideal segundo a tabela do imc:", imc)
else:
  print("você esta acima do peso segundo a tabela do imc:", imc)
