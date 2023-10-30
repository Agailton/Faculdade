#Crie um programa em Python que imprima um convite para uma festa com o nome do usuário que for digitado.
#O nome do usuário precisará ser apresentado todo em caixa alta.


nome = input("Digite seu nome: ")
nome_em_caixa_alta = nome.upper()

print(f"Olá, {nome_em_caixa_alta}. você está covidado para festa!")