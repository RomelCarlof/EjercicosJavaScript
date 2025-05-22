class UnionFind:
    def __init__(self, usuarios):
        self.parent = {u: u for u in usuarios}
        self.rank = {u: 0 for u in usuarios}
        self.count = len(usuarios)  # número de componentes conectados

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # compresión de caminos
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            self.count -= 1  # Reducimos el número de componentes al unir
            return True
        return False

def momento_conectividad_total(eventos, usuarios):
    uf = UnionFind(usuarios)
    for timestamp, u1, u2 in eventos:
        uf.union(u1, u2)
        if uf.count == 1:
            return timestamp  # Todos conectados en este momento
    return None  # No se logró conectar a todos

# Ejemplo de uso
eventos = [
    ("2024-05-31 12:01:00", "A", "B"),
    ("2024-05-31 12:10:00", "A", "G"),
    ("2024-05-31 13:00:00", "B", "C"),
    ("2024-05-31 15:00:00", "G", "H"),
    ("2024-05-31 17:00:00", "C", "H")
]

usuarios = {"A", "B", "C", "G", "H"}

resultado = momento_conectividad_total(eventos, usuarios)
if resultado:
    print("El momento en que todos los usuarios están conectados es:", resultado)
else:
    print("No todos los usuarios se conectaron en los eventos dados.")
