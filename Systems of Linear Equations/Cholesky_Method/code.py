import numpy as np
import math

def cholesky_Method(A, B):
    
    G = np.zeros((3,3))                                                 # Instanciação das matrizes G e GT
    GT = G.transpose()
    
    G[0][0] = math.sqrt(A[0][0])
    
    for i in range(2) :
        G[i+1][0] = A[i+1][0] / G[0][0]
    
    G[1][1] = pow((A[1][1] - pow(G[1][0], 2)), 0.5)

    G[2][1] = (A[2][1] - G[2][0] * G[1][0]) / G[1][1]

    sum = 0

    for k in range(2) :
        sum += pow(G[2][k], 2)

    G[2][2] = pow((A[2][2] - sum), 0.5)  
    
    print("\nMatriz G:\n")
    print(G)
    print("\nMatriz G^t:\n")
    print(GT)
    
    Y = np.zeros((3,1))                                                 # Instanciação da matriz Y
    
    Y[0][0] = B[0][0] / G[0][0]                                         # Passos para o preenchimento da matriz Y

    Y[1][0] = (B[1][0] - G[1][0] * Y[0][0]) / G[1][1] 

    Y[2][0] = (B[2][0] - G[2][0] * Y[0][0] - G[2][1] * Y[1][0]) / G[2][2]
    
    print("\nMatriz Y:\n")
    print(Y)
    
    X = np.zeros((3,1))                                                 # Instanciação da matriz X
    
    X[2][0] = Y[2][0] / GT[2][2]                                         # Passos para o preenchimento da matriz X

    X[1][0] = (Y[1][0] - GT[1][2] * X[2][0]) / GT[1][1]

    X[0][0] = (Y[0][0] - GT[0][1] * X[1][0] - GT[0][2] * X[2][0]) / GT[0][0]
    
    print("\n\nSolução: X1 =",round(X[0][0], 2),", X2 =",round(X[1][0], 2),", X3 =",round(X[2][0], 2),"\n")
    
    
def main():
    
    print("\nMétodo de Cholesky")
    
    print("\nInsira as entradas das Matrizes A e B:")
    
    print("\nExemplo:\n")
    print("\n4x1 + 2x2 + -4x3 = 0")    
    print("\n2x1 + 10x2 + 4x3 = 6")    
    print("\n-4x1 + 4x2 + 9x3 = 5")  
    print("\n\nEntradas de A:")
    print("\na11 = 4 ; a12 = 2 ; a13 = -4")
    print("\na21 = 2 ; a22 = 10 ; a23 = 4")
    print("\na31 = -4 ; a32 = 4 ; a33 = 9")
    print("\n\nEntradas de B:")
    print("\nB1 = 0 ; B2 = 6 ; B3 = 5\n")
    
    A = np.zeros((3,3))                                                 # Instanciação das matrizes A e B
    B = np.zeros((3, 1))
    
    for i in range(3) :                                                 # Preenchimento das entradas de A e B
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
    
    cholesky_Method(A, B)                                              # Executa o Método de Cholesky
    
if __name__ == "__main__" :
    main()
    
