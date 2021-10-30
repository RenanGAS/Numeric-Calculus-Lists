disp('Exercício 1');
   No MatLab, crie um arquivo live script e faça o que se pede:
disp('a)');
   Plote o gráfico de usando o arquivo "graphic plot":
syms('OK', 'P0', 'P1', 'TOL', 'NO', 'FLAG', 'NAME', 'OUP', 'F0');
syms('I', 'F1', 'P', 'FP','s','x');
fprintf(1,'Insira a função f(x) em termos de  x\n');
fprintf(1,'Por exemplo, cos(x)-x\n');
s = input(' ');
F = inline(s,'x');

fprintf(1,'Insira as extremidades a < b em linhas separadas\n');
P0 = input(' ');
P1 = input(' ');

if P0 > P1
    X = P0;
    P0 = P1;
    P1 = X;
end

x1=P0:.1:P1;
plot(x1,F(x1),'LineWidth', 1.5);
title('Gráfico de f(x)');
grid on


disp('b)');
   Plote o gráfico de  dado no item (a) juntamente com a função :
x = linspace(-pi,pi);
y1 = sin(x) + x.^2 + 1;
plot(x,y1);

hold on
y2 = x.^3 + 8*x.^2 -4*x -2;
plot(x,y2);
title('Gráfico de f(x) e g(x)');
xline(0);
yline(0);
legend('f(x) = sin(x) + x^2 + 1', 'g(x) = x^3 + 8x^2 -4x -2');
hold off


disp('Exercício 2');
   A precisão de máquina é definida como sendo o menor número positivo em aritmética de ponto flutuante  
   tal que: .
   Este número depende totalmente do sistema de representação da máquina: base numérica, total de dígitos na mantissa, forma como são realizadas as operações e do compilador utilizado. 
   É importante conhecermos a precisão de máquina porque em vários algoritmos precisamos fornecer como dado de entrada um valor positivo, próximo de zero para ser usado em testes de 
   comparação com zero. 
   Dito de outro modo, a precisão da máquina representa a exatidão relativa da aritmética do computador, e a sua existência  é uma consequência direta da precisão finita da aritmética de ponto flutuante.


disp('a)');
   O algoritmo:
t = 1;

while t + 1 > 1
    t = t / 2;
end

epsValue = t * 2;
   calcula a precisão de qualquer sistema operacional.
   Execute o código e verifique o valor da precisão de máquina.
epsilonDisp = ['epsilon =' ' ' num2str(epsValue)];

disp(epsilonDisp);
   O MatLab retorna a precisão de máquina através do comando eps. Verifique isso:
disp(eps);



disp('b)');
   Vimos no padrão IEEE 754 que um número na representação binária é dado por

   Calcule o valor de  O que este valor significa em relação à            
   representação dada em (1) ?
t = -log2(epsValue);

r1 = ['R: O valor de t (' num2str(t) ') representa o número de' newline 'bits usado para representar a mantissa no ' newline 'padrão IEEE 754.'];
disp(r1);



disp('c)');
   Sabemos que zero é o elemento neutro da adição .
   Para tanto, faça dois cálculos:

disp('(i) a + eps');

a = 1234;

sum1 = a + epsValue;

r2 = [num2str(a) ' + ' num2str(epsValue) ' = ' num2str(sum1)];

disp(r2);


disp('(ii) 2^t + a , donde t foi encontrado no item (b)');

sum2 = 2.^-t + a;

r3 = [num2str(2.^-t) ' + ' num2str(a) ' = ' num2str(sum2)];

disp(r3);
   Do exposto, o leitor está apto para responder a seguinte pergunta: “A máquina acha que ?”
r4 = ['R: Considerando os cálculos feitos, podemos' newline 'afirmar que a máquina considera o valor' newline num2str(eps) ' igual a 0.'];

disp(r4);



disp('d)');
   O maior número que representável pela máquina é dado pelo comando realmax.  Use este comando 
   para encontrar o maior número representável pela máquina.
disp(realmax);
   Para se certificar disso, não deve haver nenhum número na máquina que supere-o. Isso pode verificado pelos códigos
verif1 = 'true';

if realmax + 1 > realmax
    verif1 = 'false';
end

r5 = ['A constante realmax é o maior número representável' newline 'pela máquina?' newline newline 'R: ' verif1];

disp(r5);


disp('e)');
   O menor número representável é dado pelo comando realmin. Use este comando para encontrar o menor número representável pela máquina:
disp(realmin);

    Nota:
    Se o MATLAB devolver 0 em uma expressão lógica, a expressão é falsa. Se devolver 1, a expressão é verdadeira. 
    Outras combinações são reservadas para os valores especiais NaN (Not a Number ) que representa resultados aritméticos indefinidos e Inf que representa overflow. 
    O que o MATLAB devolve ao você realizar as seguintes operações aritméticas:
    , , 2*realmax, -2*realmax, eps/2*realmin
disp(' ');
disp("Nota:");

1/0
0/0
2*realmax
-2*realmax
(eps/2)*realmin

