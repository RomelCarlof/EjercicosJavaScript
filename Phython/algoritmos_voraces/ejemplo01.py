import heapq

# Implementación de Prim básico (O(n^2)) usando matriz de adyacencia
def prim_basico(matrix):
    n = len(matrix)
    selected = [False] * n
    # key[i] almacena el peso mínimo para conectar i al MST
    key = [float('inf')] * n
    parent = [-1] * n  # parent[i] será el padre de i en el MST
    key[0] = 0  # Iniciar desde el vértice 0

    for _ in range(n):
        # Seleccionar el vértice no seleccionado con la clave mínima
        u = min((v for v in range(n) if not selected[v]), key=lambda v: key[v])
        selected[u] = True

        # Actualizar las claves de los vértices adyacentes a u
        for v in range(n):
            if matrix[u][v] is not None and not selected[v] and matrix[u][v] < key[v]:
                key[v] = matrix[u][v]
                parent[v] = u

    # Construir lista de aristas del MST
    mst_edges = []
    total_weight = 0
    for v in range(1, n):
        if parent[v] != -1:
            mst_edges.append((parent[v], v, matrix[parent[v]][v]))
            total_weight += matrix[parent[v]][v]

    return mst_edges, total_weight

# Implementación de Prim optimizado (O(E log V)) usando lista de adyacencia y heap
def prim_optimizado(adj_list):
    n = len(adj_list)
    visited = [False] * n
    mst_edges = []
    total_weight = 0

    # Min-heap de (peso, nodo_origen, nodo_destino)
    heap = [(0, -1, 0)]  # Empezamos desde el nodo 0, sin origen real
    while heap:
        peso, u, v = heapq.heappop(heap)
        if visited[v]:
            continue
        visited[v] = True
        if u != -1:
            mst_edges.append((u, v, peso))
            total_weight += peso

        # Añadir aristas adyacentes de v al heap
        for vecino, w in adj_list[v]:
            if not visited[vecino]:
                heapq.heappush(heap, (w, v, vecino))

    return mst_edges, total_weight

# Definimos un grafo de ejemplo con 5 vértices
# Matriz de adyacencia: None significa sin arista directa
matrix = [
    [None, 2,    None, 6,    None],
    [2,    None, 3,    8,    5   ],
    [None, 3,    None, None, 7   ],
    [6,    8,    None, None, 9   ],
    [None, 5,    7,    9,    None]
]

# Lista de adyacencia equivalente
adj_list = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)]
}

# Ejecutar ambos algoritmos en el grafo de ejemplo
mst_basic, weight_basic = prim_basico(matrix)
mst_opt, weight_opt = prim_optimizado(adj_list)

# Mostrar resultados
print("Prim básico (O(n^2)) - MST aristas y peso total:")
for u, v, w in mst_basic:
    print(f"  {u} - {v} (peso {w})")
print(f"Peso total: {weight_basic}\n")

print("Prim optimizado (O(E log V)) - MST aristas y peso total:")
for u, v, w in mst_opt:
    print(f"  {u} - {v} (peso {w})")
print(f"Peso total: {weight_opt}")

