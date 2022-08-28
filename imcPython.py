peso=float(input("digite seu peso: "))
peso=peso
altura=float(input("digite sua altura: "))
altura=altura
imc= peso // altura**2

if imc < 18 :
  print("vc esta abaixo do peso", imc)
elif imc < 25 :
      print("você no peso ideal", imc)
else:
  print("você esta obeso, gordinho", imc)
