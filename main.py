import time
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean

def generate_graph(N):
    points = np.random.rand(N, 2)
    G = nx.Graph()
    for i in range(N):
        G.add_node(i, pos=(points[i][0], points[i][1]))
        for j in range(i+1, N):
            weight = euclidean(points[i], points[j])
            G.add_edge(i, j, weight=weight)
    return G

def mst_cost(mst):
    return sum(data['weight'] for _, _, data in mst.edges(data=True))

# -------- Experimento variando N --------
Ns = [20, 40, 60, 80, 100]

times_kruskal = []
times_prim = []
costs_kruskal = []
costs_prim = []

np.random.seed(42)

for N in Ns:
    G = generate_graph(N)

    # Kruskal
    start = time.time()
    mst_k = nx.minimum_spanning_tree(G, algorithm='kruskal')
    t_k = time.time() - start
    c_k = mst_cost(mst_k)

    # Prim
    start = time.time()
    mst_p = nx.minimum_spanning_tree(G, algorithm='prim')
    t_p = time.time() - start
    c_p = mst_cost(mst_p)

    times_kruskal.append(t_k)
    times_prim.append(t_p)
    costs_kruskal.append(c_k)
    costs_prim.append(c_p)

    print(f"N={N}")
    print(f"  Kruskal -> Tempo: {t_k:.5f}s | Custo: {c_k:.4f}")
    print(f"  Prim    -> Tempo: {t_p:.5f}s | Custo: {c_p:.4f}")
    print("-" * 40)

# -------- Plot Tempo --------
plt.figure()
plt.plot(Ns, times_kruskal, marker='o', label='Kruskal')
plt.plot(Ns, times_prim, marker='o', label='Prim')
plt.xlabel("Número de Nós (N)")
plt.ylabel("Tempo (s)")
plt.title("Tempo de Execução vs N")
plt.legend()
plt.show()

# -------- Plot Custo --------
plt.figure()
plt.plot(Ns, costs_kruskal, marker='o', label='Kruskal')
plt.plot(Ns, costs_prim, marker='o', label='Prim')
plt.xlabel("Número de Nós (N)")
plt.ylabel("Custo Total da MST")
plt.title("Custo da MST vs N")
plt.legend()
plt.show()

# -------- Visualização das Árvores (para o maior N) --------
N_visual = Ns[-1]
G_visual = generate_graph(N_visual)

mst_k_visual = nx.minimum_spanning_tree(G_visual, algorithm='kruskal')
mst_p_visual = nx.minimum_spanning_tree(G_visual, algorithm='prim')

pos = nx.get_node_attributes(G_visual, 'pos')

# Kruskal
plt.figure()
nx.draw(G_visual, pos, node_size=30, alpha=0.05, edge_color='gray')
nx.draw(mst_k_visual, pos, node_size=50, edge_color='red', width=2)
plt.title(f"MST - Kruskal (N={N_visual})")
plt.show()

# Prim
plt.figure()
nx.draw(G_visual, pos, node_size=30, alpha=0.05, edge_color='gray')
nx.draw(mst_p_visual, pos, node_size=50, edge_color='blue', width=2)
plt.title(f"MST - Prim (N={N_visual})")
plt.show()
