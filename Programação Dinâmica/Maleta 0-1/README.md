# Maleta 0-1

Problema proposto na disciplina de Algoritmos em Grafos do curso de Bacharelado em Ciência da Computação no CEFET-RJ (Maracanã).



**Tecnologias:**

- Python (3.9)

**Abordagem:**

- Bottom-Up

  

## Problema

Suponha que temos uma maleta que possui uma capacidade e diversos items que possuem seus respectivos pesos e valores. Como podemos maximar os valores de forma a não ultrapassar a capacidade da maleta?



## Exemplo

Considere os 5 items abaixo com as suas respectivas informações:

![exemplo4](https://github.com/LucasSargeir/Algoritmos-em-Grafos/blob/master/images/exemplo4.png)



## Solução

1. Criar nossa tabela de memorização;
2. Definir nossas condições de parada:
   - Se a capacidade que passarmos for menor que 0, devemos retornar um valor muito pequeno, pois como estamos maximizando os valores eles não serão considerados.
   - Se nossa capacidade for iguala zero, devemos retornar 0, pois se não tivermos capacidade não podemos inserir items.
3. Verificar se a sequência de capacidade e item já estão na memorização;
   - Se sim, retornar o valor memorizado;
   - Se não, devemos verificar dois caminhos diferentes, um em que escolhemos aquele item, e outro em que não escolhemos:
     - Guardar na memorização o valor encontrado;
     - Retornar a maior resposta entre os 2 caminhos.
