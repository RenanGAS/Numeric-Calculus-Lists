from sympy import *
import math
from prettytable import PrettyTable

def newtonRaphsonMethod(a, b, f, stopC, maxIt):

    t = PrettyTable()                                           # Cria a tabela
    t.field_names = ["K", "xK", "xK+1", "|xK+1 - xK|"]          # Define as colunas

    x = symbols('x')
    secDeriv = diff(f(x), x, x).subs(x, a)                      # Calcula f''(α)
    
    if f(a)*secDeriv > 0 :                                      # Determina o valor de x0
        xK = a
    else :
        xK = b
    
    for i in range(maxIt):

        firstDeriv = diff(f(x), x).subs(x, xK)                  # Calcula f'(xK)

        xKPlus1 = xK - (f(xK) / firstDeriv)                     # Executa o método
                         
        t.add_row([i, xK, xKPlus1, abs(xKPlus1 - xK)])          # Gera as linhas da tabela
            
        if abs(xKPlus1 - xK) <= stopC :                         # Verifica o Critério de Parada
                print(t)
                print("\nRaiz da equação:",xKPlus1)
                break

        xK = xKPlus1                                            # Atualiza o valor de xK para a próxima iteração


def main():

    print("\nMétodo de Newton-Raphson")

    print("\nDigite a função:")
    str_f = input("\nf(x) = ")

    f = lambda x : eval(str_f)                                  # Cria uma função para realizar a substituição de variável na equação

    print("\nEscolha um intervalo [α, β] tal que f(α) . f(β) < 0 :")
    a = float(input("\nα = "))
    b = float(input("\nβ = "))

    if f(a)*f(b) > 0:                                           # Verifica se as entradas α e β satisfazem a condição
        print("\nErro: f(",a,") =", f(a), ", f(",b,") =",f(b))
        a = float(input("\nα = "))
        b = float(input("\nβ = "))

    print("\nEntradas aceitas: f(",a,") =", f(a),", f(",b,") =",f(b))
    
    if a > b:                                                   # Garante que o intervalo seja válido: β > α
        aux = b
        b = a
        a = aux

    print("\nIntervalo definido: [",a,",",b,"]")
    
    stopC = float(eval(input("\nDigite o Critério de Parada desejado (Ex. 10**-3) : ")))
    
    maxIt = int(input("\nDigite o número máximo de iterações que o método deve realizar (Ex. 20) : "))
    
    newtonRaphsonMethod(a, b, f, stopC, maxIt)                      # Executa o Método de Newton-Raphson


if __name__ == "__main__":
    main()