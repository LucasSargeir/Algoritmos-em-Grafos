# Busca em Profundidade

A ideia da busca em profundidade visa, partindo de um vertice, verificar todos os visinhos dele que ainda não foram visitados e mostrar os valores de cada um. 

Seguindo essa ideia podemos fazer de duas formas: 

- Pré Ordem:
  - Mostra o valor do vértice atual;
  - Visita os Vizinhos.
- Pós Ordem
  - Visita os Vizinhos;
  - Mostra o valor do vértice atual.



## Exemplo

Considere o grafo abaixo abaixo:

![exemplo5](/home/lucas/Documents/CEFET/Aula/Algoritmos em Grafos/Repositório do Git/images/exemplo5.png)

**Visita em Pré-Ordem :**

Vejamos um exemplo de visita em pré ordem partindo do vértice 2:



- Visita o vértice 2;

- Verifica se já foi visitado;

- Como não foi, mostra o valor na tela:

  `[Tela]  2`

- Marca o 2 como visitado:

  `[Visitados]  {False, True, False, False, False}`

- Busca os vizinhos do 2, recebe (1, 3, 5):

  - Verifica de o 1 já foi visitado;

  - Como não foi, mostra o valor na tela:

    `[Tela]  2 1`

  - Marca o 1 como visitado:

    `[Visitados] {True, True, False, False, False}`

  - Busca os vizinhos do 1, recebe (2, 5):

    - Verifica se o 2 já foi visitado;

    - Como já foi, o 2 é ignorado;

    - Verifica de o 5 já foi visitado;

    - Como não foi, mostra o valor na tela:

      `[Tela]  2 1 5`

    - Marca o 5 como visitado:

      `[Visitados] {True, True, False, False, True}`

    - Busca os vizinhos do 5, recebe (1, 2, 4):

      - Verifica se o 1 já foi visitado;

      - Como já foi, o 1 é ignorado;

      - Verifica se o 2 já foi visitado;

      - Como já foi, o 2 é ignorado;

      - Verifica se o 4 já foi visitado;

      - Como não foi, mostra o valor na tela:

        `[Tela]  2 1 5 4`

      - Marca o 4 como visitado:

        `[Visitados] {True, True, False, True, True}`

      - Busca os vizinhos do 4, recebe (5):

        - Verifica se o 5 já foi visitado;
        - Como já foi, o 5 é ignorado;

  - Verifica se o 3 já foi visitado;

  - Como não foi, mostra o valor na tela:

    `[Tela]  2 1 5 4 3`

  - Marca o 3 como visitado:

    `[Visitados] {True, True, True, True, True}`

  - Busca os vizinhos do 3, recebe (2):

    - Verifica se o 2 já foi visitado;
    - Como já foi, o 2 é ignorado;



**Visita em Pós-Ordem :**

A visita em pós ordem ocorre da mesma forma que o exemplo acima, a única diferença é que ele so mostra o valor do elemento depois de percorrer os vizinhos, veja:



- Visita o vértice 2;

- Verifica se já foi visitado;

- Como não foi, marca o 2 como visitado:

  `[Visitados]  {False, True, False, False, False}`

- Busca os vizinhos do 2, recebe (1, 3, 5):

  - Verifica de o 1 já foi visitado;

  - Como não foi, marca o 1 como visitado:

    `[Visitados] {True, True, False, False, False}`

  - Busca os vizinhos do 1, recebe (2, 5):

    - Verifica se o 2 já foi visitado;

    - Como já foi, o 2 é ignorado;

    - Verifica de o 5 já foi visitado

    - Como não foi, marca o 5 como visitado:

      `[Visitados] {True, True, False, False, True}`

    - Busca os vizinhos do 5, recebe (1, 2, 4):

      - Verifica se o 1 já foi visitado;

      - Como já foi, o 1 é ignorado;

      - Verifica se o 2 já foi visitado;

      - Como já foi, o 2 é ignorado;

      - Verifica se o 4 já foi visitado;

      - Como não foi, marca o 4 como visitado:

        `[Visitados] {True, True, False, True, True}`

      - Busca os vizinhos do 4, recebe (5):

        - Verifica se o 5 já foi visitado;
        - Como já foi, o 5 é ignorado;

      - Mostra o valor do 4 na tela:

        `[Tela]  4`

    - Mostra o valor do 5 na tela:

      `[Tela]  4 5`

  - Mostra o valor do 1 na tela:

    `[Tela]  4 5 1`

  - Verifica se o 3 já foi visitado;

  - Como não foi, marca o 3 como visitado:

    `[Visitados] {True, True, True, True, True}`

  - Busca os vizinhos de 3, recebe (2):

    - Verifica se o 2 já foi visitado;
    - Como já foi, o 2 é ignorado;

  - Mostra o valor do 3 na tela:

    `[Tela]  4 5 1 3`

- Mostra o valor do 2 na tela:

  `[Tela]  4 5 1 3 2`