# Sequenciamento de Tarefas

Problema proposto na disciplina de Algoritmos em Grafos do curso de Bacharelado em Ciência da Computação no CEFET-RJ (Maracanã).



**Tecnologias:**

- Python (3.9)



## Problema

Suponha que temos uma lista de tarefas, onde cada tarefa tem seu prazo limite e um prêmio associado. Cada tarefa leva 1 u.t. para ser realizada e apenas uma tarefa pode ser feita de cada vez. Dadas as tarefas, os prêmios relacionados e seus respectivos limites, como podemos priorizar as tarefas de forma a maximizar o prêmio??



## Exemplo

Considere a lista de Tarefas abaixo:

| Tarefa           | A    | B    | C    | D    | E    |
| ---------------- | ---- | ---- | ---- | ---- | ---- |
| **Tempo Limite** | 2    | 1    | 2    | 1    | 3    |
| **Prêmio**       | 100  | 19   | 27   | 25   | 15   |



## Solução

Passo a passo:

1. Ordenar as Tarefas em ordem decrescente de prêmio:


| Tarefa           | A    | C    | D    | B    | E    |
| ---------------- | ---- | ---- | ---- | ---- | ---- |
| **Tempo Limite** | 2    | 2    | 1    | 1    | 3    |
| **Prêmio**       | 100  | 27   | 25   | 219  | 15   |



2. Selecionar a primeira Tarefa e adicionar ela o mais tarde possível:

   **Linha do Tempo:** 

| 1    | 2    | 3    | 4    | 5    |
| ---- | ---- | ---- | ---- | ---- |
|      | A    |      |      |      |



3. Por fim, analise cada uma das próximas Tarefas. Se a Tarefa atual pode ser adicionada dentro do seu tempo limite, adicione, se não, ignore a Tarefa:

   **Linha do Tempo:**

| 1    | 2    | 3    | 4    | 5    |
| ---- | ---- | ---- | ---- | ---- |
| C    | A    | E    | -    | -    |