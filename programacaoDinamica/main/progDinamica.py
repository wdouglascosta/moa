# https://pt.stackoverflow.com/questions/205528/como-criar-uma-matriz-em-python
# https://stackoverflow.com/questions/17870612/printing-a-two-dimensional-array-in-python
# https://www.youtube.com/watch?v=pEH5uuC4nlw
#  pip install numpy
import numpy as np


def backpack(capacity, loads, values):
    # obtem a quantidade de itens
    numItens = len(loads)
    # matriz de tamanho numItens X capacity que funciona como memoria para armazenar as subsolucoes
    memory = np.zeros((numItens + 1, capacity +1), dtype=np.int)
    # for i, j para percorrer a matriz memoria
    for i in range(numItens + 1):
        for j in range(capacity + 1):
            # testa se e a primeira linha ou primeira coluna da matriz,
            # condicao de referencia
            if i == 0 or j == 0:
                memory[i][j] = 0
            else:
                # se o item i "couber" em uma mochila de capacidade j
                if loads[i -1] <= j:
                    # a memoria armazena o maior valor entre a soma do valor do item j com o valor da mochila na iteracao anterior, e o valor armazenado da iteracao anterior
                    memory[i][j] = max(values[i-1] + memory[i-1][j-loads[i-1]], memory[i-1][j])
                else:
                    # caso o valor i seja menor que o peso do item j (nao "cabe") a memoria recebe o valor da iteracao anterior
                    memory[i][j] = memory[i-1][j]
    # apenas para visualizarmos a matriz memoria
    print(np.matrix(memory))
    return memory[numItens][capacity]


# values = [1, 6, 18, 22, 28, 40, 60]
# loads = [1, 2, 5, 6, 7, 9, 11]
# capacity = 23

values = [1, 6, 18, 22, 28, 40, 60, 18, 65, 52, 41, 37, 19, 14, 35, 70, 71, 59, 62, 45]
loads = [1, 2, 5, 6, 7, 9, 11, 3, 10, 13, 15, 16, 3, 8, 12, 14, 17, 3, 5, 9]
capacity = 35

# values = [100, 60, 70, 15, 15]
# loads = [8, 3, 6, 4, 2]
# capacity = 10
result = backpack(capacity, loads, values)

print('The biggest value is: ', result)
