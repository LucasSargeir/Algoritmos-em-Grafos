# Seleção de Atividades

Problema proposto na disciplina de Algoritmos em Grafos do curso de Bacharelado em Ciência da Computação no CEFET-RJ (Maracanã).



**Tecnologias:**

- Python (3.9)



## Problema

Suponha que temos uma lista de atividades, onde so se pode fazer uma atividade de cada vez. Para cada atividade temos um momento de início e um momento de término. Dadas as atividades e seus respectivos momentos, como podemos separá-las para realizar o máximo possível delas?



## Exemplo

Considere a lista de Atividades abaixo:

| Atividades | A1   | A2   | A3   | A4   | A5   | A6   |
| ---------- | ---- | ---- | ---- | ---- | ---- | ---- |
| **Início** | 9    | 3    | 1    | 5    | 5    | 8    |
| **Fim**    | 6    | 4    | 2    | 9    | 7    | 9    |



## Solução

Passo a passo:

1. Ordenar as Atividades por tempo de témino:

   | Atividades | A3   | A2   | A1   | A5   | A6   | A4   |
   | ---------- | ---- | ---- | ---- | ---- | ---- | ---- |
   | **Início** | 1    | 3    | 0    | 5    | 8    | 5    |
   | **Fim**    | 2    | 4    | 6    | 7    | 9    | 9    |



2. Selecionar a primeira Atividade:

   **Ficamos:** A3

   

3. Por fim, analise cada uma das próximas Atividades. Se o tempo de início for maior ou igual ao tempo da Atividade anterior, selecione, se não, ignore a Atividade:

   **Ficamos:** A3, A2, A5, A6