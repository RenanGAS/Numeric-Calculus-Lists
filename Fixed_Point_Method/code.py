from numpy import *
from sympy import *
from prettytable import PrettyTable

def fixedPointMethod(f, F, xK, stopC):

    t = PrettyTable()                                                   # Cria a tabela
    t.field_names = ["K", "xK", "xK+1", "|f(xK+1)|"]                    # Define as colunas
    
    numIt = 0
    xKPlus1 = 0
    
    while numIt < 200 :
        
        xKPlus1 = F(xK)                                                 # Executa o Método
        
        t.add_row([numIt, xK, xKPlus1, abs(f(xKPlus1))])                # Gera as linhas da tabela
        
        if abs(f(xKPlus1)) <= stopC :                                   # Toma como Critério de Parada o momento em que a aproximação xK+1 é uma raiz de f(Ⲭ) de precisão Ɛ 
            print(t)                                                    # Faz-se uso disso para evitar que Funções de Iteração inapropriadas gerem resultados
            print("\nRaiz da função:", xKPlus1)
            print("\n")
            break
        
        xK = xKPlus1                                                    # Atualiza o valor de xK para próxima iteração
        
        numIt += 1                                                   
        
    if numIt == 200 :                                                   # Verifica a validade da Função de Iteração
        print("\nFunção de Iteração inválida\n")                   
        main()
        

def main():

    print("\nMétodo do Ponto Fixo")
    
    print("\nDigite a função:")
    print("\nEx. f(x) = cos(x)-x")
    str_f = input("\nf(x) = ")
    
    f = lambda x : eval(str_f) 
    
    print("\nDigite a Função de Iteração correspondente:")
    print("\nEx. f(x) = cos(x)-x → F(x) = cos(x)")
    str_F = input("\nF(x) = ")

    F = lambda x : eval(str_F)                                          # Cria uma função para realizar a substituição de variável na equação
    
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
    
    xK = float(input("\nDigite um valor inicial, x0, que esteja dentro do intervalo para realização da aproximação: "))
    
    stopC = float(eval(input("\nDigite o Critério de Parada desejado (Ex. 10**-3) : ")))

    print("\n")
    
    fixedPointMethod(f, F, xK, stopC)                                   # Executa o Método do Ponto Fixo


if __name__ == "__main__":
    main()