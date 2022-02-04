import numpy as np

def lu_Decomposition(A, B):
    
    L = np.zeros((3,3))                                                 # Instanciação das matrizes L e U
    U = np.zeros((3, 3))
    
    for j in range(3) :                                                 # Passo 1
        U[0][j] = A[0][j]
    
    for i in range(2) :                                                 # Passo 2
        L[i+1][0] = A[i+1][0] / U[0][0]
        
    for j in range(2) :                                                 # Passo 3
        U[1][j+1] = A[1][j+1] - L[1][0] * U[0][j+1]
        
    for i in range(1) :                                                 # Passo 4
        L[i+2][1] = (A[i+2][1] - L[i+2][0] * U[0][1]) / U[1][1]
        
    sum = 0
    
    for i in range(2) :
        sum += L[2][i] * U[i][2]
        
    U[2][2] = A[2][2] - sum                                             # Passo 5
    
    for i in range(3) :                                                 # Preenche com ums, a diagonal principal de L
        L[i][i] = 1
    
    print("\nMatriz L:\n")
    print(L)
    print("\nMatriz U:\n")
    print(U)
    
    Y = np.zeros((3,1))                                                 # Instanciação da matriz Y
    
    Y[0][0] = B[0][0] / L[0][0]                                         # Passos para o preenchimento da matriz Y

    Y[1][0] = (B[1][0] - L[1][0] * Y[0][0]) / L[1][1] 

    Y[2][0] = (B[2][0] - L[2][0] * Y[0][0] - L[2][1] * Y[1][0]) / L[2][2]
    
    print("\nMatriz Y:\n")
    print(Y)
    
    X = np.zeros((3,1))                                                 # Instanciação da matriz X
    
    X[2][0] = Y[2][0] / U[2][2]                                         # Passos para o preenchimento da matriz X

    X[1][0] = (Y[1][0] - U[1][2] * X[2][0]) / U[1][1]

    X[0][0] = (Y[0][0] - U[0][1] * X[1][0] - U[0][2] * X[2][0]) / U[0][0]
    
    print("\n\nSolução: X1 =",round(X[0][0], 2),", X2 =",round(X[1][0], 2),", X3 =",round(X[2][0], 2),"\n")
    
    
def main():
    
    print("\nDecomposição LU")
    
    print("\nInsira as entradas das Matrizes A e B:")
    
    print("\nExemplo:\n")
    print("\n5x1 + 2x2 + 1x3 = 0")    
    print("\n3x1 + x2 + 4x3 = -7")    
    print("\nx1 + x2 + 3x3 = -5")  
    print("\n\nEntradas de A:")
    print("\na11 = 5 ; a12 = 2 ; a13 = 1")
    print("\na21 = 3 ; a22 = 1 ; a23 = 4")
    print("\na31 = 1 ; a32 = 1 ; a33 = 3")
    print("\n\nEntradas de B:")
    print("\nB1 = 0 ; B2 = -7 ; B3 = -5\n")
    
    A = np.zeros((3,3))
    B = np.zeros((3, 1))
    
    for i in range(3) : 
        print("\na",i+1,"1 = ", end = "")
        A[i][0] = float(input())
        print("a",i+1,"2 = ", end = "")
        A[i][1] = float(input())
        print("a",i+1,"3 = ", end = "")
        A[i][2] = float(input())
        print("B",i+1,"= ", end = "")
        B[i][0] = float(input())
        
    print("\nMatriz A:\n")
    print(A)
    print("\nMatriz B:\n")
    print(B)
    
    lu_Decomposition(A, B)
    
if __name__ == "__main__" :
    main()
    
