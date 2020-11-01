# Coin Change

Problema proposto na disciplina de Algoritmos em Grafos do curso de Bacharelado em Ciência da Computação no CEFET-RJ (Maracanã).



**Tecnologias:**

- Python (3.9)

**Abordagem:**

- Bottom-Up

  

## Problema

Suponha que temos uma lista de notas e uma valor a ser sacado. Como podemos sacar o valor minimizando o número de notas??



## Exemplo

Considere que  precisamos sacar __R$11,00__, e para isso temos disponível as notas:

__R$8,00__

__R$6,00__

__R$5,00__

__R$1,00__

Como podemos minimizar o número de notas.



## Solução

1. Criar nossa tabela de memorização;

2. Definir nossas condições de parada;

   - Se um valor de saque negativo for passado temos que devolver um número muito alto, pois como estamos buscando minimizar o número de notas, se devolvermos um número pequeno ele será considerado.

   - Se o nosso valor de saque for 0 devemos retornar zero, pois não precisamos de notas para não sacar.

3. Verificar se ja temos um valor na tabela de memorização:

   - Se tivermos retornar o valor.

   - Caso não, criar um vetor de opções do tamanho do vetor de notas disponíveis, utilizaremos ele para verificar as opções para cada nota disponível.

   - Para cada nota disponível vamos analisar o mínimo de notas possível para formar o valor desejado utilizando aquela nota;

   - Recursivamente chamamos a nossa função passando o valor de saque subtraido da nota atual.

4. Verificar, das opções analisadas, qual o menor dos valores.

5. Guardar o menor valor na memóra;

6. Retornar o menor valor