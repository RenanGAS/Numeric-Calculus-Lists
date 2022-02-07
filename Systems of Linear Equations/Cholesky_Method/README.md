# Método de Cholesky


### **Visão Geral**

Dado um sistema com **η** equações e **η** variáveis, dizemos que sua solução pode ser obtida através do **Método de Cholesky**, se a **matriz A** em questão é **Simétrica** (**G = G<sup>t</sup>**) **Positiva Definida** (**det(Ak) > 0 , ∀ k**). Sob essas circunstâncias, o método prevê que **A** pode ser decomposta em **G . G<sup>t</sup>** , sendo **G** uma **Matriz Triangular Inferior** com elementos diagonais positivos. Dese modo, obtemos que:

* **A . X = B** é equivalente a **G.G<sup>t</sup>.X = B** ;

* Tomando **G<sup>t</sup> . X = Y** , temos que : **G . Y = B** ;

* E calculando **Y** , podemos descobrir **X** : **G<sup>t</sup> . X = Y** .


### **Aplicação do Método**

Para calcularmos as entradas da matriz **G** , temos fórmulas propostas pelo método. Após isso, realizamos o processo descrito anteriormente sobre a equação **G.G<sup>t</sup>.X = B** , usando algoritmos que são notáveis durante o cálculo de **X** . 

Para obtenção de **G** :

1. Elementos na Diagonal Principal :

    * g11 = <img src="https://latex.codecogs.com/svg.image?\sqrt{a11}"/> ;

    * gii = <img src="https://latex.codecogs.com/svg.image?(aii&space;-&space;\sum_{k=1}^{i-1}&space;(gik)^{2})^{1/2}&space;"/> , i = 2, 3, ..., η .

