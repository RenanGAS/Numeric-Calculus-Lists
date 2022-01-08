import math
 
def bisectionMethod(a, b, f, stopC, maxIt):
    
    for i in range(maxIt):
        
        A = f(a)
        B = f(b)
        x = (a + b)/2                           # Determina o ponto médio do intervalo
        X = f(x)
        
        if i != 0 :  
            if abs(x-x_ant) <= stopC :          # Verifica o Critério de Parada
                print("\nRaiz da equação:",x)
                break

        if X*A < 0 :                            # Define o intervalo em que se encontra a raiz
            b = x
        elif X*B < 0 :
            a = x
            
        x_ant = x                               # Armazena a raiz atual
        
                
def main():
    print("\nMétodo da Bissecante")

    print("\nDigite a função:")
    str_f = input("\nf(x) = ")

    f = lambda x : eval(str_f)

    print("\nEscolha um intervalo [α, β] tal que f(α) . f(β) < 0 :")
    a = float(input("\nα = "))
    b = float(input("\nβ = "))

    if f(a)*f(b) > 0:
        print("\nErro: f(",a,") =", f(a), ", f(",b,") =",f(b))
        a = float(input("\nα = "))
        b = float(input("\nβ = "))

    print("\nEntradas aceitas: f(",a,") =", f(a),", f(",b,") =",f(b))
    
    if a > b:
        aux = b
        b = a
        a = aux

    print("\nIntervalo definido: [",a,",",b,"]")
    
    stopC = float(eval(input("\nDigite o Critério de Parada desejado (Ex. 10**-3) : ")))
    
    maxIt = int(input("\nDigite o número máximo de iterações que o método deve realizar (Ex. 20) : "))
    
    print("\nDado que α =", a,", β =", b,"e Ɛ =", stopC,"temos que o método realizará um número maior ou igual a", round((math.log2((b-a)/stopC)-1)),"iterações")
    
    bisectionMethod(a, b, f, stopC, maxIt)

if __name__ == "__main__":
    main()
