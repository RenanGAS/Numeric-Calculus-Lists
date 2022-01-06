# Método da Bissecante

### Objetivo

Calcular uma raiz de uma função (Determinar um valor para χ tal que f(χ) = 0).

### Visão Geral

Encontraremos um intervalo [α, β] que contenha uma e somente uma raiz. Em seguida, definiremos uma raiz inicial "χ0" pertencente ao intervalo, e a refinaremos através de iterações até obtermos uma raiz que satisfaça o Critério de Parada desejado.

### Observações

* Teorema: Se uma função contínua f(χ) assume valores de sinais opostos nos pontos extremos do intervalo [α, b], isto é, f(α)*f(b) < 0 , então, o intervalo conterá, no mínimo, uma raiz da equação. Em outras palavras, haverá, no mínimo, um número "ξ" ∈ (α, β), tal que f(ξ) = 0;

* Propriedade: A raiz "ξ" será definida e única se f'(χ) existir e preservar o sinal dentro do intervalo (α, β), isto é, se f'(χ) > 0 ou f'(χ) < 0 , se "χ" ∈ (α, β).


