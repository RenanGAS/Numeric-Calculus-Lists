# Decomposição LU


### **Visão Geral**

Dado um sistema com **η** equações e **η** variáveis, dizemos que a solução pode ser obtida através da **Decomposição LU** , se **det(Ak) ≠ 0** para **k = 1, 2, ..., η-1** . Esta condição diz que o método é aplicável se, e somente se os **Menores Principais** de **A** tiverem determinantes não nulos. Assumindo que essas circunstâncias são satisfeitas, temos então que **A** pode ser decomposta na multiplicação das matrizes **L** e **U** , tal que **L** é uma **Matriz Triangular Inferior** , com **l11 = l22 = ... = lnn = 1** , e **U** é uma **Matriz Triangular Superior** . Desse modo, obtemos que:

* **A . X = B** é equivalente a **L.U.X = B** ;

* Tomando **U . X = Y** , temos que : **L . Y = B** ;

* E calculando **Y** , podemos descobrir **X** : **U . X = Y** .


### **Aplicação do Método**

Para calcularmos as entradas das matrizes **L** e **U** , temos fórmulas propostas pelo método. Após isso, realizamos o processo descrito anteriormente sobre a equação **L.U.X = B** , usando algoritmos que são notáveis durante o cálculo de **X** . 

Para obtenção de **L** e **U** :

1. u1j = a1j , j = 1, 2, ..., η ;

2. li1 = ai1 / u11 , i = 2, ..., η ;

3. u2j = a2j - l21 . u1j , j = 2, ..., η ;

4. li2 = (ai2 - li1 . u12) / u22 , i = 3, ..., η ;

5. uij = aij - ∑ i-1 , k = 1 (lik . ukj) , i ≤ j ;


Para solução do sistema (3 x 3) :

1. L . Y = B :

    * Y1 = B1 / l11 ;

    * Y2 = (B2 - l21 . Y1) / l22 ;

    * Y3 = (B3 - l31 . Y1 - l32 . Y2) / l33 .

2. U . X = Y : 

    * X3 = Y3 / u33 ;

    * X2 = (Y2 - u23 . X3) / u22 ;

    * X1 = (Y1 - u12 . X2 - u13 . X3) / u11 .