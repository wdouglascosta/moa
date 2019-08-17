from random import randint
# Matriz quadrada com 11 cidades e as distâncias entre elas
cities = [
#      0   1   2   3   4   5    6   7    8   9  10
    [  0, 29, 20, 21, 16, 31, 100, 12,   4, 31, 18], # 0
    [ 29,  0, 15, 29, 28, 40,  72, 21,  29, 41, 12], # 1
    [ 20, 15,  0, 15, 14, 25,  81,  9,  23, 27, 13], # 2
    [ 21, 29, 15,  0,  4, 12,  92, 12,  25, 13, 25], # 3
    [ 16, 28, 14,  4,  0, 16,  94,  9,  20, 16, 22], # 4
    [ 31, 40, 25, 12, 16,  0,  95, 24,  36,  3, 37], # 5
    [100, 72, 81, 92, 94, 95,   0, 90, 101, 99, 84], # 6
    [ 12, 21,  9, 12,  9, 24,  90,  0,  15, 25, 13], # 7
    [  4, 29, 23, 25, 20, 36, 101, 15,   0, 35, 18], # 8
    [ 31, 41, 27, 13, 16,  3,  99, 25,  35,  0, 38], # 9
    [ 18, 12, 13, 25, 22, 37,  84, 13,  18, 38, 0]   # 10
]

evaluationsList = []
# Algoritmo guloso usando o vizinho mais próximo
# Generate the inicial solution for tabooSearch
def starterSolution(cities, initial=0):
    # Inicializa a rota com a cidade inicial e a distancia total com zero
    current = initial
    route = [current]
    total_distance = 0

    # Repita para o número de cidades - 1
    # A primeira cidade já foi adicionada na rota
    for _ in range(len(cities) - 1):

        # Pega a linha da matriz que representa os vizinhos da cidade atual (current)
        neighbours = cities[current]

        # Inicializa a menor distância com infinito
        best_neighbour = None
        best_distance = float("inf")

        # Para cada cidade vizinha da cidade corrente
        for idx in range(len(neighbours)):

            # Pega a distância da cidade atual para a cidade vizinha
            distance = neighbours[idx]

            # Se a cidade ainda não foi visitada e
            #  sua distância for maior que zero e
            #  sua distância for menor que a menor distância até o momento
            # então atualiza a cidade mais próxima da atual
            if idx not in route and distance > 0 and distance < best_distance:
                best_neighbour = idx
                best_distance = distance

        # Atualiza a cidade atual para o vizinho mais próxima
        # Adiciona o vizinho na rota e incrementa a distância total
        current = best_neighbour
        route.append(current)

    # Ao final, conectar a última cidade na primeira cidade
    route.append(initial)

    return (route)


teste = starterSolution(cities)


##### Métodos relacionados a busca tabu #####
# Valida a distância percorrida na rota recebida como parametro
def evaluate(solution):
    cityIndex = cities[solution[0]]
    distanceSolution = 0

    for city in solution:
        distanceSolution += cityIndex[city]
        cityIndex = cities[city]
    return distanceSolution


# inverte a posição do elemento index no array, com o proximo elemento (index + 1)
def invertTwoConsec(index, array):
    size = len(array) - 1
    aux = array[index]
    array[index] = array[index + 1]
    array[index + 1] = aux
    array[size] = array[0]
    return array

# Gera a vizinhança da solução atual, invertendo a posição de duas cidades consecutivas
def generateNeighboor(solution):

    neighborhood = []

    for i in range(20):
        node1 = 0
        node2 = 0

        while node1 == node2:
            node1 = randint(1, len(solution) - 1)
            node2 = randint(1, len(solution) - 1)

        if node1 > node2:
            swap = node1
            node1 = node2
            node2 = swap

        tmp = solution[node1:node2]
        tmp_state = solution[:node1] + tmp[::-1] + solution[node2:]
        neighborhood.append(tmp_state)

    return neighborhood

def getBestNeigh(neighborhood, tabooList, bestSol):

    toReturn = []
    aux = float("inf")

    for neighbor in neighborhood:
        if neighbor in tabooList:
            if evaluate(neighbor) < evaluate(bestSol):
                toReturn = neighbor
        else:
            aux2 = evaluate(neighbor)
            #variáveis extras criadas somente para fins de debug
            if aux2 < aux:
                aux = aux2
                toReturn = neighbor
    return toReturn


    print('erro: any neighbor was selected')


def tabooSearch(cities, BTmax, T):
    tabooList = []
    iter, bestIter = 0, 0
    starterSol = starterSolution(cities)
    bestSol = starterSol[:]

    print('the starter solution is: ', starterSol)
    print('Avaliation of starter solution: ', evaluate(starterSol))



    while (iter - bestIter) <= BTmax:
        neighborhood = generateNeighboor(starterSol)

        bestNeighbor = getBestNeigh(neighborhood, tabooList, bestSol)
        evaluation = evaluate(bestNeighbor)
        print(bestNeighbor, evaluation)
        evaluationsList.append(evaluation)

        posTaboo = bestNeighbor
        starterSol = bestNeighbor[:]

        if len(tabooList) < T:
            tabooList.append(posTaboo)
        else:
            tabooList.pop(0)
            tabooList.append(posTaboo)

        if evaluate(bestNeighbor) < evaluate(bestSol):
            bestSol = bestNeighbor[:]
            bestIter += 1
        iter += 1

    return bestSol


if __name__ == '__main__':
    bestSol = tabooSearch(cities, BTmax=10, T=13)
    print('\nMelhor Solução: ', bestSol)
    print('Avaliação da melhor solução: ', evaluate(bestSol))




    with open('trab.txt', 'w') as f:
        for value in evaluationsList:
            valueStr = str(value) + "\n"
            f.write(str(valueStr))

