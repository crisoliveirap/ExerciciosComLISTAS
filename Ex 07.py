# Matriz de dimensão 3x3 (Parte 2)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
maior_valor = 0
soma_coluna = 0
for r in range(0, 3):
    for c in range(0, 3):
        matriz[r][c] = int(input(f'Digite um valor para [{r}, {c}]: '))
print('-=' * 30)
for r in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[r][c]:^5}]', end='')
        if matriz[r][c] % 2 == 0:
            soma_pares += matriz[r][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {soma_pares}')
for r in range(0, 3):
    soma_coluna += matriz[r][2]
print(f'A soma dos valores da terceira coluna é {soma_coluna}')
for c in range(0, 3):
    if c == 0:
        maior_valor = matriz[1][c]
    elif matriz[1][c] > maior_valor:
        maior_valor = matriz[1][c]
print(f'O maior valor da segunda linha é {maior_valor}')
