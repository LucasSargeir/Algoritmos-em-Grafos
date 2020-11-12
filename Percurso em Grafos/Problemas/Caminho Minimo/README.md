# Caminho Mínimo

Problema proposto na disciplina de Algoritmos em Grafos do curso de Bacharelado em Ciência da Computação no CEFET-RJ (Maracanã).



**Tecnologias:**

- Python (3.9)



## Algoritmos

Para solucionar o problema de caminho mínimo em um grafo podemos utilizar alguns algoritmos já conhecidos. Alguns deles são:

- Dijkstra;

- Bellman-Ford;

- Floyd-Wharshall;

- Johnson.




## Dijkstra

O algortimo de Dijkstra pode ser usado para encontrar o menor caminho caminho entre um vértice e todos os outros de um determinado grafo. Embora seja um algoritmo simples de implementar e que funcione de forma eficiente, o algoritmo de Dijkstra possui a limitação de que todas as arestas devem ter pesos positivos.

A ideia do algoritmo consiste em, para cada vétice visitado, buscar todos os vétices vizinhos, que ainda não foram visitados, e verificar quais os custos para se chegar em cada um deles, anotando tudo em uma lista de distâncias. 

Feito isso verificamos qual desses vértices vizinhos possui o menor custo e caminhamos para ele. É importante ter em mente que o custo para o próximo vétice é sempre a soma do custo para chegar no vertice anterior somado ao custo do caminho entre eles, pois como a análise está sendo feita em relação ao primeiro vétice, quando caminhamos devemos considerar todo o percurso.

Quando todos os vétices tiverem sido visitados teremos em nossa lista de distâncias o menor caminho para cada um dos vértices.

## Bellman-Ford





## Floyd-Wharshall





## Johnson





## Usabilidade

Considerando os 4 algoritmos citados, quando devemos utilizar cada um deles?

#### Quanto a origem 

- Múltiplas Origens

  Quanto ao grafo de entrada ser esparço:

  - É esparço:

    **Johnson;**

  - Não é esparço:

    **Floyd-Wharshall;**

- Origem Única

  ​	Quando a ter pesos negativos:

  - Possui peso negativo:

	  **Bellman-Ford;**

  - Não possui peso negativo:
  
    **Dijkstra;**
