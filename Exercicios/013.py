sal = float(input('Qual é o salário do funcionário? R$'))

vlaum = float(input('Qual o valor do aumento?: '))

aum = sal + (sal*vlaum/100)

print('O funcionário que ganhava R${:.2f}, com {:.0f}% de aumento, passa a receber R${:.2f}'.format(sal, vlaum, aum))

quit()
