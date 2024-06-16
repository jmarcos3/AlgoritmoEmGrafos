import sys

# Definindo a matriz de adjacência usando listas
matriz_adjacencia = [
    [0, 1, 5, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 3, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 3, 1, 0, 0, 0],
    [0, 3, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 3, 2, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 5, 4, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 3],
    [0, 0, 0, 0, 0, 4, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 3, 2, 0]
]

#algoritmo de djikstra
def dijkstra(matriz, origem):
    n = len(matriz) # pega o tamanho do grafo
    dist = [sys.maxsize] * n # define a lista de distancias com  numeros "infinitos"
    dist[origem] = 0 # define a distancia de origem como sendo 0
    visitados = [False] * n # faz uma lista de vertices visitado"
    antecessores = [-1] * n # lista para "mapeamento" para os nós antecessores

    for _ in range(n):
        # seleciona o vértice não visitado com a menor distância
        min_dist = sys.maxsize # garanto que o min_dist sempre será um numero inifnito
        u = -1
        for i in range(n):
            if not visitados[i] and dist[i] < min_dist:  # se não for um nó visitado e a distancia for menor que a distancia minima
                min_dist = dist[i]  # distancia minima é a distancia em questão
                u = i # atualizo u que seria meu vértice visitado para o valord e i que é o valor "real" do vértice

        if u == -1:
            break

        visitados[u] = True # utilizando esse u eu atualizo minha de visitados
  
        # atualiza as distâncias dos vizinhos de u
        for v in range(n):
            if matriz[u][v] > 0 and not visitados[v]: # e aqui eu procuro dentro da matriz percorrendo toda a linha u
                nova_dist = dist[u] + matriz[u][v]
                #print(dist)
                if nova_dist < dist[v]: # para atualizar a lista de distancias
                    dist[v] = nova_dist # minha lista de distancia
                    antecessores[v] = u # a lista de antecessores

    print("Lista de nós visitados:", visitados)
    print("Distância do nó de origem aos outros nós do gravo:", dist) #printa a distnacia dos nó de origem aos outros nós
    print("Nós antecessores com o menor caminho possível:", antecessores)

    return dist, antecessores

# função para achar o caminho mínimo
def caminho_minimo(antecessores, destino):  
    caminho = []

    while destino != -1:  # enquanto eu não chegar no começo da lista que é -1
        caminho.append(destino) # vou atribuindo á minha lista de caminho o destino
        destino = antecessores[destino] #e vou pegando um "novo destino"
    caminho.reverse() # no final minha lista vai tá ao contrario, é necessário reverte-la

    return caminho #retorno o caminho

# Função principal para executar o programa
def encontrar_caminho_minimo():
    origem = int(input("Digite o vértice de origem (0 a 8): "))
    destino = int(input("Digite o vértice de destino (0 a 8): "))

    distancias, antecessores = dijkstra(matriz_adjacencia, origem)
    caminho = caminho_minimo(antecessores, destino)

    if distancias[destino] == sys.maxsize:
        print(f"Não há caminho disponível do vértice {origem} para o vértice {destino}.")
    else:
        print(f"Caminho mínimo do vértice {origem} para o vértice {destino}: {caminho}")
        print(f"Custo do caminho: {distancias[destino]}")

# Executar o programa
encontrar_caminho_minimo()
