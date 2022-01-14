from sympy import *
import math
from prettytable import PrettyTable

def secantMethod(a, b, f, stopC, maxIt):

    t = PrettyTable()                                                   # Cria a tabela
    t.field_names = ["K", "xK-1", "xK", "xK+1", "|xK+1 - xK|"]          # Define as colunas

    xMinus = a                                                          # Ⲭ0 = α
    xK = b                                                              # Ⲭ1 = β

    for i in range(maxIt):

        xPlus = xK - ((f(xK) * (xK - xMinus)) / (f(xK) - f(xMinus)))    # Executa o método
                         
        t.add_row([i, xMinus, xK, xPlus, abs(xPlus - xK)])              # Gera as linhas da tabela
            
        if abs(xPlus - xK) <= stopC :                                   # Verifica o Critério de Parada
                print(t)
                print("\nRaiz da equação:",xPlus)
                print("\n")
                break

        xMinus = xK                                                     # Atualiza os valores de Ⲭk-1 e Ⲭk para a próxima iteração
        xK = xPlus


def main():

    print("\nMétodo da Secante")

    print("\nDigite a função:")
    str_f = input("\nf(x) = ")

    f = lambda x : eval(str_f)                                          # Cria uma função para realizar a substituição de variável na equação

    print("\nEscolha um intervalo [α, β] tal que f(α) . f(β) < 0 :")
    a = float(input("\nα = "))
    b = float(input("\nβ = "))

    while (f(a)*f(b) > 0) :                                             # Verifica se as entradas α e β satisfazem a condição
        print("\nErro: f(",a,") =", f(a), ", f(",b,") =",f(b))
        a = float(input("\nα = "))
        b = float(input("\nβ = "))

    print("\nEntradas aceitas: f(",a,") =", f(a),", f(",b,") =",f(b))
    
    if a > b:                                                           # Garante que o intervalo seja válido: β > α
        aux = b
        b = a
        a = aux

    print("\nIntervalo definido: [",a,",",b,"]")
    
    stopC = float(eval(input("\nDigite o Critério de Parada desejado (Ex. 10**-3) : ")))
    
    maxIt = int(input("\nDigite o número máximo de iterações que o método deve realizar (Ex. 20) : "))

    print("\n")
    
    secantMethod(a, b, f, stopC, maxIt)                                 # Executa o Método da Secante


if __name__ == "__main__":
    main()