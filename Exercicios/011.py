larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

area = larg * alt

print('A dimensão da sua parede é de {:.2f}x{:.2f} e sua área é de {:.3f}m².'.format(larg, alt, area))

tinta = area / 2

print('A quantidade de tinta necessária para pintar a parede é: {:.2f}l'.format(tinta))

quit()            
