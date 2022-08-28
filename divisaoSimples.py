#Júlia decidiu vender caixas com doces para recadar dinheiro e poder viajar nas férias ela comprou 12 caixas e com os ingredientes produziu
#50 brigadeiros de tá beijinhos 30 cajuzinhos e 40 bem casados 
#de acordo com a produção de Júlia quantos doces ela deve colocar em cada caixa para ser vendidos

caixas=int(input("Infome a quantidade de caixas: "))
doces=int(input("informe a quantidade de doces: "))

caixasProntas = doces // caixas

print("Cada caixa tem: ", caixasProntas, "doces")

#saída: Cada caixa tem:  10 doces
