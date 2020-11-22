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



 **Resultado**

Ao final temos a tabela com menor custo de 0 para todos os vértices como a indicada abaixo:

| Vértices |  0   |  1   |  2   |  3   |  4   |
| :------- | :--: | :--: | :--: | :--: | :--: |
| **C.M.** |  0   |  3   |  2   |  5   |  6   |

Podemos também montar um novo grafo seguindo os menores trajetos, veja:

![Imagem do Grafo](https://github.com/LucasSargeir/Algoritmos-em-Grafos/blob/master/images/exemplo13.png)



## Bellman-Ford

O algoritmo de Bellman-Ford, assim como o de Dijkstra, serve para encontrarmos o menor caminho entre um vértice e todos os outros. Diferente do algoritmo anterior, esse pode ser utilizado quando temos pesos negativos em nossas arestas. Apesar disso ele é um pouco mais custoso do que o visto anteriomente.

A ideia do algoritmo parte do princípio que se temos um grafo com n vértices o maior caminho para chegar a um outro vértice passará por no máximo (n - 1) vértices. Se essa regra não for satisfeita, significa que temos um ciclo negativo no nosso grafo, e nesse caso, não é possível encontrar o menor caminho uma vez que a cada ciclo negativo nosso custo diminue.

Uma vez que nosso grafo satisfaça essa condição, o algoritmo irá analizar, no máximo (n - 1) vezes, o custo para chegar em cada vértice considerando o custo encontrado para o vértice atual na iteração anteriores. Embora as iterações aconteçam no máximo (n - 1) vezes isso não quer dizer que sempre será dessa forma. Se em alguma iteração nós não atualizarmos nenhum dos valores da tabela nosso algoritmo pode ser interrompido.

**Exemplo:** Considere o grafo abaixo com as arestas indicadas. Começaremos a visitação pelo vértice (0).

![Imagem do Grafo](https://github.com/LucasSargeir/Algoritmos-em-Grafos/blob/master/images/exemplo14.png)

Como temos 6 vértices nosso número de iterações será (n - 1) = 5.

Caminharemos por cada vértice, sequencialmente, 5 vezes, verificando se o custo para chegar em cada um dos seus vizinhos somado ao seu próprio custo é menor do que o já armazenado na tabela.

------

#### Iteração 1

<u>Analisando o vértice (0)</u> 

Verificamos que seus vizinhos são o vértice (1) com custo 10 e o vértice (5) com custo 8. Como os custos são menores que os guardados na tabela, substituimos.

![Imagem do Grafo](https://github.com/LucasSargeir/Algoritmos-em-Grafos/blob/master/images/exemplo14.png)

| Vértices | [0]  |       1       |  2   |  3   |  4   |      5      |
| -------- | :--: | :-----------: | :--: | :--: | :--: | :---------: |
| **C.M.** |  0   | (0 + 10) = 10 |  ∞   |  ∞   |  ∞   | (0 + 8) = 8 |



<u>Analisando o vértice (1)</u> 

Verificamos que seu único vizinhos é o vértice (3) com custo 2. Como o custo é menor que o guardado na tabela, substituimos.

![Imagem do Grafo](https://github.com/LucasSargeir/Algoritmos-em-Grafos/blob/master/images/exemplo15.png)

| Vértices |  0   | [1]  |  2   |       3       |  4   |  5   |
| -------- | :--: | :--: | :--: | :-----------: | :--: | :--: |
| **C.M.** |  0   |  10  |  ∞   | (10 + 2) = 12 |  ∞   |  8   |



<u>Analinsando o vértice (2)</u>

Repare que não sabemos como chegar no vértice (2) ainda, pois sua distância é ∞. Neste caso não podemos caminhar até ele, então pulamos a iteração.



<u>Analinsando o vértice (3)</u>

Verificamos que seu único vizinhos é o vértice (2) com custo -2. Como o custo é menor que o guardado na tabela, substituimos.

![Imagem do Grafo](https://github.com/LucasSargeir/Algoritmos-em-Grafos/blob/master/images/exemplo16.png)

| Vértices |  0   |  1   |       2       | [3]  |  4   |  5   |
| -------- | :--: | :--: | :-----------: | :--: | :--: | :--: |
| **C.M.** |  0   |  10  | (12 - 2) = 10 |  12  |  ∞   |  8   |



<u>Analinsando o vértice (4)</u>

Repare que não sabemos como chegar no vértice (2) ainda, pois sua distância é ∞. Neste caso não podemos caminhar até ele, então pulamos a iteração.



<u>Analinsando o vértice (5)</u>

Verificamos que seu único vizinhos é o vértice (2) com custo -2. Como o custo é menor que o guardado na tabela, substituimos.

![Imagem do Grafo](https://github.com/LucasSargeir/Algoritmos-em-Grafos/blob/master/images/exemplo17.png)

| Vértices |  0   |  1   |  2   |  3   |      4      | [5]  |
| -------- | :--: | :--: | :--: | :--: | :---------: | :--: |
| **C.M.** |  0   |  10  |  10  |  12  | (8 + 1) = 9 |  8   |



------

#### Iteração 2

<u>Analisando o vértice (0)</u> 

Verificamos os vizinhos do vértice (0). Como não houve melhora nos custos pulamos essa iteração.



<u>Analisando o vértice (1)</u> 

Verificamos os vizinhos do vértice (0). Como não houve melhora nos custos pulamos essa iteração.



<u>Analinsando o vértice (2)</u>

Verificamos os vizinhos do vértice (2). Como não houve melhora nos custos pulamos essa iteração.



<u>Analinsando o vértice (3)</u>

Verificamos os vizinhos do vértice (3). Como não houve melhora nos custos pulamos essa iteração.



<u>Analinsando o vértice (4)</u>

Verificamos os vizinhos do vétice (4). Repare que agora, ao somarmos o custo do nosso vértice somado ao custo para chegar em seus vizinhos é menos do que os valores salvos na tabela. Nesse caso atualizamos os valores na tabela.

![Imagem do Grafo](https://github.com/LucasSargeir/Algoritmos-em-Grafos/blob/master/images/exemplo19.png)


| Vértices |  0   |      1      |  2   |      3      | [4]  |  5   |
| -------- | :--: | :---------: | :--: | :---------: | :--: | :--: |
| **C.M.** |  0   | (9 - 4) = 5 |  10  | (9 - 1) = 8 |  9   |  8   |



<u>Analinsando o vértice (5)</u>

Verificamos os vizinhos do vértice (5). Como não houve melhora nos custos pulamos essa iteração.



------

#### Iteração 3

<u>Analisando o vértice (0)</u> 

Verificamos os vizinhos do vértice (0). Como não houve melhora nos custos pulamos essa iteração.



<u>Analisando o vértice (1)</u> 

Verificamos os vizinhos do vértice (1), podemos observar que temos melhora de custo ao caminharmos para o vértice (3). Neste caso atualizamos a tabela.

![Imagem do Grafo](https://github.com/LucasSargeir/Algoritmos-em-Grafos/blob/master/images/exemplo16.png)

| Vértices |  0   | [1]  |  2   |      3      |  4   |  5   |
| -------- | :--: | :--: | :--: | :---------: | :--: | :--: |
| **C.M.** |  0   |  5   |  10  | (5 + 2) = 7 |  9   |  8   |



<u>Analinsando o vértice (2)</u>

Verificamos os vizinhos do vértice (2). Como não houve melhora nos custos pulamos essa iteração.



<u>Analinsando o vértice (3)</u>

Verificamos os vizinhos do vértice (3), podemos observar que temos melhora de custo ao caminharmos para o vértice (2). Neste caso atualizamos a tabela.

![Imagem do Grafo](https://github.com/LucasSargeir/Algoritmos-em-Grafos/blob/master/images/exemplo17.png)

| Vértices |  0   |  1   |      2      | [3]  |  4   |  5   |
| -------- | :--: | :--: | :---------: | :--: | :--: | :--: |
| **C.M.** |  0   |  5   | (7 - 2) = 5 |  7   |  9   |  8   |



<u>Analinsando o vértice (4)</u>

Verificamos os vizinhos do vértice (4). Como não houve melhora nos custos pulamos essa iteração.



<u>Analinsando o vértice (5)</u>

Verificamos os vizinhos do vértice (5). Como não houve melhora nos custos pulamos essa iteração.



------

#### Iteração 4

<u>Analisando o vértice (0)</u> 

Verificamos os vizinhos do vértice (0). Como não houve melhora nos custos pulamos essa iteração.



<u>Analisando o vértice (1)</u> 

Verificamos os vizinhos do vértice (1). Como não houve melhora nos custos pulamos essa iteração.



<u>Analinsando o vértice (2)</u>

Verificamos os vizinhos do vértice (2). Como não houve melhora nos custos pulamos essa iteração.



<u>Analinsando o vértice (3)</u>

Verificamos os vizinhos do vértice (3). Como não houve melhora nos custos pulamos essa iteração.



<u>Analinsando o vértice (4)</u>

Verificamos os vizinhos do vértice (4). Como não houve melhora nos custos pulamos essa iteração.



<u>Analinsando o vértice (5)</u>

Verificamos os vizinhos do vértice (5). Como não houve melhora nos custos pulamos essa iteração.



Como não tivemos nenhuma atualização nessa iteração podemos finalizar o algoritmo.



**Resultado**

Ao final temos a tabela com menor custo de 0 para todos os vértices como a indicada abaixo:

| Vértices |  0   |  1   |  2   |  3   |  4   |  5   |
| -------- | :--: | :--: | :--: | :--: | :--: | :--: |
| **C.M.** |  0   |  5   |  5   |  7   |  9   |  8   |


Podemos também montar um novo grafo seguindo os menores trajetos, veja:

![Imagem do Grafo](https://github.com/LucasSargeir/Algoritmos-em-Grafos/blob/master/images/exemplo20.png)



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
