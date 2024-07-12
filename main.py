import networkx as nx
import matplotlib.pyplot as plt

import pandas as pd


# Ler a matriz de adjacência do arquivo CSV
df = pd.read_csv('insertcsvhere.csv', index_col=0)

# Converter o DataFrame para uma matriz numpy
adj_matrix = df.values

# Criar o grafo a partir da matriz de adjacência
G = nx.from_numpy_matrix(adj_matrix)

# Renomear os nós para corresponder às etiquetas do CSV
labels = df.index
mapping = {i: label for i, label in enumerate(labels)}
G = nx.relabel_nodes(G, mapping)

# Desenhar o grafo
nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold')
plt.show()

# Calcular o grau médio
average_degree = sum(dict(G.degree()).values()) / len(G.nodes())
print(f"Grau médio: {average_degree}")

# Calcular a complexidade (ciclos)
# Complexidade de um grafo é dada por M - N + 1 (para grafos conexos),
# onde M é o número de arestas e N é o número de nós.
num_edges = G.number_of_edges()
num_nodes = G.number_of_nodes()
complexity = num_edges - num_nodes + nx.number_connected_components(G)
print(f"Complexidade (número de ciclos): {complexity}")

# Calcular o número de componentes conexas
num_components = nx.number_connected_components(G)
print(f"Número de componentes conexas: {num_components}")
