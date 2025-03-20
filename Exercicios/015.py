d = int(input('Por quantos dias o carro foi alugado? '))

vd = d * 60

km = float(input('Por quantos quilômetros o carro rodou? '))

vkm = km * 0.15

vltt = vkm + vd

#ou vltt = (d*60) + (km*0.15)

print('O total a pagar é de R${:.2f}'.format(vltt))

quit()
