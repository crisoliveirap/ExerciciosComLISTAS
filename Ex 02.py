# Valores únicos em uma Lista
listanum = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in listanum:
        listanum.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? ')).strip().upper()[0]
    if r == 'N':
        break

listanum.sort()
print(f'Você digitou os valores {listanum}')





