#Uma empresa está realizando uma pesquisa de satisfação com seus clientes. O programa deve solicitar ao usuário a sua
#nota de satisfação com a empresa, de 1 a 5. O programa deve imprimir o número de clientes que avaliaram a empresa
#com cada nota.

from random import randint

for sorteio in range(10):
    numero = randint(1, 100)
    print(f'O numero sorteardo é: {numero}')
    