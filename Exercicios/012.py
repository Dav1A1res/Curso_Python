p = float(input('Qual o preço do produto? R$'))

#desconto de 5%
pf = p - (p*5/100)

print('O produto que custava R${}, na promoção de 5% irá custar R${:.2f}'.format(p,pf))

#outra possibilidade
print('='*20)

d = int(input('Insira o valor do desconto: '))

vld = d/100

pp = float(input('Insira o preço do produto: '))

ppf = pp - (pp*vld)

print('O produto que custava R${:.2f}, na promoção de {}% irá custar R${:.2f}'.format(pp,d,ppf))


quit()
