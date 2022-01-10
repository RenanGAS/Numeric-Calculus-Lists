from sympy import *

def main():
    str_f = input("\nDigite uma função:")
    x = symbols('x')
    f = lambda x: str_f
    print(diff(f(x), x))
    print(diff(f(x), x).subs(x,1))

if __name__ == "__main__":
    main()