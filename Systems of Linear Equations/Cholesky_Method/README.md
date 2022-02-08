# Método de Cholesky


### **Visão Geral**

Dado um sistema com **η** equações e **η** variáveis, dizemos que sua solução pode ser obtida através do **Método de Cholesky**, se a **matriz A** em questão é **Simétrica** (**G = G<sup>t</sup>**) **Positiva Definida** (**det(Ak) > 0 , ∀ k**). Sob essas circunstâncias, o método prevê que **A** pode ser decomposta em **G . G<sup>t</sup>** , sendo **G** uma **Matriz Triangular Inferior** com elementos diagonais positivos. Dese modo, obtemos que:

* **A . X = B** é equivalente a **G.G<sup>t</sup>.X = B** ;

* Tomando **G<sup>t</sup> . X = Y** , temos que : **G . Y = B** ;

* E calculando **Y** , podemos descobrir **X** : **G<sup>t</sup> . X = Y** .


### **Aplicação do Método**

Para calcularmos as entradas da matriz **G** , temos fórmulas propostas pelo método. Após isso, realizamos o processo descrito anteriormente sobre a equação **G.G<sup>t</sup>.X = B** , usando algoritmos que são notáveis durante o cálculo de **X** . 

Para obtenção de **G** :

1. Diagonal Principal :

    * <img src="https://latex.codecogs.com/svg.image?g11&space;=&space;\sqrt{a11}"/> ;

    * <img src="https://latex.codecogs.com/svg.image?gii&space;=&space;(aii&space;-&space;\sum_{k=1}^{i-1}&space;(gik)^{2})^{1/2}&space;,&space;i&space;=&space;2,&space;3,&space;...,&space;\eta&space;"/> ;

2. Demais elementos :

    * <img src="https://latex.codecogs.com/svg.image?gi1&space;=&space;\frac{ai1}{g11}&space;,&space;i&space;=&space;2,&space;3,&space;...,&space;\eta&space;"/> ;

    * <img src="https://latex.codecogs.com/svg.image?gi2&space;=&space;\frac{ai2-gi1.g21&space;}{g22}&space;,&space;i&space;=&space;3,&space;4,&space;...,&space;\eta&space;"/> ;

    * <img src="https://latex.codecogs.com/svg.image?gij&space;=&space;\frac{aij&space;-&space;\sum_{k=1}^{j-1}&space;(gik.gjk)}{gjj}&space;,&space;2&space;\leqslant&space;j&space;<&space;i"/> .

Para solução do sistema (3 x 3) :

1. G . Y = B :

    * Y1 = B1 / g11 ;

    * Y2 = (B2 - g21 . Y1) / g22 ;

    * Y3 = (B3 - g31 . Y1 - g32 . Y2) / g33 .

2. G<sup>t</sup> . X = Y : 

    * X3 = Y3 / gT33 ;

    * X2 = (Y2 - gT23 . X3) / gT22 ;

    * X1 = (Y1 - gT12 . X2 - gT13 . X3) / gT11 .