#Faça um algoritmo que leia o sálario de um funcionário e mostre seu novo sálario com 15% de aumento.

salario = float(input(">>> Qual o Salário do Funcionário? R$"))
novo = salario + (salario * 15/100)

print('='*50)
print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))
print('='*50)