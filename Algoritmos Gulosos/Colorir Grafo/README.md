# Colorir Grafo

Problema proposto na disciplina de Algoritmos em Grafos do curso de Bacharelado em Ciência da Computação no CEFET-RJ (Maracanã).



**Tecnologias:**

- Python (3.9)



## Problema

Suponha que temos um grafo qualquer. Como podemos colorir seus vértices de forma que cada vértice tenha uma cor diferente de cada vértice vizinho? 



## Exemplo

Considere o grafo abaixo:

![exemplo2](https://github.com/LucasSargeir/Algoritmos-Gulosos/blob/master/images/exemplo8.png)



## Solução

Passo a passo:

1. Visitar o primeiro vétice e definir uma cor inicial para ele;




2. Para cada um dos vértices seguintes:

   1. Verificar qual dos vizinhos dele já possuem uma cor;

   2. Verificar existe alguma cor já utilizada que não está nos vizinhos do vértice atual;

      1. Se existir, escolher essa cor;

      2. Se não existir, criar uma cor nova.

         

3. Retornar lista das cores escolhidas para cada vértice.

   

![exemplo2](https://github.com/LucasSargeir/Algoritmos-Gulosos/blob/master/images/exemplo7.png)