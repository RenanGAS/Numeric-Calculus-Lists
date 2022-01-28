# Método de Newton-Raphson


### **Visão Geral**

Encontraremos um intervalo **[α, β]** que contenha uma e somente uma raiz. Em seguida, definiremos como **Ⲭ0** o valor de **α** ou **β**, dependendo de qual satisfazer a condição: **f(Ⲭ) . f''(Ⲭ) > 0** . Desse modo, sabendo que **f'(Ⲭ0) = tg(𝜃)** , temos que **f'(Ⲭ0) = f(Ⲭ0) ÷ (Ⲭ0 - Ⲭ1)** , sendo **Ⲭ1 = Ⲭ0 - (f(Ⲭ0) ÷ f'(Ⲭ0))** . Nesse contexto, **Ⲭ1** corresponde ao **ponto** em que, a reta que é tangente à função no ponto **f'(Ⲭ0)** , toca o **eixo das abscissas**. Realizaremos iterações sobre esse processo até que o resultado satisfaça o **Critério de Parada** desejado.

* **Critério de Parada**: após cada iteração, verificamos se o resultado obtido tem a **precisão numérica** desejada. Para isso, utilizamos a fórmula: **| Ⲭk+1 - Ⲭk |  ⩽  Ɛ** . 

    * **Ⲭk+1** corresponde ao resultado da iteração atual, **Ⲭk** ao resultado da iteração anterior, e **Ɛ** representa a precisão (Ex. **Ɛ = 10^-3**).


### **Especificações**

* Teorema: Se uma função contínua **f(Ⲭ)** assume valores de sinais opostos nos pontos extremos do intervalo **[α, b]**, isto é, **f(α) . f(β) < 0** , então, o intervalo conterá, no mínimo, uma raiz da equação. Em outras palavras, haverá, no mínimo, um número **ξ ∈ (α, β)**, tal que **f(ξ) = 0** ;

* Propriedade: A raiz **ξ** será definida e única se **f'(Ⲭ)** existir e preservar o sinal dentro do intervalo **(α, β)**, isto é, se **f'(Ⲭ) > 0** ou **f'(Ⲭ) < 0** , se **Ⲭ ∈ (α, β)** ;

* Teorema: Uma condição suficiente para a convergência do método de Newton-Raphson é, **f'(Ⲭ) e f''(Ⲭ)** forem não-nulas e preservem o sinal em **(α, β)** , de modo que **f(Ⲭ0) . f''(Ⲭ0) > 0** . Assim, temos que se **f(α) . f''(α) > 0** , **Ⲭ0 = α** ; caso contrário, **Ⲭ0 = β** .


### **Aplicação do Método**

Para encontrarmos um valor para **Ⲭk+1** que satisfaça o **Critério de Parada** e seja **raiz da função**, executamos os seguintes passos:

1. Para K = 0 :

    * Determinar se **Ⲭ0** receberá **α** ou **β** ;

    * Ⲭ1 = Ⲭ0 - (f(Ⲭ0) ÷ f'(Ⲭ0)) ;

    * Critério de Parada: | Ⲭ1 - Ⲭ0 |  ⩽  Ɛ ;

2. Para K = η :

    * ⲬK+1 = Ⲭk - (f(Ⲭk) ÷ f'(Ⲭk)) ;

    * Critério de Parada: | Ⲭk+1 - Ⲭk |  ⩽  Ɛ .