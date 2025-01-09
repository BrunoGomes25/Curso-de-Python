nome = "emily tripa seca"
peso = 65  
altura = 1.70
imc = peso / (altura * altura)

linha_1 = f'meu nome é {nome} e imc é: {imc:.2f} e estou abaixo do peso'
linha_2 = f'meu nome é {nome} e imc é: {imc:.2f} e estou no peso ideal'
linha_3 = f'meu nome é {nome} e imc é: {imc:.2f} e estou acima do peso'
linha_4 = f'meu nome é {nome} e imc é: {imc:.2f} e estou obeso(a)'

if imc < 18.5:
    print(linha_1)
if (imc > 18.5) and (imc < 24.9):
    print(linha_2)
if (imc > 25.0) and (imc < 29.9):
    print(linha_3)
if imc > 30:
    print(linha_4)
