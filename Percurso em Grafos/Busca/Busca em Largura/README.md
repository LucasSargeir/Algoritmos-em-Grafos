# Busca em Largura

A ideia da busca em largura é, partindo de um vertice, adicionar ele em uma fila. Para cada elemento da fila buscamos o primeiro elemento, mostramos o seu valor, e adicionamos seus vértices adjacentes, que não foram visitados ainda, no final da fila e remover o elemento da fila. Realizar esse o processo até que a fila esteja vazia.



## Exemplo

Considere o grafo abaixo abaixo:

![exemplo5](/home/lucas/Documents/CEFET/Aula/Algoritmos em Grafos/Repositório do Git/images/exemplo5.png)

**Visita em Ordem-por-Nível :**

Vejamos um exemplo de visita em pré ordem partindo do vértice 2:



- Adicionar o 2 na fila:

  `[Fila] => [2]`

- Percorrer fila:

  - Pegar o primeiro da fila, recebe (2);

  - Verificar se o 2 já foi visitado;

  - Como não foi, mostrar na tela:

    `[Tela]   2`

  - Marca o 2 como visitado:

    `[Visitados]  {False, True, False, False, False}`

  - Buscar vizinhos do 2, recebe (1, 3, 5);

    - Verificar se o 1 já foi visitado;

    - Como não foi, adicionar ao final da fila:

      `[Fila] => [2, 1]`

    - Verificar se o 3 já foi visitado;

    - Como não foi, adicionar ao final da fila:

      `[Fila] => [2, 1, 3]`

    - Verificar se o 5 já foi visitado;

    - Como não foi, adicionar ao final da fila:

      `[Fila] => [2, 1, 3, 5]`

  - Remover o 2 da fila:

    `[Fila] => [1, 3, 5]`

  - Pegar o primeiro da fila, recebe (1);

  - Verificar se o 1 já foi visitado;

  - Como não foi, mostrar na tela:

    `[Tela]   2 1`

  - Marca o 1 como visitado:

    `[Visitados]  {True, True, False, False, False}`

  - Buscar vizinhos do 1, recebe (2, 5);

    - Verificar se o 2 já foi visitado;

    - Como ja foi, ignorar o 2;

    - Verificar se o 5 já foi visitado;

    - Como não foi, adicionar ao final da fila:

      `[Fila] => [1, 3, 5, 5]`

  - Remover o 1 da fila:

    `[Fila] => [3, 5, 5]`

  - Pegar o primeiro da fila, recebe (3);

  - Verificar se o 3 já foi visitado;

  - Como não foi, mostrar na tela:

    `[Tela]   2 1 3`

  - Marca o 3 como visitado:

    `[Visitados]  {True, True, True, False, False}`

  - Buscar vizinhos do 3, recebe (2);

    - Verificar se o 2 já foi visitado;
    - Como ja foi, ignorar o 2;

  - Remover o 3 da fila:

    `[Fila] => [5, 5]`

  - Pegar o primeiro da fila, recebe (5);

  - Verificar se o 5 já foi visitado;

  - Como não foi, mostrar na tela:

    `[Tela]   2 1 3 5`

  - Marca o 5 como visitado:

    `[Visitados]  {True, True, True, False, True}`

  - Buscar vizinhos do 5, recebe (1, 2, 4);

    - Verificar se o 1 já foi visitado;

    - Como ja foi, ignorar o 1;

    - Verificar se o 2 já foi visitado;

    - Como ja foi, ignorar o 2;

    - Verificar se o 4 já foi visitado;

    - Como não foi, adicionar ao final da fila:

      `[Fila] => [5, 5, 4]`

  - Remover o 5 da fila:

    `[Fila] => [5, 4]`

  - Pegar o primeiro da fila, recebe (5);

  - Verificar se o 5 já foi visitado;

  - Como já foi, ignorar o 5;

  - Remover o 5 da fila:

    `[Fila] => [4]`

  - Pegar o primeiro da fila, recebe (4);

  - Verificar se o 4 já foi visitado;

  - Como não foi, mostrar na tela:

    `[Tela]   2 1 3 5 4`

  - Marca o 5 como visitado:

    `[Visitados]  {True, True, True, True, True}`

  - Buscar vizinhos do 5, recebe (5);

    - Verificar se o 5 já foi visitado;
    - Como ja foi, ignorar o 5;

  - Remover o 4 da fila:

    `[Fila] => []`