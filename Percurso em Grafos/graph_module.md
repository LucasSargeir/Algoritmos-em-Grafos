# Módulo Graph

Módulo criado com o objetivo de facilitar a manipulação de grafos.

#### Tecnologia

- Python (3.9)

  

## Conceitos

- Matriz de adjacência

  Uma matriz de adjancência é uma matriz que guarda a quais vétices cada um dos outros estão ligados e seus respectivos pesos. Veja o exemplo:

  ![](https://github.com/LucasSargeir/Algoritmos-em-Grafos/blob/master/images/exemplo6.png)

  Tem como matriz de adjacência a tabela abaixo:
  
  | Vértices |  v1  |  v2  |  v3  |  v4  |  v5  |
  | :------: | :--: | :--: | :--: | :--: | :--: |
  |  **v1**  |  0   |  4   |  3   |  ∞   |  ∞   |
  |  **v2**  |  ∞   |  0   |  3   |  2   |  3   |
  |  **v3**  |  ∞   |  1   |  0   |  4   |  5   |
  |  **v4**  |  ∞   |  ∞   |  ∞   |  0   |  ∞   |
  |  **v5**  |  ∞   |  ∞   |  ∞   |  1   |  0   |
  
  Repare que um vétice sempre tem peso 0 para ir a si mesmo, e tem peso ∞ quando não está ligado a outro vértice.
  
  
## Módulo



### Classe Graph

#### Construtor

- `Graph(<matrix[N][N]>)`

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

- `	__matrix[N][N]`

  Atributo que guarda a matriz de adjacência de um grafo onde N é o número de vértices. Perceba que o atributo é privado, para acessá-lo você pode utilizar o método `get_matrix()` especificado na sessão de métodos.



#### Infinito

- `infinity`

  Trabalhando com grafos as vezes torna-se necessário utilizar valores muito grandes ou muito pequenos. Para isso você pode utilizar a variável infinity que é importada junto ao módulo.

  > _**Obs:** O valor de `infinity` é retirado do módulo math e representa o maior real possível de se representar_



#### Métodos

- `get_matrix(self)->list`

  Retorna a matriz de adjacência do grafo.
  
  
  
- `get_adj_list(self, index: int)->list`

  Retorna uma lista de adjacência do vétice especificado.

  

- `get_total_v(self)->int`

  Retorna um número inteiro com o total de vétices do grafo.

  

- `__print_matrix(self)`

  Método privado utilizado para sobrescrever o método `__str__(self)`, isso faz com que se criarmos uma intância do nosso objeto e passarmos como parâmetro para o método `print()`  ele seja impressom como o exemplo abaixo:

  ```python
  >>> print(graph)
  #TELA
  #Ver.     (1)     (2)     (3)     (4)     (5)	
  #(1)       0       4       2      inf     inf	
  #(2)      inf      0       3       2       3	
  #(3)      inf      1       0       4       5	
  #(4)      inf     inf     inf      0      inf	
  #(5)      inf     inf     inf      1       0	
  ```




### Métodos do Módulo

- `print_m(matrix)`

  Método que imprime uma matriz no formato padrão, veja o exemplo:

  ```python
  # 1    2    3    4
  # 5    6    7    8
  # 9    1    2    3
  # 4    5    6    7
  ```

  



## Possíveis Erros

- Code 01:

```python
#Exception: Missing vertices in adjacency matrix on line <linha> | code 01  
```

Esse erro é lançado quando temos mais linhas do que colunas na nossa matriz de adjacência. Onde `<linha>` será qual das linha da matriz da adjacência que têm argumentos faltando.

- Code 02:

```python
#Exception: To much vertices in adjacency matrix on line <linha> | code 02
```

Esse erro é lançado quando temos mais colunas do que linhas na nossa matriz de adjacência. Onde `<linha>` será qual das linha da matriz da adjacência que têm argumentos a mais.
