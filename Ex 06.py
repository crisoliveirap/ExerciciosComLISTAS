# Matriz de dimensão 3x3
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for r in range(0, 3):
    for c in range(0, 3):
        matriz[r][c] = int(input(f'Digite um valor para [{r}, {c}]: '))
for r in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[r][c]:^5}]', end='')
    print()
