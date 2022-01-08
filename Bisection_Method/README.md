# Método da Bissecção


### **Objetivo**

Calcular a **raiz de uma função** (Determinar um valor para **Ⲭ** tal que **f(Ⲭ) = 0**).


### **Visão Geral**

Encontraremos um intervalo **[α, β]** que contenha uma e somente uma raiz. Em seguida, definiremos uma raiz inicial **Ⲭ0** pertencente ao intervalo, e a refinaremos através de iterações até obtermos uma raiz que satisfaça o **Critério de Parada** desejado.

* **Critério de Parada**: após cada iteração, verificamos se o resultado obtido tem a **precisão numérica** desejada. Para isso, utilizamos a fórmula: **| Ⲭk - Ⲭk-1 |  ⩽  Ɛ** . 

    * **Ⲭk-1** corresponde ao resultado da iteração anterior, **Ⲭk** ao resultado da iteração atual, e **Ɛ** representa a precisão (Ex. **Ɛ = 10^-3**).


### **Especificações**

* Teorema: Se uma função contínua **f(Ⲭ)** assume valores de sinais opostos nos pontos extremos do intervalo **[α, b]**, isto é, **f(α) . f(β) < 0** , então, o intervalo conterá, no mínimo, uma raiz da equação. Em outras palavras, haverá, no mínimo, um número **ξ ∈ (α, β)**, tal que **f(ξ) = 0** ;

* Propriedade: A raiz **ξ** será definida e única se **f'(Ⲭ)** existir e preservar o sinal dentro do intervalo **(α, β)**, isto é, se **f'(Ⲭ) > 0** ou **f'(Ⲭ) < 0** , se **Ⲭ ∈ (α, β)** .


### **Aplicação do Método**

Para encontrarmos um valor para **Ⲭk** que satisfaça o **Critério de Parada** e seja **raiz da função**, executamos os seguintes passos:

1. Para K = 0 (α0 = α , β0 = β) :

    * f(α0) = A ;

    * f(β0) = B ;

    * Ⲭ0 = (α0 + β0) ÷ 2 ;

    * f(Ⲭ0) = X ;

2. Para K = η :

    * Nota: Podemos aproximar o número **η** de iterações que serão necessárias para convergência do método, através da fórmula:
    **K ⩾ log2((β - α) ÷ Ɛ) - 1** . Observe que o **logaritmo é de base 2**.

    * Se X . A < 0 , então αk = αk-1, βk = Ⲭk-1 ;

    * Se X . B < 0 , então αk = Ⲭk-1, βk =  βk-1 ;

    * f(αk) = A ;

    * f(βk) = B ;

    * Ⲭk = (αk + βk) ÷ 2 ;

    * f(Ⲭk) = X ;

    * Critério de Parada: | Ⲭk - Ⲭk-1 |  ⩽  Ɛ .

