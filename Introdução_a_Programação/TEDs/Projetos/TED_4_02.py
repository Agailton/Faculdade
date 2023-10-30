#Problema: As maçãs custam R$ 1,30 cada, se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12.
#Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

numero_de_maça = int(input('Digite a quantidade de maça que você deseja comprar: '))

preco_por_unidade = 1.00

if numero_de_maça < 12:
    preco_por_unidade = 1.30

custo_total = numero_de_maça * preco_por_unidade

print(f'O custo total da sua compra é: {custo_total}')