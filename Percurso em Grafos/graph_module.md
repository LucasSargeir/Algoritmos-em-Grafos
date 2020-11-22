# Módulo Graph

Módulo criado com o objetivo de facilitar a manipulação de grafos.

#### Tecnologia

- Python (3.9)

## Conceitos

- Matriz de adjacência

  Uma matriz de adjancência é uma matriz que guarda a quais vétices cada um dos outros estão ligados e seus respectivos pesos. Veja o exemplo:

  ![](https://github.com/LucasSargeir/Algoritmos-em-Grafos/blob/master/images/exemplo6.png)

  Tem como matriz de adjacência a tabela abaixo:

  | Vértices | v1  | v2  | v3  | v4  | v5  |
  | :------: | :-: | :-: | :-: | :-: | :-: |
  |  **v1**  |  0  |  4  |  3  |  ∞  |  ∞  |
  |  **v2**  |  ∞  |  0  |  3  |  2  |  3  |
  |  **v3**  |  ∞  |  1  |  0  |  4  |  5  |
  |  **v4**  |  ∞  |  ∞  |  ∞  |  0  |  ∞  |
  |  **v5**  |  ∞  |  ∞  |  ∞  |  1  |  0  |

  Repare que um vétice sempre tem peso 0 para ir a si mesmo, e tem peso ∞ quando não está ligado a outro vértice.
  





## Módulo

### Classe Graph

#### Construtor

- **`Graph(<matrix[N][N]>)`**

  Esse construtor recebe uma matriz de adjacência para criar o grafo.

  ##### Exemplo

```python
graph = Graph([ [ 0 , 4 , 2 ,inf,inf],
		[inf, 0 , 3 , 2 , 3 ],
		[inf, 1 , 0 , 4 , 5 ],
		[inf,inf,inf, 0 ,inf],
		[inf,inf,inf, 1 , 0 ] ])
```
> _**Obs:** Os grafos estão indexados pelas posições do Array, onde o índice = V -1_



#### Atributos

- **` __matrix[N][N]`**

  Atributo que guarda a matriz de adjacência de um grafo onde N é o número de vértices. Perceba que o atributo é privado, para acessá-lo você pode utilizar o método `get_matrix()` especificado na sessão de métodos.



#### Infinito

- **`infinity`**

  Trabalhando com grafos as vezes torna-se necessário utilizar valores muito grandes ou muito pequenos. Para isso você pode utilizar a variável infinity que é importada junto ao módulo.

  > _**Obs:** O valor de `infinity` é retirado do módulo math e representa o maior real possível de se representar_



#### Métodos

- **`get_matrix(self, type: str ='ref')->list`**

  Retorna a matriz de adjacência do grafo.

  O parâmetro opcional `type` especifica se a matriz de adjacência será passada como valor ou referência. 

  Opções disponíveis:

  - ref **(default)**: passa uma referência da matriz de adjacência.
  - copy: passa uma cópia da matriz de adjacência.

  

- **`get_adj_list(self, index: int)->list`**

  Retorna a lista de adjacência do vétice especificado pelo parâmetro `index`.

  

- **`get_total_v(self)->int`**

  Retorna um número inteiro com o total de vétices do grafo.

  

- **`__print_matrix(self)`**

  Método privado utilizado para sobrescrever o método `__str__(self)`, isso faz com que se criarmos uma intância do nosso objeto e passarmos como parâmetro para o método `print()` ele seja impressom como o exemplo abaixo:

  ```python
  >>> print(graph)
  #TELA
  #Ver.     (0)     (1)     (2)     (3)     (4)
  #(0)       0       4       2      inf     inf
  #(1)      inf      0       3       2       3
  #(2)      inf      1       0       4       5
  #(3)      inf     inf     inf      0      inf
  #(4)      inf     inf     inf      1       0
  ```

  

- **`has_negative_cycle(self)->bool`**

  Retorna um boleano que indica se o grafo possui um ciclo negativo.




### Funções do Módulo

- **`print_m(matrix)`**

  Função que imprime uma matriz no formato padrão, veja o exemplo:

  ```python
  # 1    2    3    4
  # 5    6    7    8
  # 9    1    2    3
  # 4    5    6    7
  ```



- **`add_vertice(graph: Graph, create_weight: list, set_weight: list=None)->Graph`**

  Função que recebe um grafo e insere um vértice no final da matriz de adjacência. A função retorna um novo grafo com os dados modificados, não altera o grafo original.

  Parâmetros:

  - `graph:` grafo onde o vétice deverá inserido;

    

  - `create_weight`: lista de pesos a serem criados para o novo vértice.

    O tamanho da lista deverá ser **(número de vértices antes da inserção) + 1** representando os pesos de cada vértice já existente mais o peso para si mesmo.

    

  - `set_weight`: lista de pesos referentes ao novo vértice a serem inseridos nos vértices já existentes.

    O tamanho da lista deverá ser **(número de vértices antes da inserção)** representando os pesos a serem inserido em cada vértice já existente .

  ![exemplo5](https://github.com/LucasSargeir/Algoritmos-em-Grafos/blob/master/images/exemplo9.png)



- **`remove_vertice(graph: Graph, vertice: int)->Graph`**

  Função que recebe um grafo e remove um vértice especificado pelo parâmetro `vertice`. A função retorna um novo grafo com os dados modificados, não altera o grafo original.



## Possíveis Erros

- Code 01:

```python
#Exception: Missing vertices in adjacency matrix on line <linha> | code 01
```

Esse erro é lançado quando temos mais linhas do que colunas na nossa matriz de adjacência. Onde `<linha>` será qual das linha da matriz da adjacência que têm argumentos faltando.



- Code 02:

```python
#Exception: Too much vertices in adjacency matrix on line <linha> | code 02
```

Esse erro é lançado quando temos mais colunas do que linhas na nossa matriz de adjacência. Onde `<linha>` será qual das linha da matriz da adjacência que têm argumentos a mais.



- Code 03:

```python
#Exception: Too much weights to create new vertice | code 03
```

Esse erro é lançado quando tentamos adicionar um novo vétice ao nosso grafo e passamos mais elementos do que a quantidade de vértices.

> **Obs:** A quantidade de vértices passada para esse parâmetro deve ser igual a quantidade de vétices que tinhamos antes de adicionar um elemento +1.



- Code 04:

```python
#Exception: Missing weights to create new vertice | code 04
```

Esse erro é lançado quando tentamos adicionar um novo vétice ao nosso grafo e passamos menos elementos do que a quantidade de vértices.

> **Obs:** A quantidade de vértices passada para esse parâmetro deve ser igual a quantidade de vétices que tinhamos antes de adicionar um elemento +1.



- Code 05:

```python
#Exception: More weights than vertices | code 05
```

Esse erro é lançado quando tentamos adicionar um novo vétice ao nosso grafo e decidimos passar o valor opicional `set_weight`. O erro significa que passamos mais elementos do que a quantidade de vértices existentes antes da inserção.

> **Obs:** A quantidade de vértices passada para esse parâmetro deve ser igual a quantidade de vétices que tinhamos antes de adicionar um elemento.



- Code 06:

```python
#Exception: Less weights then vertice | code 06
```

Esse erro é lançado quando tentamos adicionar um novo vétice ao nosso grafo e decidimos passar o valor opicional `set_weight`. O erro significa que passamos menos elementos do que a quantidade de vértices existentes antes da inserção.

> **Obs:** A quantidade de vértices passada para esse parâmetro deve ser igual a quantidade de vétices que tinhamos antes de adicionar um elemento.



- Code 07:

```python
#Exception: Invalid vertice index [<índice>] | code 07
```

Esse erro é lançado quando tentamos remover um vétice do nosso grafo e passamos um índice não existente. O elemento `<indice> ` representa o índice que foi passado, por exemplo -1.