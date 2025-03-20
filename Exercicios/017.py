'''
from math import sqrt
catop = float(input('Comprimento do cateto oposto: '))
catad = float(input('Comprimento do cateto adjacente: '))

hip = sqrt(catop**2 + catad**2)

print('A hipotenusa vai medir {:.2f}'.format(hip))
'''

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hip = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hip))
