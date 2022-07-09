


def cubo():
    n = input('introduce un número para elevarlo al cubo:  ')
    n = int(n)
    print(n ** 3)
    
try:
    cubo()
except ValueError:
    print('Introduce un número cojones')
