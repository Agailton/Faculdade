#Contexto: Avaliação de desempenho de um funcionário.
#Questão: Peça ao usuário para inserir o número de horas extras e o número de horas que o funcionário faltou. 
#Se a quantidade de horas extras for maior que as horas faltadas mais 50%, imprima "Bônus de R$ 500.00".
#Caso contrário, imprima "Sem bônus".

horas = int(input('Digite suas horas extras: '))
horas1 = int(input('Digite horas de falta: '))

horas = (horas1 * 1.5)

if horas > horas1:
    print('Parabéns você ganhou um Bônus de R$ 500,00! ')
else: 
    print('Sem bônus!')