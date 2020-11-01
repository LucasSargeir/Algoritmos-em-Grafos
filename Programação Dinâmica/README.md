# Programação Dinâmica 



Programação dinânica é um paradigma de programação que visa quebrar um problema maior em vários subproblemas. 

Nesse processo resolvemos cada um dos subproblemas e sempre guardamos os valores obtidos, assim, se eventualmente precisarmos resolver esse subproblema novamente, basta buscar o valor guardado anteriormente.

#### Características: 

- Posssue duas abordagens de programação: 

  - Tabulations (Bottom-Up); 
  - Memorization (Top-Down). 

- Analisa todo o espaço de soluções (Exaustivo); 

- Geralmente mais lento do que algoritmos gulosos; 

- Usando quando existem subproblemas iguais que precisam ser resolvidos várias vezes.


#### Propriedades: 

- Sobreposição de subproblemas: Um mesmo subproblema não é resolvido mais de uma vez;

- Subestrutura ótima: A solução do problema pode ser construido a partir da solução ótima dos subproblemas. 



## Abordagens

### Tabulation

De um modo geral essa abordagem implica em um algoritmo iterativo e funciona utilizando a ideias de **Bottom Up**, ou seja, vamos calculando os subproblemas menores e aumentando a complexidade com o passar do tempo. Observe que, nesta abordagem, nós sabemos que, na i-ésima iteração, a [i-ésima - 1] já foi resolvida, logo não precisamos verificar toda vez como na top-down.

#### Ideia:

- Inicializar uma estrutura tabular com os valores base; 

- Fazer um laço que itere em cima dos valores de i restantes: 
  
- A cada iteração atualizar table(i) = f(i) utilizando a estrutura tabular para combinar as soluções dos subproblemas resolvidos. 
  
- Retornar table(n) 

  

Para ajudar no entendimento, vejamos o exemplo clássico de _Fibonacci_:

 ```c++
int Fib(int n){ 
	int f[n+1]; 
	f[0] = 0; f[1] = 1; 
    for(int i = 2; i <= n; ++i){
        f[i] = f[i+1] + f[i+2]; 
	}
	return f[n] 
} 

 ```

#### Característica: 

- Funciona usando a ideia Bottom-Up; 
- Reduz o número de consultas na tabela de memorização o que reduz o overhead; 

 

 

### Memorization

De um modo geral essa abordagem implica em um algoritmo recursivo comum, ou seja, começamos pelo n-ésimo número e, recursivamente, vamos calculando os valores anteriores. Mas diferente da abordagem recursiva comum, nesta abordagem, os valores são armazenados em uma tabela e, para a i-ésima iteração, verifica-se se esse problema já foi calculado.

  

#### Ideia: 

- Cria uma estrutura (table) para armazenar a solução dos subproblemas; 

- Inicializa a estrutura como vazia; 

- A cada etapa I: 
  - Checar se a table[i] está vazia; 

  - Se não estiver, retornar table[i]; 

  - Se table[i] estiver vazia e i satisfazer a condição básica, atualizamos table[i] e a retornamos; 

  - Se table[i] estiver vazia e i não satisfazer a condição básica, dividimos i em seus subproblemas e os resolvemos recursivamente; 

  - Após as chamadas recursivas resolverem os subproblemas, combinam-se as soluções e atualiza-se table; 

    

Para ajudar no entendimento, vejamos o exemplo clássico de _Fibonacci_: 

```c++
int tabFib[MaxSize] 
//Inicializa todos os valores de tabFib com -1 
memset(tabFib, -1, sizeof(int)*MaxSize); 

int Fib(int n){ 
	if(tabFib[n] != -1) return tabFib[n]; 
	if(n == 0) return tabFib[0] = 0; 
	if(n == 1) return tabFib[1] = 1; 
	return tabFib[n] = Fib(n-1)+Fib(n-2); 
} 


```

#### Característica: 

- Funciona usando a ideia Top-Down; 
- Pode evitar o cáculo de subproblemas que não são necessários pro caso solicitado; 
- Costuma ser mais intuitivo. 

 