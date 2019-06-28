from random import randint
def starterSolution(tam):
    solution = [str(randint(0,1)) for i in range(tam)]
    return ''.join(solution)



def evaluate(solution):
    return solution.count('1')

def generateNeighboor(solution):
    neighborhood = []
    tam = range(len(solution))

    for i in tam:
        list_bits = list(solution)
        list_bits[i] = '1' if solution[i] == '0' else '0'
        neighboor = ''.join(list_bits)
        neighborhood.append(neighboor)
    return neighborhood

def tabooMovement(sol, neighboor):
    for i in range(len(sol)):
        if sol[i] != neighboor[i]:
            return i
        

def getBestNeigh(neighborhood, tabooList, bestSol, solution):
    neighborhood.sort(key=evaluate, reverse=True)

    for neighbor in neighborhood:
        if tabooMovement(solution, neighbor) in tabooList:
            if evaluate(neighbor) > evaluate(bestSol):
                return neighbor
        else:
                return neighbor
    print('error: any neighbor was selected')
        
def tabooSearch(bits = 4, BTmax = 2, T= 1):
    tabooList = []
    iter, bestIter = 0, 0
    starterSol = starterSolution(bits)
    bestSol = starterSol[:]

    print('the starter solution is: ', starterSol)
    print('Avaliation of starter solution: ', evaluate(starterSol))

    while (iter - bestIter) <= BTmax:
        aval_sol = evaluate(starterSol)
        neighbor = generateNeighboor(starterSol)

        bestNeighbor = getBestNeigh(neighbor, tabooList, bestSol, starterSol)

        starterSol = bestNeighbor[:]
        posTaboo = tabooMovement(starterSol, bestNeighbor)

        if len(tabooList) < T:
            tabooList.append(posTaboo)
        else:
            tabooList.pop(0)
            tabooList.append(posTaboo)

        if evaluate(bestNeighbor) > evaluate(bestSol):
            bestSol = bestNeighbor[:]
            bestIter += 1
        iter += 1

    return bestSol

if __name__ == '__main__':
    bestSol = tabooSearch(bits=100, BTmax=1, T=1)
    print('\nMelhor Solução: ', bestSol)
    print('Avaliação da melhor solução: ', evaluate(bestSol))
