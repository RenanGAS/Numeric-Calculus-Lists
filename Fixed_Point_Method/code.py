from sympy import *
import math
from prettytable import PrettyTable

def fixedPointMethod(g, xk, stopC, maxIt):

    t = PrettyTable()                                                   # Cria a tabela
    t.field_names = ["K", "xK-1 / x", "xK", "xK+1", "|xK+1 - xK|"]      # Define as colunas


def main():

    print("\nMétodo do Ponto Fixo")

    print("\nDigite a função de iteração correspondente a função em questão:")
    print("\nEx. f(x) = cos(x)-x -> g(x) = cos(x)")
    str_g = input("\ng(x) = ")

    g = lambda x : eval(str_g)                                          # Cria uma função para realizar a substituição de variável na equação
    
    xk = float(input("\nDigite um valor inicial, xk, para realização da aproximação:"))
    
    stopC = float(eval(input("\nDigite o Critério de Parada desejado (Ex. 10**-3) : ")))
    
    maxIt = int(input("\nDigite o número máximo de iterações que o método deve realizar (Ex. 20) : "))

    print("\n")
    
    fixedPointMethod(g, xk, stopC, maxIt)                             # Executa o Método do Ponto Fixo


if __name__ == "__main__":
    main()