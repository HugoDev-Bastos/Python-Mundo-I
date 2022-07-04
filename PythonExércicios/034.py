# Escrea um programa que pergunte o sálario de um funcionario e calcule o valor do seu aumento
# PAra salários superiores a R$1.250,00, calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%.


salario = float(input('Qual é o salário do funcionário? R$: '))

if salario <= 1250:
    novo  = salario + (salario * 15 / 100)
else:
    novo  = salario + (salario * 10 / 100)
    
print('Quem ganhava R${:0.2f} passa a ganhar R${:0.2f} agora.'.format(salario, novo))