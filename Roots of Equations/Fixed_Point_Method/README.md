# Método do Ponto Fixo


### **Objetivo**

Calcular a **raiz de uma função** (Determinar um valor para **Ⲭ** tal que **f(Ⲭ) = 0**).


### **Visão Geral**

Encontraremos um intervalo **[α, β]** que contenha uma e somente uma raiz. Em seguida, definiremos uma Função de Iteração **F(Ⲭ)** de **f(Ⲭ)**, que satisfaça o seguinte teorema: 

* Teorema: Seja **ξ ∈ [α, β]** uma raiz da equação **f(Ⲭ) = 0** e **F(Ⲭ)** contínua, diferenciável em **[α, β]** e **F(Ⲭ) ∈ [α, β]**. Se **|F'(Ⲭ)| ⩽ k < 1** para todos os pontos em **[α, β]** e **Ⲭ0 ∈ [α, β]** , então, os valores dados pela equação **Ⲭk+1 = F(Ⲭk) , k = 0, 1, ...** converge para **ξ** .

    * Para construir uma Função de Iteração, precisamos isolar um termo **Ⲭ** de **f(Ⲭ)** , obtendo **F(Ⲭ)** no outro lado da igualdade. **Ex.: cos(Ⲭ) - Ⲭ = 0 ⇔ cos(Ⲭ) = Ⲭ → F(Ⲭ) = cos(Ⲭ)** . Deve-se fazer esse processo até que obtenha-se uma função que satisfaça as condições do Teorema, no entanto, para realizar a verificação de **F(Ⲭ)** no código, delimitamos um máximo de 200 iterações. Desse modo, caso o algoritmo chegue a essa marca, consideramos que a função não está correta.

Após determinar **F(Ⲭ)** , realizamos iterações sobre a expressão dada no Teorema, a saber, **Ⲭk+1 = F(Ⲭk) , k = 0, 1, ...** , até que o resultado satisfaça o **Critério de Parada** desejado.

* **Critério de Parada**: após cada iteração, verificamos se o resultado obtido tem a **precisão numérica** desejada. Para isso, utilizamos a fórmula: **| Ⲭk+1 - Ⲭk |  ⩽  Ɛ** . 

    * **Ⲭk+1** corresponde ao resultado da iteração atual, **Ⲭk** ao resultado da iteração anterior, e **Ɛ** representa a precisão (Ex. **Ɛ = 10^-3**).


### **Especificações**

* Teorema: Se uma função contínua **f(Ⲭ)** assume valores de sinais opostos nos pontos extremos do intervalo **[α, b]**, isto é, **f(α) . f(β) < 0** , então, o intervalo conterá, no mínimo, uma raiz da equação. Em outras palavras, haverá, no mínimo, um número **ξ ∈ (α, β)**, tal que **f(ξ) = 0** ;

* Propriedade: A raiz **ξ** será definida e única se **f'(Ⲭ)** existir e preservar o sinal dentro do intervalo **(α, β)**, isto é, se **f'(Ⲭ) > 0** ou **f'(Ⲭ) < 0** , se **Ⲭ ∈ (α, β)** ;

* Definição: Um número **p** é dito **ponto fixo** de uma função **g**, se **g(p) = p** ;

* Propriedade: Supondo que **g(Ⲭ)** tenha um ponto fixo em **p** , ou seja, **g(p) = p** , a função **f(Ⲭ) = Ⲭ - g(Ⲭ)** tem um zero em **p**, pois: **f(p) = p - g(p) = p - p = 0** .


### **Aplicação do Método**

Para encontrarmos um valor para **Ⲭk+1** que satisfaça o **Critério de Parada** e seja **raiz da função**, executamos os seguintes passos:

1. Para K = 0 :

    * Atribuir a **Ⲭ0** qualquer valor dentro do intervalo **[α, β]** ;

    * Ⲭ1 = F(Ⲭ0) ;

    * Critério de Parada: | Ⲭ1 - Ⲭ0 |  ⩽  Ɛ ;

2. Para K = η :

    * ⲬK+1 = F(Ⲭk) ;

    * Critério de Parada: | Ⲭk+1 - Ⲭk |  ⩽  Ɛ .