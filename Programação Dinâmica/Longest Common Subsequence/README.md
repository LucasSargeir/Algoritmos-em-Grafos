# Longest Common Sequence

Problema proposto na disciplina de Algoritmos em Grafos do curso de Bacharelado em Ciência da Computação no CEFET-RJ (Maracanã).



**Tecnologias:**

- Python (3.9)

**Abordagem:**

- Bottom-Up

  

## Problema

Suponha que temos duas strings. Como podemos descobrir a maior substring possível que é comum nas duas? É importante dizer que as letras não precisas estar na mesma ordem para ser uma substring, veja no exemplo.



## Exemplo

Considere as strings abaixo:

![exemplo3](/home/lucas/Documents/CEFET/Aula/Algoritmos em Grafos/Repositório do Git/images/exemplo3.png)

Considere os exemplos de substring, como podemos encontrar o maior tamanho possível de substring.



## Solução

1. Criar nossa tabela de memorização;
2. Definir nossas condições de parada:
   - Se terminarmos de percorrer qualquer uma das strings devemos retornar 0.

3. Verificar se já temos um valor guardado na tabela de memorização:

   - Se tivermos, retornar o valor.

   - Caso não, verificar se o caracter atual é igual nas duas strings:
     - Caso sim avançamos nas duas strings;
     - Caso não devemos abrir dois caminhos, onde em cada um avançamos em uma string diferente.
   - Retornamos o valor que tiver a maior sequência;



## Extras

Função que encontra qual a maior das substrings.

​	