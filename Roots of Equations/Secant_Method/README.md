# Método da Secante


### **Visão Geral**

Encontraremos um intervalo **[α, β]** que contenha uma e somente uma raiz. Em seguida, definiremos **Ⲭ0 = α** e **Ⲭ1 = β**, e aplicaremos o método. A ideia é traçarmos uma reta secante sobre os pontos **(x, y)** para **Ⲭ0** e **Ⲭ1**, e determinarmos a intersecção da mesma com o eixo das abscissas como **Ⲭ2** . A partir disso, se **f(α) < 0** , seguimos delineando retas secantes entre **β** e **ⲬK**, e caso contrário, entre **α** e **ⲬK**, até que **ⲬK+1** satisfaça o **Critério de Parada** desejado.

* **Critério de Parada**: após cada iteração, verificamos se o resultado obtido tem a **precisão numérica** desejada. Para isso, utilizamos a fórmula: **| Ⲭk+1 - Ⲭk |  ⩽  Ɛ** . 

    * **Ⲭk+1** corresponde ao resultado da iteração atual, **Ⲭk** ao resultado da iteração anterior, e **Ɛ** representa a precisão (Ex. **Ɛ = 10^-3**).


### **Especificações**

* Teorema: Se uma função contínua **f(Ⲭ)** assume valores de sinais opostos nos pontos extremos do intervalo **[α, b]**, isto é, **f(α) . f(β) < 0** , então, o intervalo conterá, no mínimo, uma raiz da equação. Em outras palavras, haverá, no mínimo, um número **ξ ∈ (α, β)**, tal que **f(ξ) = 0** ;

* Propriedade: A raiz **ξ** será definida e única se **f'(Ⲭ)** existir e preservar o sinal dentro do intervalo **(α, β)**, isto é, se **f'(Ⲭ) > 0** ou **f'(Ⲭ) < 0** , se **Ⲭ ∈ (α, β)** ;

* Propriedade: Nesse método, consideramos **Ⲭ0 = α** e **Ⲭ1 = β** , independentemente dos valores de **α** e **β**.


### **Aplicação do Método**

Para encontrarmos um valor para **Ⲭk+1** que satisfaça o **Critério de Parada** e seja **raiz da função**, executamos os seguintes passos:

* Nota: Esse método se assemelha ao Método de Newton-Raphson, no entanto, busca eliminar a utilização de derivadas recorrendo à definição das mesmas, a fim de diminuir o número de operações em prol de uma melhor acurácia: 

    * f'(Ⲭk) = lim Ⲭ -> Ⲭk ( (f(Ⲭ) - f(Ⲭk)) ÷ (Ⲭ - Ⲭk) ) 

    * Considerando Ⲭ = Ⲭk-1 :

        * f'(Ⲭk) ≈ ( (f(Ⲭk-1) - f(Ⲭk)) ÷ (Ⲭk-1 - Ⲭk) ) = ( (f(Ⲭk) - f(Ⲭk-1)) ÷ (Ⲭk - Ⲭk-1) )
    
    * Substituindo o resultado anterior na fórmula do Método de Newton-Raphson:

        * Ⲭk+1 = Ⲭk - ( (f(Ⲭk) . (Ⲭk - Ⲭk-1)) ÷ (f(Ⲭk) - f(Ⲭk-1)) )


1. Para K = 1 :

    * **Ⲭ0** = **α** , **Ⲭ1** = **β** ;

    * Ⲭ2 = Ⲭ1 - ( (f(Ⲭ1) . (Ⲭ1 - Ⲭ0)) ÷ (f(Ⲭ1) - f(Ⲭ0)) ) ;

    * Critério de Parada: | Ⲭ2 - Ⲭ1 |  ⩽  Ɛ ;

2. Para K = η :

    * Ⲭk+1 = Ⲭk - ( (f(Ⲭk) . (Ⲭk - Ⲭk-1)) ÷ (f(Ⲭk) - f(Ⲭk-1)) ) ;

    * Critério de Parada: | Ⲭk+1 - Ⲭk |  ⩽  Ɛ .

    