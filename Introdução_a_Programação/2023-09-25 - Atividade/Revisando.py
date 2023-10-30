#Contexto: Avaliação de desempenho de um funcionário.
#Questão: Peça ao usuário para inserir o número de horas extras e o número de horas que o funcionário faltou.
#Se a quantidade de horas extras for maior que as horas faltadas mais 50%, imprima "Bônus de R$ 500.00".
#Caso contrário, imprima "Sem bônus".

horas_extras = float(input("Digite suas horas extras trabalhadas: "))
horas_em_falta = float(input("Digite suas horas pendentes: "))

horas = 1.5 * horas_em_falta

if horas_extras > horas:
    print('Patabéns você ganhou um bônus de R$ 500.00! ')

else:
    print('Não atigimos a meta, nesse mês você ficará sem bônus, mas quem sabe no próximo mês. ')