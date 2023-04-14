print("\n\nComprovante de sálario.")
salarioMinimo = 1320

print("\nM = Matutino;")
print("V = Vespertino;")
print("N = Noturno.")
turnoDeTrabalho = str(input("\nInforme-nos seu turno trabalhado: ")).upper()

if turnoDeTrabalho == "M" or turnoDeTrabalho == "V" or turnoDeTrabalho == "N":
    print("\nO = Operário")
    print("G = Gerente")
    cargo = str(input("Informe seu cargo de trabalho: ")).upper()
    
    if cargo == "O" or cargo == "G": 
        
        horasTrabalhadas = int(input("\nInforme sua carga horario mensal: "))
        
        if horasTrabalhadas > 0:
            if turnoDeTrabalho == "M":
                coeficiente = 0.10/100 * salarioMinimo 
            elif turnoDeTrabalho == "V":
                coeficiente = 0.15/100 * salarioMinimo 
            elif turnoDeTrabalho == "N":
                coeficiente = 0.12/100 * salarioMinimo 
                
            salarioBruto = horasTrabalhadas * coeficiente
            
            if cargo == "O" and salarioBruto >= 300:
                imposto = 5/100 * salarioBruto
            elif cargo == "O" and salarioBruto < 300:
                imposto = 3/100 * salarioBruto
            elif cargo == "G" and salarioBruto >= 400:
                imposto = 6/100 * salarioBruto
            elif cargo == "G" and salarioBruto < 400:
                imposto = 4/100 * salarioBruto
            
            if turnoDeTrabalho == "N" and horasTrabalhadas > 80:
                gratificacao = 50
                print("Você recebeu uma gratificação de R$ 50,00")
            else: 
                gratificacao = 30
                print("Você recebeu uma gratificação de R$ 30,00")
                
            if cargo == "O" or coeficiente <= 25:
                auxulioAlimentacao = 50
                print("Seu auxilio alimentação é de R${:,.2f}".format(auxulioAlimentacao))
            else: 
                auxulioAlimentacao = 30
                print("Seu auxilio alimentação é de: R${:,.2f}".format(auxulioAlimentacao))
                
            salarioLiquido = salarioBruto - imposto + gratificacao + auxulioAlimentacao
            
            if salarioLiquido < 350:
                print("Seu salaário é de R${:,.2f}".format(salarioLiquido),", você está sendo MAL REMUNERADO!")
            elif salarioLiquido > 350 and salarioLiquido <= 600:
                print("Seu salaário é de R${:,.2f}".format(salarioLiquido),"seu sálario é considerado NORMAL!")
            else:
                print("Seu salaário é de R${:,.2f}".format(salarioLiquido),"você está sendo BEM REMUNERADO!")
                
        else:
            print("\nCARGA HORÁRIA INVÁLIDA!")
    else:
        print("\nERRO, INFORME UM CARGO VÁLIDO!")
else: 
    print("\nERRO, INFORME UM TURNO DE TRABALHO VÁLIDO")