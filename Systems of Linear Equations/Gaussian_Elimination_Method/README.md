# Método de Eliminação de Gauss


### **Visão Geral**

Dado um sistema com **η** equações e **η** variáveis, podemos obter sua solução através do **Método de Eliminação de Gauss com pivotamento parcial** . A ideia é transformarmos a **Matriz Ampliada** do sistema, em uma **Matriz Triangular Superior** através de **Operações Elementares** . Para tanto, temos as seguintes fórmulas:

* <img src="https://latex.codecogs.com/svg.image?a{_{ij}}^{(k&plus;1)}&space;=&space;a{_{ij}}^{(k)}&space;-&space;a{_{kj}}^{(k)}\frac{a{_{ik}}^{(k)}}{a{_{kk}}^{(k)}}"/> ;

* <img src="https://latex.codecogs.com/svg.image?b{_{i}}^{(k&plus;1)}&space;=&space;b{_{i}}^{(k)}&space;-&space;b{_{k}}^{(k)}\frac{a{_{ik}}^{(k)}}{a{_{kk}}^{(k)}}"/> ;

    * <img src="https://latex.codecogs.com/svg.image?k&space;=&space;1,&space;2,&space;...,&space;\eta-1"/> ;

    * <img src="https://latex.codecogs.com/svg.image?i&space;=&space;k&plus;1,&space;...,&space;\eta"/> ;

    * <img src="https://latex.codecogs.com/svg.image?j&space;=&space;k,&space;...,&space;\eta" title="j = k, ..., \eta" /> .

Os algoritmos acima identificam o **Método de Eliminação de Gauss** , que leva em consideração uma matriz A com elementos não nulos na **Diagonal Principal** . Para que possamos generalizar o método, devemos realizar o chamado **pivotamento parcial** que consiste em garantir que os números da diagonal sejam maiores em módulo do que os abaixo deles em suas colunas. Essa verificação é feita antes de cada iteração, **η - 1** vezes, e quando a condição não é atendida, deve-se permutar a linha que contém o maior elemento com a linha da diagonal em questão.


### **Aplicação do Método**

Para obtermos a Matriz Triangular Superior, temos a dinâmica das iterações e as fórmulas propostas pelo método. Devemos lembrar de realizar o pivotamento antes de cara ciclo, e após essas etapas, aplicar os algoritmos notáveis para a solução da matriz ampliada final. 

* Exemplo de pivotamento :

    * Dado a matriz <img src="https://latex.codecogs.com/svg.image?\begin{pmatrix}&space;1&space;&&space;&space;12&space;&&space;3&space;&&space;|&space;&&space;1\\&space;4&space;&&space;6&space;&&space;9&space;&&space;|&space;&&space;3\\&space;3&space;&&space;&space;5&space;&&space;7&space;&&space;|&space;&&space;7\\\end{pmatrix}"/> , ao pivotarmos o elemento <img src="https://latex.codecogs.com/svg.image?a_{11}"/> temos o seguinte resultado:

        * <img src="https://latex.codecogs.com/svg.image?\begin{pmatrix}&space;4&space;&&space;6&space;&&space;9&space;&&space;|&space;&&space;3\\&space;1&space;&&space;&space;12&space;&&space;3&space;&&space;|&space;&&space;1\\&space;3&space;&&space;&space;5&space;&&space;7&space;&&space;|&space;&&space;7\\\end{pmatrix}"/> .
        

Para o cálculo da Matriz Triangular Superior (η = 3):

* Pivotamento da entrada <img src="https://latex.codecogs.com/svg.image?a_{11}"/> ;

* K = 1, i = 2, j = 1 :

    * <img src="https://latex.codecogs.com/svg.image?{a_{21}}^{(2)}&space;=&space;{a_{21}}^{(1)}&space;-&space;{a_{11}}^{(1)}\frac{{a_{21}}^{(1)}}{{a_{11}}^{(1)}}"/> ;

* K = 1, i = 2, j = 2 :

    * <img src="https://latex.codecogs.com/svg.image?{a_{22}}^{(2)}&space;=&space;{a_{22}}^{(1)}&space;-&space;{a_{12}}^{(1)}\frac{{a_{21}}^{(1)}}{{a_{11}}^{(1)}}"/> ;

* K = 1, i = 2, j = 3 :

    * <img src="https://latex.codecogs.com/svg.image?{a_{23}}^{(2)}&space;=&space;{a_{23}}^{(1)}&space;-&space;{a_{13}}^{(1)}\frac{{a_{21}}^{(1)}}{{a_{11}}^{(1)}}"/> ;

    * <img src="https://latex.codecogs.com/svg.image?{b_{2}}^{(2)}&space;=&space;{b_{2}}^{(1)}&space;-&space;{b_{1}}^{(1)}\frac{{a_{21}}^{(1)}}{{a_{11}}^{(1)}}"/> ;

* Pivotamento da entrada <img src="https://latex.codecogs.com/svg.image?a_{22}"/> ;

* K = 2, i = 3, j = 1 :

    * <img src="https://latex.codecogs.com/svg.image?{a_{31}}^{(3)}&space;=&space;{a_{31}}^{(2)}&space;-&space;{a_{21}}^{(2)}\frac{{a_{32}}^{(2)}}{{a_{22}}^{(2)}}"/> ;
 
* K = 2, i = 3, j = 2 :

    * <img src="https://latex.codecogs.com/svg.image?{a_{32}}^{(3)}&space;=&space;{a_{32}}^{(2)}&space;-&space;{a_{22}}^{(2)}\frac{{a_{32}}^{(2)}}{{a_{22}}^{(2)}}"/> ;

* K = 2, i = 3, j = 3 :

    * <img src="https://latex.codecogs.com/svg.image?{a_{33}}^{(3)}&space;=&space;{a_{33}}^{(2)}&space;-&space;{a_{23}}^{(2)}\frac{{a_{32}}^{(2)}}{{a_{22}}^{(2)}}"/> ;

    * <img src="https://latex.codecogs.com/svg.image?{b_{3}}^{(3)}&space;=&space;{b_{3}}^{(2)}&space;-&space;{b_{2}}^{(2)}\frac{{a_{32}}^{(2)}}{{a_{22}}^{(2)}}"/> .


Para solução da matriz :

* <img src="https://latex.codecogs.com/svg.image?x_{3}&space;=&space;\frac{b_{3}}{a_{33}}"/> ;

* <img src="https://latex.codecogs.com/svg.image?x_{2}&space;=&space;\frac{b_{2}&space;-&space;a_{23}\frac{b_{3}}{a_{33}}}{{a_{22}}}"/> ;

* <img src="https://latex.codecogs.com/svg.image?x_{1}&space;=&space;\frac{b_{1}&space;-&space;a_{12}\frac{b_{2}&space;-&space;a_{23}\frac{b_{3}}{a_{33}}}{a_{22}}&space;-&space;a_{13}\frac{b_{3}}{a_{33}}}{{a_{11}}"/> .