# Decomposição LU


# Visão Geral

Dado um sistema com **η** equações e **η** variáveis, dizemos que a solução pode ser obtida através da **Decomposição LU** , se **det(Ak) ≠ 0** para **k = 1, 2, ..., η-1** . Esta condição diz que o método é aplicável se, e somente se os **Menores Principais** de **A** tiverem determinantes não nulos. Assumindo que essas circunstâncias foram satisfeitas, temos então que **A** pode ser decomposta na multiplicação das matrizes **L** e **U** , tal que **L** é uma **Matriz Triangular Inferior** , com **l11 = l22 = ... = lnn = 1** , e **U** é uma **Matriz Triangular Superior** . Desse modo, obtemos que:

* **A . X = B** é equivalente a **L.U.X = B** ;

* Tomando **U . X = Y** , temos que : **L . Y = B** ;

* E calculando **Y** , podemos descobrir **X** : **U . X = Y** .