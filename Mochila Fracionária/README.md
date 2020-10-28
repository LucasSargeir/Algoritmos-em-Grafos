# Mochila Fracionária

Problema proposto na disciplina de Algoritmos em Grafos do curso de Bacharelado em Ciência da Computação no CEFET-RJ (Maracanã).



**Tecnologias:**

- Python (3.9)



## Problema

Suponha que temos uma uma mochila fracionária com uma capacidade limitada. Além disso, temos alguns items, que possuem um peso e um valor associados. Por ser uma mochila fracionária podemos pegar frações de items. Dadas as informações de cada item e a capacidade da mochila, como escolher quais itens pegar e em qual fração de cada um, visando maximizar o valor dos items? 



## Exemplo

Considere os 3 items abaixo com as suas respectivas informações:

![exemplo2](/home/lucas/Documents/CEFET/Aula/Algoritmos em Grafos/Algortimos Gulosos/images/exemplo2.png)



## Solução

Passo a passo:

1. Fazer a razão entre o valor e o peso para cada item:

   |           | Item 1 | Item 2 | Item 3 |
   | --------- | ------ | ------ | ------ |
   | **Valor** | 60     | 100    | 120    |
   | **Peso**  | 10     | 20     | 30     |
   | **Razão** | 6      | 5      | 4      |



2. Oredenar os items pela razão em ordem decrescente:

   **Ficamos:** item1, item2, item3

   

3. Selecionar os itens com a maior razão até que o próximo não possa ser adicionado em sua integralidade:

   **Mochilha (30/50):** 10 + 20 + ???

   **Valor (160):** 60 + 100 + ???

   

4. Por fim, adicionar a maior fração possível do item restante na lista:

   **Mochilha (30/50):** 10 + 20 + 2/3.(30)

   **Valor (240):** 60 + 100 + 2/3.(120)

