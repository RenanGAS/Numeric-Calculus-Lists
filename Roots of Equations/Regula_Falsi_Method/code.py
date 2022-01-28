from sympy import *
import math
from prettytable import PrettyTable

def regulaFalsiMethod(a, b, f, stopC, maxIt):

    t = PrettyTable()                                                   # Cria a tabela
    t.field_names = ["K", "xK-1 / x", "xK", "xK+1", "|xK+1 - xK|"]      # Define as colunas

    x = a                                                               # Ⲭ0 = α
    xK = b                                                              # Ⲭ1 = β

    for i in range(maxIt):

        xPlus = xK - ((f(xK) * (xK - x)) / (f(xK) - f(x)))              # Executa o método
                         
        t.add_row([i, x, xK, xPlus, abs(xPlus - xK)])                   # Gera as linhas da tabela
            
        if abs(xPlus - xK) <= stopC :                                   # Verifica o Critério de Parada
                print(t)
                print("\nRaiz da equação:",xPlus)
                print("\n")
                break
        
        if ((f(xK)*f(xPlus)) < 0) :                                     # Faz a validação e atualização do valor da entrada Ⲭk-1 (ou Ⲭ , por convenção)
            x = xK
                                                    
        xK = xPlus                                                      # Atualiza o valor de Ⲭk para a próxima iteração


def main():

    print("\nMétodo Regula Falsi")

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
    
    regulaFalsiMethod(a, b, f, stopC, maxIt)                           # Executa o Método Regula Falsi


if __name__ == "__main__":
    main()