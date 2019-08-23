# https://pt.stackoverflow.com/questions/205528/como-criar-uma-matriz-em-python
# https://stackoverflow.com/questions/17870612/printing-a-two-dimensional-array-in-python
# https://www.youtube.com/watch?v=pEH5uuC4nlw
#  pip install numpy
import numpy as np


def backpack(capacity, loads, values):
    numItens = len(loads)
    memory = np.zeros((numItens + 1, capacity +1), dtype=np.int)

    for i in range(numItens + 1):

        for j in range(capacity + 1):
            if i == 0 or j == 0:
                memory[i][j] = 0
            else:
                if loads[i -1] <= j:
                    memory[i][j] = max(values[i-1] + memory[i-1][j-loads[i-1]], memory[i-1][j])
                else:
                    memory[i][j] = memory[i-1][j]

    print(np.matrix(memory))
    return memory[numItens][capacity]


values = [1, 6, 18, 22, 28, 40, 60]
loads = [1, 2, 5, 6, 7, 9, 11]
capacity = 23
result = backpack(capacity, loads, values)

print('The biggest value is: ', result)
