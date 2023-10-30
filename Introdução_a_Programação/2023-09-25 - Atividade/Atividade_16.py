#Uma empresa está realizando uma pesquisa de satisfação com seus clientes. O programa deve solicitar ao usuário a 
#sua nota de satisfação com a empresa, de 1 a 5. O programa deve imprimir o número de clientes que avaliaram a empresa 
#com cada nota.

from random import randint

numero_clientes = 1000
lista_de_respostas = []

while numero_clientes > 0:
    lista_de_respostas.append(randint(1, 5))
    numero_clientes -= 1

respostas_1 = lista_de_respostas.count(1)
respostas_2 = lista_de_respostas.count(2)
respostas_3 = lista_de_respostas.count(3)
respostas_4 = lista_de_respostas.count(4)
respostas_5 = lista_de_respostas.count(5)

print(f'Quantidade de resposta 1: {respostas_1}')
print(f'Quantidade de resposta 1: {respostas_2}')
print(f'Quantidade de resposta 1: {respostas_3}')
print(f'Quantidade de resposta 1: {respostas_4}')
print(f'Quantidade de resposta 1: {respostas_5}')