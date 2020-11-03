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