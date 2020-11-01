# Algoritmos Gulosos 

Um algoritmo guloso é um algoritmo que visa sempre buscar o melhor caminho a cada tomada de decisão, sem se importar com o que virá na próxima iteração, e por isso os chamamos de gulosos. Uma desvantagem desse paradigma de programação é que, apesar de sempre nos apontar um ótimo local, nem sempre esse ótimo local vai nos levar a um ótimo global. Veja o exemplo;

![exemplo1](https://github.com/LucasSargeir/Algoritmos-Gulosos/blob/master/images/exemplo1.png)

Certamente, seguindo o paradigma guloso, o algoritmo seguiria pelo caminho em vermelho, quando na verdade o que nos levaria ao ótimo global é o marcado em verde.

## Garantia do Ótimo Global

Apesar de nem sempre levar vantagem, se garantirmos algumas propriedades, nosso algoritmo poderá sempre nos levar a um ótimo global, e isso pode ser de grande ajuda, considerando que algoritmos gulosos não são difíceis de implementar. Vejamos então que propriedades são essas:

- **Propriedade de escolha gulosa:** 

  Uma solução ótima pode ser alcançada através de escolhas ótimas locais; 

- **Subestrutura ótima:**

  A solução ótima do problema pode ser construída a partir da solução ótima dos subproblemas. 

  

## Exemplos

Alguns exemplos famosos da aplicações de algoritmos gulosos são: 

- [Mochila fracionária](https://github.com/LucasSargeir/Algoritmos-em-Grafos/tree/master/Algoritmos%20Gulosos/Mochila%20Fracion%C3%A1ria); 
- [Problema de Seleão de atividades](https://github.com/LucasSargeir/Algoritmos-em-Grafos/tree/master/Algoritmos%20Gulosos/Sele%C3%A7%C3%A3o%20de%20Atividades); 
- [Problema de sequenciamento de tarefas](https://github.com/LucasSargeir/Algoritmos-em-Grafos/tree/master/Algoritmos%20Gulosos/Sequenciamento%20de%20Tarefas). 
