from sympy import *                                             # Necessário para que o usuário possa colocar funções trigonométricas como entrada
import math
from prettytable import PrettyTable
    
def bisectionMethod(a, b, f, stopC, maxIt):
    
    t = PrettyTable()                                           # Cria a tabela
    t.field_names = ["K", "αK", "βK", "f(αK)", "f(βK)",         # Define as colunas
                     "xK", "f(xK)", "|xK - xK-1|"]
    
    for i in range(maxIt):
        A = f(a)
        B = f(b)
        x = (a + b)/2                                           # Determina o ponto médio do intervalo
        X = f(x)
            
        if i == 0 :                                             # Gera as linhas
            t.add_row([i, a, b, f(a), f(b), x, f(x), "--"])
        else:
            t.add_row([i, a, b, f(a), f(b), x, f(x), abs(x - x_ant)])
            
        if i != 0 :  
            if abs(x-x_ant) <= stopC :                          # Verifica o Critério de Parada
                print(t)
                print("\nRaiz da equação:",x)
                break

        if X*A < 0 :                                            # Define o intervalo em que se encontra a raiz
            b = x
        elif X*B < 0 :
            a = x
            
        x_ant = x                                               # Armazena a raiz atual
        
                
def main():
    
    print("\nMétodo da Bissecção")

    print("\nDigite a função:")
    str_f = input("\nf(x) = ")

    f = lambda x : eval(str_f)                                  # Cria uma função para realizar a substituição de variável na equação

    print("\nEscolha um intervalo [α, β] tal que f(α) . f(β) < 0 :")
    a = float(input("\nα = "))
    b = float(input("\nβ = "))

    while (f(a)*f(b) > 0) :                                           # Verifica se as entradas α e β satisfazem a condição
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
    
    print("\nDado que α =", a,", β =", b,"e Ɛ =", stopC,"temos que o método realizará um número maior ou igual a", round((math.log2((b-a)/stopC)-1)),"iterações :\n")
    
    bisectionMethod(a, b, f, stopC, maxIt)                      # Executa o Método da Bissecção
    

if __name__ == "__main__":
    main()
