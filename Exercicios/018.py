import math
a = float(input('Digite o ângulo que você deseja: '))

sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))

print('O ângulo de {:.1f} tem o SENO de {:.2f}, o COSSENO de {:.2f}, e a TANGENTE de {:.2f}'.format(a, sen, cos, tan))
