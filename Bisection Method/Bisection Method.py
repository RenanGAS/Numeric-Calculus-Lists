from sympy import symbols

print("\nMétodo da Bissecante")

print("\nDigite a função:")
str_f = input("\nf(x) = ")

def f(x):
    func = eval(str_f)
    return func

def main():
    print("\nEscolha um intervalo [a, b] tal que f(a) . f(b) < 0 :")
    a = float(input("\na = "))
    b = float(input("\nb = "))

    if f(a)*f(b) > 0:
        print("\nErro: f(",a,") =", f(a), ", f(",b,") =",f(b))
        a = float(input("\na = "))
        b = float(input("\nb = "))

    print("\nEntradas aceitas: f(",a,") =", f(a),", f(",b,") =",f(b))
    
    if a > b:
        aux = b
        b = a
        a = aux

    print("\nIntervalo definido: [",a,",",b,"]")

if __name__ == "__main__":
    main()
