# Método Regula Falsi


### **Visão Geral**

Encontraremos um intervalo **[α, β]** que contenha uma e somente uma raiz. Em seguida, definiremos **Ⲭ0 = α** e **Ⲭ1 = β**, e aplicaremos o método. A ideia é traçarmos uma reta secante sobre os pontos **(x, y)** , para **Ⲭ0** e **Ⲭ1**, e determinarmos a intersecção da mesma com o eixo das abscissas como **Ⲭ2** . A partir disso, verificamos qual imagem, **f(Ⲭ0)** ou **f(Ⲭ1)**, tem sinal contrário à imagem **f(Ⲭ2)** , e delineamos outra reta secante entre **(Ⲭ2, f(Ⲭ2))** e o ponto que satisfaz a condição, sendo **Ⲭ3** a intersecção dessa reta com o eixo das abscissas. Essa seleção de pontos para construção da reta secante é o que diferencia o algoritmo do Método da Secante, e faz com que não obtenhamos resultados fora do intervalo **(α, β)** , agregando eficiência ao método. Realizamos essa validação de pontos e construção de retas secantes até que o resultado satisfaça o **Critério de Parada** desejado.

* **Critério de Parada**: após cada iteração, verificamos se o resultado obtido tem a **precisão numérica** desejada. Para isso, utilizamos a fórmula: **| Ⲭk+1 - Ⲭk |  ⩽  Ɛ** . 

    * **Ⲭk+1** corresponde ao resultado da iteração atual, **Ⲭk** ao resultado da iteração anterior, e **Ɛ** representa a precisão (Ex. **Ɛ = 10^-3**).


### **Especificações**

* Teorema: Se uma função contínua **f(Ⲭ)** assume valores de sinais opostos nos pontos extremos do intervalo **[α, b]**, isto é, **f(α) . f(β) < 0** , então, o intervalo conterá, no mínimo, uma raiz da equação. Em outras palavras, haverá, no mínimo, um número **ξ ∈ (α, β)**, tal que **f(ξ) = 0** ;

* Propriedade: A raiz **ξ** será definida e única se **f'(Ⲭ)** existir e preservar o sinal dentro do intervalo **(α, β)**, isto é, se **f'(Ⲭ) > 0** ou **f'(Ⲭ) < 0** , se **Ⲭ ∈ (α, β)** ;

* Propriedade: Nesse método, consideramos **Ⲭ0 = α** e **Ⲭ1 = β** , independentemente dos valores de **α** e **β**.


### **Aplicação do Método**

Para encontrarmos um valor para **Ⲭk+1** que satisfaça o **Critério de Parada** e seja **raiz da função**, executamos os seguintes passos:

* Nota: Esse método se assemelha ao Método da Secante, no entanto, busca aumentar sua eficiência realizando a seleção do valor que entrará em Ⲭk-1 para K > 1: 

    * Dado a fórmula do Método da Secante:

    * Ⲭk+1 = Ⲭk - ( (f(Ⲭk) . (Ⲭk - Ⲭk-1)) ÷ (f(Ⲭk) - f(Ⲭk-1)) )

    * Temos que **Ⲭk-1** corresponderá a **Ⲭk** ou **Ⲭk-1** da iteração anterior. O valor escolhido é aquele que, ainda na iteração anterior, tinha imagem de sinal contrário à **f(Ⲭk+1)** . Desse modo, como **Ⲭk-1** não é uma notação apropriada para o método, podemos anotar o algoritmo do Método Regula Falsi dessa maneira:

    * Ⲭk+1 = Ⲭk - ( (f(Ⲭk) . (Ⲭk - Ⲭ)) ÷ (f(Ⲭk) - f(Ⲭ)) )


1. Para K = 1 :

    * **Ⲭ0** = **α** , **Ⲭ1** = **β** ;

    * Ⲭ2 = Ⲭ1 - ( (f(Ⲭ1) . (Ⲭ1 - Ⲭ0)) ÷ (f(Ⲭ1) - f(Ⲭ0)) ) ;

    * Critério de Parada: | Ⲭ2 - Ⲭ1 |  ⩽  Ɛ ;

2. Para K = 2:

    * Se f(Ⲭ0) . f(Ⲭ2) < 0 , então Ⲭk-1 = Ⲭ0 ;

    * Se f(Ⲭ1) . f(Ⲭ2) < 0 , então Ⲭk-1 = Ⲭ1 ;
    
    * Ⲭ3 = Ⲭ2 - ( (f(Ⲭ2) . (Ⲭ2 - Ⲭ)) ÷ (f(Ⲭ2) - f(Ⲭ)) ) , Ⲭ = Ⲭ0 ou Ⲭ1 ;

    * Critério de Parada: | Ⲭ3 - Ⲭ2 |  ⩽  Ɛ ;

3. Para K = η :

    * Validação de Ⲭ ;

    * Ⲭk+1 = Ⲭk - ( (f(Ⲭk) . (Ⲭk - Ⲭ)) ÷ (f(Ⲭk) - f(Ⲭ)) ) ;

    * Critério de Parada: | Ⲭk+1 - Ⲭk |  ⩽  Ɛ .