import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.colors as mcolors

# Ler a matriz de adjacência do arquivo CSV
df = pd.read_csv('https://www.dropbox.com/scl/fi/baabpgdo8yzljc8u6ypxg/Grafo-Metro-CR-Matriz-adjacencia-1.csv?rlkey=x0o584wo3zjydcwmxjp08mcj6&st=sku1n8np&dl=1', index_col=0)

# Converter o DataFrame para uma matriz numpy
adj_matrix = df.values

# Criar o grafo a partir da matriz de adjacência
G = nx.from_numpy_array(adj_matrix)

# Renomear os nós para corresponder às etiquetas do CSV
labels = df.index
mapping = {i: label for i, label in enumerate(labels)}
G = nx.relabel_nodes(G, mapping)

# Gerar posições com spring_layout com uma semente para resultados reproduzíveis
pos = nx.spring_layout(G, seed=100, k=1.5)

# Ajustar manualmente as posições dos nós para aumentar o espaçamento
pos_new = {}
scale_factor = 10.0  # Fator de escala para aumentar o espaçamento

for node, (x, y) in pos.items():
    pos_new[node] = (x * scale_factor, y * scale_factor)

node_colors = {
    'V1': (0, 0, 1, 1),   # azul
    'V2': (0, 0, 1, 1),   # azul
    'V3': (0, 0, 1, 1),   # azul
    'V4': (0, 0, 1, 1),   # azul
    'V5': (0, 0, 1, 1),   # azul
    'V6': (0, 0, 1, 1),   # azul
    'V7': (0, 0, 1, 1),   # azul
    'V8': (0, 0, 1, 1),   # azul
    'V9': (0, 0, 1, 1),   # azul
    'V10': (0, 0, 1, 1),  # azul
    'V11': (0, 0, 1, 1),  # azul
    'V12': (0, 0, 1, 1),  # azul
    'V13': (0, 0, 1, 1),  # azul
    'V14': (0, 0, 1, 1),  # azul
    'V15': (0, 0, 1, 1),  # azul
    'V16': (0, 0, 1, 1),  # azul
    'V17': (0, 0, 1, 1),  # azul
    'V18': (0, 0, 1, 1),  # azul
    'V19': (0, 0, 1, 1),  # azul
    'V20': (0, 0, 1, 1),  # azul
    'V21': (0, 0, 1, 1),  # azul
    'V22': (0, 0, 1, 1),  # azul
    'V23': (0, 0, 1, 1),  # azul
    'V24': (0, 1, 0, 1),  # verde
    'V25': (0, 1, 0, 1),  # verde
    'V26': (0, 1, 0, 1),  # verde
    'V27': (0, 1, 0, 1),  # verde
    'V28': (0, 1, 0, 1),  # verde
    'V29': (0, 1, 0, 1),  # verde
    'V30': (0, 1, 0, 1),  # verde
    'V31': (0, 1, 0, 1),  # verde
    'V32': (0, 1, 0, 1),  # verde
    'V33': (0, 1, 0, 1),  # verde
    'V34': (0, 1, 0, 1),  # verde
    'V35': (0, 1, 0, 1),  # verde
    'V36': (1, 0, 0, 1),  # vermelho
    'V37': (1, 0, 0, 1),  # vermelho
    'V38': (1, 0, 0, 1),  # vermelho
    'V39': (1, 0, 0, 1),  # vermelho
    'V40': (1, 0, 0, 1),  # vermelho
    'V41': (1, 0, 0, 1),  # vermelho
    'V42': (1, 0, 0, 1),  # vermelho
    'V43': (1, 0, 0, 1),  # vermelho
    'V44': (1, 0, 0, 1),  # vermelho
    'V45': (1, 0, 0, 1),  # vermelho
    'V46': (1, 0, 0, 1),  # vermelho
    'V47': (1, 0, 0, 1),  # vermelho
    'V48': (1, 0, 0, 1),  # vermelho
    'V49': (1, 0, 0, 1),  # vermelho
    'V50': (1, 0, 0, 1),  # vermelho
    'V51': (1, 0, 0, 1),  # vermelho
    'V52': (1, 0, 0, 1),  # vermelho
    'V53': (1, 1, 0, 1),  # amarelo
    'V54': (1, 1, 0, 1),  # amarelo
    'V55': (1, 1, 0, 1),  # amarelo
    'V56': (1, 1, 0, 1),  # amarelo
    'V57': (1, 1, 0, 1),  # amarelo
    'V58': (1, 1, 0, 1),  # amarelo
    'V59': (1, 1, 0, 1),  # amarelo
    'V60': (1, 1, 0, 1),  # amarelo
    'V61': (1, 1, 0, 1),  # amarelo
    'V62': (0.5, 0, 0.5, 1),  # roxo
    'V63': (0.5, 0, 0.5, 1),  # roxo
    'V64': (0.5, 0, 0.5, 1),  # roxo
    'V65': (0.5, 0, 0.5, 1),  # roxo
    'V66': (0.5, 0, 0.5, 1),  # roxo
    'V67': (0.5, 0, 0.5, 1),  # roxo
    'V68': (0.5, 0, 0.5, 1),  # roxo
    'V69': (0.5, 0, 0.5, 1),  # roxo
    'V70': (0.5, 0, 0.5, 1),  # roxo
    'V71': (0.5, 0, 0.5, 1),  # roxo
    'V72': (0.5, 0, 0.5, 1),  # roxo
    'V73': (0.5, 0, 0.5, 1),  # roxo
    'V74': (0.5, 0, 0.5, 1),  # roxo
    'V75': (0.5, 0, 0.5, 1),  # roxo
    'V76': (0.5, 0, 0.5, 1),  # roxo
    'V77': (0.5, 0, 0, 1),  # rubi
    'V78': (0.5, 0, 0, 1),  # rubi
    'V79': (0.5, 0, 0, 1),  # rubi
    'V80': (0.5, 0, 0, 1),  # rubi
    'V81': (0.5, 0, 0, 1),  # rubi
    'V82': (0.5, 0, 0, 1),  # rubi
    'V83': (0.5, 0, 0, 1),  # rubi
    'V84': (0.5, 0, 0, 1),  # rubi
    'V85': (0.5, 0, 0, 1),  # rubi
    'V86': (0.5, 0, 0, 1),  # rubi
    'V87': (0.5, 0, 0, 1),  # rubi
    'V88': (0.5, 0, 0, 1),  # rubi
    'V89': (0.5, 0, 0, 1),  # rubi
    'V90': (0.5, 0, 0, 1),  # rubi
    'V91': (0.5, 0, 0, 1),  # rubi
    'V92': (0.5, 0, 0, 1),  # rubi
    'V93': (0.66, 0.66, 0.66, 1),  # cinza escuro
    'V94': (0.66, 0.66, 0.66, 1),  # cinza escuro
    'V95': (0.66, 0.66, 0.66, 1),  # cinza escuro
    'V96': (0.66, 0.66, 0.66, 1),  # cinza escuro
    'V97': (0.66, 0.66, 0.66, 1),  # cinza escuro
    'V98': (0.66, 0.66, 0.66, 1),  # cinza escuro
    'V99': (0.66, 0.66, 0.66, 1),  # cinza escuro
    'V100': (0.66, 0.66, 0.66, 1), # cinza escuro
    'V101': (0.66, 0.66, 0.66, 1), # cinza escuro
    'V102': (0.66, 0.66, 0.66, 1), # cinza escuro
    'V103': (0.66, 0.66, 0.66, 1), # cinza escuro
    'V104': (0.66, 0.66, 0.66, 1), # cinza escuro
    'V105': (0.66, 0.66, 0.66, 1), # cinza escuro
    'V106': (0.66, 0.66, 0.66, 1), # cinza escuro
    'V107': (0.66, 0.66, 0.66, 1), # cinza escuro
    'V108': (0.66, 0.66, 0.66, 1), # cinza escuro
    'V109': (0.66, 0.66, 0.66, 1), # cinza escuro
    'V110': (0.66, 0.66, 0.66, 1), # cinza escuro
    'V111': (0.66, 0.66, 0.66, 1), # cinza escuro
    'V112': (0.66, 0.66, 0.66, 1), # cinza escuro
    'V113': (0.66, 0.66, 0.66, 1), # cinza escuro
    'V114': (0, 1, 1, 1),  # verde-água
    'V115': (0, 1, 1, 1),  # verde-água
    'V116': (0, 1, 1, 1),  # verde-água
    'V117': (0, 1, 1, 1),  # verde-água
    'V118': (0, 1, 1, 1),  # verde-água
    'V119': (0, 1, 1, 1),  # verde-água
    'V120': (0, 1, 1, 1),  # verde-água
    'V121': (0, 1, 1, 1),  # verde-água
    'V122': (0, 1, 1, 1),  # verde-água
    'V123': (0, 1, 1, 1),  # verde-água
    'V124': (0, 1, 1, 1),  # verde-água
    'V125': (0, 1, 1, 1),  # verde-água
    'V126': (0, 1, 1, 1),  # verde-água
    'V127': (0, 1, 1, 1),  # verde-água
    'V128': (0, 1, 1, 1),  # verde-água
    'V129': (0, 1, 1, 1),  # verde-água
    'V130': (0, 0.75, 0.75, 1),  # turquesa
    'V131': (0, 0.75, 0.75, 1),  # turquesa
    'V132': (0, 0.75, 0.75, 1),  # turquesa
    'V133': (0, 0.75, 0.75, 1),  # turquesa
    'V134': (0, 0.75, 0.75, 1),  # turquesa
    'V135': (0, 0.75, 0.75, 1),  # turquesa
    'V136': (0, 0.75, 0.75, 1),  # turquesa
    'V137': (0, 0.75, 0.75, 1),  # turquesa
    'V138': (0, 0.75, 0.75, 1),  # turquesa
    'V139': (0, 0.75, 0.75, 1),  # turquesa
    'V140': (0, 0.75, 0.75, 1),  # turquesa
    'V141': (1, 0.65, 0, 1),  # laranja
    'V142': (1, 0.65, 0, 1),  # laranja
    'V143': (1, 0.65, 0, 1),  # laranja
    'V144': (1, 0.65, 0, 1),  # laranja
    'V145': (1, 0.65, 0, 1),  # laranja
    'V146': (1, 0.65, 0, 1),  # laranja
    'V147': (1, 0.65, 0, 1),  # laranja
    'V148': (1, 0.65, 0, 1),  # laranja
    'V149': (1, 0.65, 0, 1),  # laranja
    'V150': (1, 0.65, 0, 1),  # laranja
    'V151': (1, 0.65, 0, 1),  # laranja
    'V152': (1, 0.65, 0, 1),  # laranja
    'V153': (0.15, 0.35, 0.55, 1),  # safira
    'V154': (0.15, 0.35, 0.55, 1),  # safira
    'V155': (0.15, 0.35, 0.55, 1),  # safira
    'V156': (0.15, 0.35, 0.55, 1),  # safira
    'V157': (0.15, 0.35, 0.55, 1),  # safira
    'V158': (0.15, 0.35, 0.55, 1),  # safira
    'V159': (0.15, 0.35, 0.55, 1),  # safira
    'V160': (0.15, 0.35, 0.55, 1),  # safira
    'V161': (0.15, 0.35, 0.55, 1),  # safira
    'V162': (0.15, 0.35, 0.55, 1),  # safira
    'V163': (0.0, 0.5, 0.0, 1),  # jade
    'V164': (0.0, 0.5, 0.0, 1),  # jade
    'V165': (0.66, 0.66, 0.66, 1),  # cinza claro
    'V166': (0.66, 0.66, 0.66, 1),  # cinza claro
    'V167': (0.66, 0.66, 0.66, 1),  # cinza claro
    'V168': (0.66, 0.66, 0.66, 1),  # cinza claro
    'V169': (0.66, 0.66, 0.66, 1),  # cinza claro
    'V170': (0.66, 0.66, 0.66, 1),  # cinza claro
    'V171': (0.66, 0.66, 0.66, 1),  # cinza claro
    'V172': (0.66, 0.66, 0.66, 1),  # cinza claro
    'V173': (0.66, 0.66, 0.66, 1),  # cinza claro
    'V174': (0.66, 0.66, 0.66, 1)   # cinza claro
}

# Gerar uma lista de cores para todos os nós
colors = [node_colors.get(node, 'lightblue') for node in G.nodes()]

# Ajustar a largura e a altura da figura
plt.figure(figsize=(20, 15))

# Desenhar o grafo
nx.draw(G, pos, with_labels=True, node_color=colors, font_weight='bold', node_size=700, font_size=8, edge_color='gray', width=2.0)

plt.show()
