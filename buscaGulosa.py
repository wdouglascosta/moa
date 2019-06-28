# Matriz quadrada com 11 cidades e as distâncias entre elas
cities = [
#    A   B   C   D   E   F    G   H    I   J   K
  [  0, 29, 20, 21, 16, 31, 100, 12,   4, 31, 18],
  [ 29,  0, 15, 29, 28, 40,  72, 21,  29, 41, 12],
  [ 20, 15,  0, 15, 14, 25,  81,  9,  23, 27, 13],
  [ 21, 29, 15,  0,  4, 12,  92, 12,  25, 13, 25],
  [ 16, 28, 14,  4,  0, 16,  94,  9,  20, 16, 22],
  [ 31, 40, 25, 12, 16,  0,  95, 24,  36,  3, 37],
  [100, 72, 81, 92, 94, 95,   0, 90, 101, 99, 84],
  [ 12, 21,  9, 12,  9, 24,  90,  0,  15, 25, 13],
  [  4, 29, 23, 25, 20, 36, 101, 15,   0, 35, 18],
  [ 31, 41, 27, 13, 16,  3,  99, 25,  35,  0, 38],
  [ 18, 12, 13, 25, 22, 37,  84, 13,  18, 38, 0]
]


# Algoritmo guloso usando o vizinho mais próximo
def greedy_closest_neighbor(cities, initial = 0):

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
    total_distance += best_distance

  # Ao final, conectar a última cidade na primeira cidade
  route.append(initial)
  total_distance += cities[current][initial]

  return (total_distance, route)

print(greedy_closest_neighbor(cities))


##### Métodos relacionados a busca tabu #####
#def evaluate