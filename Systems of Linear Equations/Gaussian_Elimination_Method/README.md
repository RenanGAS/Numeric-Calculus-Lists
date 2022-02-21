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

Para obtermos a Matriz Triangular Superior, temos a dinâmica das iterações e as fórmulas propostas pelo método. Devemos lembrar de realizar o pivotamento antes de cara ciclo, e após essas etapas, aplicar os algoritmos notáveis para a solução da nova matriz ampliada. 

Para o cálculo da Matriz Triangular Superior (η = 3):

1. K = 1, i = 2, j = 1 :