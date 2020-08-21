from collections import deque

listaVertices = ["S", "d", "e", "p", "b", "c", "h", "r", "q", "a", "f", "G"]
listaArsitas = [(0,1), (0,2), (0,3), (1,4), (1,5), (1,2), (2,6), (2,7), (3,8), (4,9), (5,9), (6,3), (6,8), (7,10), (10,5), (10,11)]
grafo = (listaVertices, listaArsitas)

def BFS(grafo, estado_inicial, goalTest):
    listaVertices, listaArsitas = grafo
    frontera = deque()
    explorados = []
    listaAdyacentes = [[] for vertice in listaVertices]

    frontera.append(estado_inicial)

    for arista in listaArsitas:
        listaAdyacentes[arista[0]].append(arista[1])
        print(listaAdyacentes)

    while frontera:

        print("frontera")
        print(frontera)

        estado = frontera.popleft()
        explorados.append(estado)

        print("explorados")
        print(explorados)

        if goalTest==estado:
            return explorados

        auxiliar = listaVertices.index(estado)

        for vecinoIndice in listaAdyacentes[auxiliar]:
            vecino = listaVertices[vecinoIndice]
            if not vecino in explorados:
                if not vecino in frontera:
                    frontera.append(vecino)

    return 0

BFS(grafo,"S","G")