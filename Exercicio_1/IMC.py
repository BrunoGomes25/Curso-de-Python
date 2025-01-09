nome = "emily tripa seca"
peso = 65  
altura = 1.70
imc = peso / (altura * altura) 

if imc < 18.5:
    print("meu nome é",nome, "e IMC é:", int(imc),"e estou no abaixo do peso")
if (imc > 18.5) and (imc < 24.9):
    print("meu nome é",nome, "e IMC é:", int(imc),"e estou no peso ideal")
if (imc > 25.0) and (imc < 29.9):
    print("meu nome é",nome, "e IMC é:", int(imc),"e estou acima do peso")
if imc > 30:
    print("meu nome é",nome, "e IMC é:", int(imc),"e estou no obeso(a)")
