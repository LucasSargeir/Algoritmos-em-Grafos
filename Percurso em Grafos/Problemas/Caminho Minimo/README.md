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

A ideia do algoritmo consiste em, para cada vétice visitado, buscar todos os vétices vizinhos, que ainda não foram visitados, e verificar quais os custos para se chegar em cada um deles, sempre guardando o menor valor encontrado uma lista de distâncias. 

Feito isso verificamos qual desses vértices vizinhos possui o menor custo e caminhamos para ele. É importante ter em mente que o custo para o próximo vétice é sempre a soma do custo para chegar no vertice anterior somado ao custo do caminho entre eles, pois como a análise está sendo feita em relação ao primeiro vétice, quando caminhamos devemos considerar todo o percurso.

Quando todos os vétices tiverem sido visitados teremos em nossa lista de distâncias o menor caminho para cada um dos vértices.



**Exemplo:** Considere o grafo abaixo com as arestas indicadas. Começaremos a visitação pelo vértice (0).

![Imagem do Grafo](https://github.com/LucasSargeir/Algoritmos-em-Grafos/blob/master/images/exemplo10.png)

Atualizamos o custo na tabela de caminhos mínimos, como estamos no vértice inicial o custo é 0. Agora devemos verificar o custo para cada um de seus vétices adjacentes que não tenham sido visitados ainda, e caso esse custo seja menor do que o já existente na tabela, atualizamos.

Para os vizinhos não visitados de (0) temos o vétice (1) com custo 4 e o vértice (2) com custo 2. Como ambos os custos são menores que infinito, atualizamos a tabela.
| Vértices | [0]  |  1   |  2   |  3   |  4   |
| :------- | :--: | :--: | :--: | :--: | :--: |
| **C.M.** |  0   |  4   |  2   |  ∞   |  ∞   |

Além de atualizar os custos, devemos observar qual dos vértices tem o menor custo. Ele será o proximo a ser visitado. Neste caso, visitaremos o vétice (2).

![Imagem do Grafo](https://github.com/LucasSargeir/Algoritmos-em-Grafos/blob/master/images/exemplo11.png)

Seguindo o mesmo passo realizado anteriormente, verificamos os vizinhos não visitados de 2, atualizando a tabela.

Para os vizinhos não visitados de (2) temos o vértice (1) com custo 1, o vértice (4) com custo 5 e o vértice (3) com custo 4. Como todos os custos são menores do que os custos já encontrados atualizamos a tabela. 

| Vértices |  0   |      1      | [2]  |     3      |      4      |
| :------- | :--: | :---------: | :--: | :--------: | :---------: |
| **C.M.** |  0   | (2 + 1) = 3 |  2   | (2 + 4) =6 | (2 + 5) = 7 |

> **Obs:** Note que nessa iteração estamos caminhando do vértice (2), mas as distâncias são procuradas em relação ao vértice (0), neste caso devemos somar o custo para cada vértice com o custo para chegar até o vértice (2).

Nesta iteração o vétice de menor custo é o (1), logo, caminharemos para ele. A verificação de menor custo deve ser feita em relação a aresta entre os vétices atual e seus vizinhos, não devem ser considerados os valores da tabela. 

Agora, visitaremos o vétice (1).

![Imagem do Grafo](https://github.com/LucasSargeir/Algoritmos-em-Grafos/blob/master/images/exemplo12.png)

Seguindo a iteração, devemos pegar os vizinhos não visitados do vértice (1). Para este vértice temos os vizinhos (3) com custo 2 e (4) com custo 3. Como todos os custos são menores do que os custos já encontrados atualizamos a tabela. 

| Vértices |  0   |  1   |  2   |    3    |    4    |
| :------- | :--: | :--: | :--: | :-----: | :-----: |
| **C.M.** |  0   |  3   |  2   | (3 + 2) | (3 + 3) |

Como o (3) é o vértice de menor custo, caminharemos para ele. Porém como esse vértice não possui vizinhos não visitados pulamos essa iteração e pegamos o próximo vértice não visitado, que neste caso é o (4).

Como o quatro não possui vértices não visitados, e não existem mais vértices não visitados, terminamos o algoritmo.

Ao final temos a tabela com menor custo de 0 para todos os vértices como a indicada abaixo:

| Vértices |  0   |  1   |  2   |  3   |  4   |
| :------- | :--: | :--: | :--: | :--: | :--: |
| **C.M.** |  0   |  3   |  2   |  5   |  6   |

Podemos também montar um novo vértice seguindo os menores trajetos, veja:

![Imagem do Grafo](https://github.com/LucasSargeir/Algoritmos-em-Grafos/blob/master/images/exemplo13.png)



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
