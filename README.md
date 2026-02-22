
# Comparação entre os Algoritmos de Kruskal e Prim para Construção de Árvores Geradoras Mínimas em Grafos Euclidianos

## 📌 Descrição

Este repositório contém a implementação experimental utilizada no estudo comparativo entre os algoritmos de **Kruskal** e **Prim** para a construção de Árvores Geradoras Mínimas (Minimum Spanning Trees – MST) em grafos euclidianos completos.

Os experimentos analisam:

* Tempo de execução dos algoritmos
* Custo total da árvore geradora mínima
* Visualização gráfica das árvores resultantes

O estudo foi conduzido variando o número de nós entre 20 e 100, considerando grafos completos com pesos definidos por distâncias euclidianas no plano bidimensional.

---

## 🎯 Objetivos

* Comparar experimentalmente o desempenho temporal dos algoritmos de Kruskal e Prim
* Verificar a igualdade do custo total das MSTs produzidas
* Visualizar graficamente as árvores geradoras mínimas
* Fornecer uma base reprodutível para experimentos didáticos e acadêmicos

---

## 🧠 Fundamentação Teórica

O problema da Árvore Geradora Mínima consiste em encontrar um subconjunto de arestas que:

* Conecte todos os vértices do grafo
* Não forme ciclos
* Minimize o custo total

Foram utilizados dois algoritmos clássicos:

* **Kruskal** (1956): estratégia gulosa baseada na ordenação global das arestas
* **Prim** (1957): crescimento incremental da árvore a partir de um vértice inicial

Ambos possuem complexidade assintótica dependente da estrutura do grafo e da implementação das estruturas auxiliares.

---

## 🛠 Tecnologias Utilizadas

* Python 3
* NetworkX
* NumPy
* SciPy
* Matplotlib

---

## 📂 Estrutura do Projeto

```
mst/
│
├── main.py          # Script principal contendo geração dos grafos e experimentos
├── README.md        # Documentação do projeto
```

---

## ⚙️ Metodologia Experimental

Para cada valor de N ∈ {20, 40, 60, 80, 100}:

1. Geração de N pontos aleatórios no quadrado unitário [0,1] × [0,1]
2. Construção de grafo completo com pesos definidos pela distância euclidiana
3. Aplicação dos algoritmos:

   * `minimum_spanning_tree(G, algorithm='kruskal')`
   * `minimum_spanning_tree(G, algorithm='prim')`
4. Medição do tempo de execução
5. Cálculo do custo total da MST
6. Visualização gráfica das árvores para N = 100

A semente aleatória foi fixada para garantir reprodutibilidade.

---

## 📊 Resultados Esperados

* O custo total das MSTs obtidas por Kruskal e Prim é idêntico.
* Pequenas diferenças podem ocorrer no tempo de execução.
* Para grafos completos euclidianos de pequeno e médio porte, ambos os algoritmos apresentam desempenho semelhante.

---

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/vitor-souza-ime/mst.git
cd mst
```

2. Instale as dependências:

```bash
pip install networkx numpy scipy matplotlib
```

3. Execute o script:

```bash
python main.py
```

Os gráficos de tempo, custo e visualização das árvores serão exibidos automaticamente.

---

## 📈 Possíveis Extensões

* Executar múltiplas repetições por valor de N (benchmark estatístico)
* Avaliar grafos esparsos
* Testar valores maiores de N
* Comparar com o algoritmo de Borůvka
* Analisar crescimento assintótico do custo médio da MST

---

## 📚 Referências Principais

* Cormen, T. H. et al. *Introduction to Algorithms*. MIT Press.
* Kruskal, J. B. (1956). On the shortest spanning subtree of a graph.
* Prim, R. C. (1957). Shortest connection networks and some generalizations.
* Sedgewick, R.; Wayne, K. *Algorithms*.
* Skiena, S. S. *The Algorithm Design Manual*.

---

## 👨‍🏫 Autor

Vitor Amadeu Souza


