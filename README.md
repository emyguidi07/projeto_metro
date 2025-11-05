# 🚇 Análise de Grafos — Conectividade da Rede de Metrô de São Paulo

Projeto desenvolvido para a disciplina **Comunicação e Redes**, da **Universidade Federal do ABC (UFABC)**.  
O objetivo foi **analisar a conectividade e as propriedades estruturais** da rede de metrô da cidade de **São Paulo** por meio da **teoria dos grafos**, utilizando **Python** e o pacote **NetworkX**.

---

## 🎯 Objetivo do Projeto

O estudo buscou compreender a **estrutura de conectividade** da rede metroviária de São Paulo — considerada um sistema complexo de transporte urbano — através de **métricas quantitativas e qualitativas** de teoria dos grafos.

Mais especificamente, o projeto teve como metas:

- Modelar o **metrô de São Paulo** como um **grafo não direcionado**;  
- Calcular **métricas topológicas** (grau médio, diâmetro, centralidade, etc.);  
- Avaliar **a robustez da rede** frente a falhas e desconexões;  
- Explorar **visualizações** que evidenciem **os pontos críticos e de maior importância** para a conectividade geral.

---

## 🧠 Fundamentação Teórica

A **teoria dos grafos** permite representar redes de comunicação, transporte e informação de maneira abstrata, onde:

- **Nós (vértices)** representam estações do metrô;  
- **Arestas** representam conexões diretas (trechos) entre as estações.

A partir dessa estrutura, é possível calcular métricas que revelam:
- **Conectividade** (quão interligada é a rede);  
- **Centralidade** (estações mais importantes para o fluxo);  
- **Eficiência global** (quantidade média de conexões entre dois nós);  
- **Vulnerabilidade** (impacto da remoção de um nó na rede).

---

## 🧩 Metodologia

O projeto foi implementado em **Python 3** utilizando o pacote **NetworkX**, amplamente empregado para análise e visualização de redes complexas.

### 🔧 Etapas do projeto:
1. **Coleta de dados:** lista de estações e conexões do metrô de São Paulo.  
2. **Modelagem do grafo:** criação de um grafo não direcionado `G` representando a rede.  
3. **Cálculo de métricas:** obtenção de indicadores de conectividade.  
4. **Visualização:** plotagem da rede e destaque de estações críticas.  
5. **Análise qualitativa:** interpretação dos resultados e discussão sobre a eficiência e vulnerabilidade da rede.

---


## 🐍 Tecnologias Utilizadas

- **Python 3.10+**  
- **NetworkX** — análise e modelagem de grafos  
- **Matplotlib** — visualização gráfica da rede  
- **Pandas** — manipulação de dados tabulares  

---
