#criar uma lista com 5 clubes

clubes_de_futebol = [
    'Ibis',
    'Flamengo',
    'Perilima',
    'Volta Redonda'
    'Nacional de Patos']

#perguntar qual o clube o usuário vai verificar

clube_pesquisado = input('Digite o clube: ')

for clube in clubes_de_futebol:

    if clube == clube_pesquisado:
        print('Achei')

    else:
        print('Ainda não achei!')