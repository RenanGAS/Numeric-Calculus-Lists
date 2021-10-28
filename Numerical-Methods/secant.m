
 % Método da Secante 1.0              
 %
 % Achar uma solução para f(x) = 0 dado um
 % intervalo [A,B]:
 %
 % Entradas:   Intervalo [A,B]; Tolerância TOL;
 %             Número máximo de iterações NO.
 %
 % Saída:      Solução aproximada P ou uma mensagem de erro.

 syms('OK', 'P0', 'P1', 'TOL', 'NO', 'FLAG', 'NAME', 'OUP', 'F0'); 
 syms('I', 'F1', 'P', 'FP','s','x'); 

 % syms é, por definição, uma função para declarar objetos simbólicos, ou seja, variáveis
 % Ao colocarmos 'OK', 'P0', ... e etc, a função syms cria as variáveis Ok, P0, ... e atribui elas a uma variável do tipo Matlab
 % com o mesmo nome: 
 % OK = OK
 % (variavel_matlab) = (variavel_entrada)
                                   
 TRUE = 1;
 FALSE = 0;
 fprintf(1,'Este é o método da secante\n'); 
 fprintf(1,'Insira a função f(x) em termos de  x\n');
 fprintf(1,'Por exemplo, cos(x)-x\n');

 % Nesses usos da função fprintf, temos dois parâmetros: o ID e uma simples mensagem de texto 
 % O ID pode assumir 3 valores: um ID real de um arquivo, o valor 1, e o valor 2.
 % ID = 1 é para que a saída da função, no caso a mensagem, seja pela saída
 % padrão, a tela;
 % Já ID = 2, é usado para sinalizar mensagens de erro. Assim, se o colocássemos, a cor do texto mudaria para vermelho. 

 s = input(' ');

 % Atribui à variável 's', a função digitada pelo usuário
 
 F = inline(s,'x');

 % Atribui à variável 'F' a função atribuída a 's', e determina que ela
 % tem somente uma variável denotada por 'x'.

 % Começo da iteração: "Enquanto OK equivale a FALSE"
 % Modificação: Aplicar identação em trechos de códigos como esse, para
 % entender melhor seu funcionamento. (ctrl + i)

 OK = FALSE;

 while OK == FALSE

     fprintf(1,'Insira as extremidades A < B em linhas separadas\n');

     P0 = input(' ');
     P1 = input(' ');

     % P0 = A
     % P1 = B

     if P0 > P1
         X = P0;
         P0 = P1;
         P1 = X;
     end

     % Para que o código funcione, P0 tem que possuir o menor valor entre A e B.
     % Caso o usuário não passe os valores em ordem crescente:
     % O trecho de código acima inverte as atribuições: 
     % Se P0 > P1 (A > B):
     % P0 = B 
     % P1 = A.

     if P0 == P1
         fprintf(2,'A não pode ser igual a B\n'); % Modificação: colocado o valor 2 no parâmetro ID

     else
         FA = F(P0);
         FB = F(P1);

         if FA*FB > 0
             fprintf(2,'f(A) e f(B) têm o mesmo sinal.\n'); % Modificação: colocado o valor 2 no parâmetro ID

         else
             OK = TRUE;

         end

     end

     % Trecho de código que verifica se A e B são iguais ou não.

     % Caso sejam, imprime uma mensagem de erro, mantém OK = FALSE e
     % recomeça a iteração.

     % Caso não, calcula o valor de F(P0) e F(P1), que são, respectivamente, F(A) ou F(B),
     % dependendo da ordem crescente das entradas;
     
     % Verifica se o produto dos resultados é maior que 0:

     % Caso sejam, imprime uuma mensagem de erro e recomeça a iteração.

     % Caso não, atribui à OK o valor de TRUE, encerrando a estrutura de repetição.

 end

 % Fim da iteração

 % Começo da iteração: "Enquanto OK equivale a FALSE"

 OK = FALSE;

 while OK == FALSE

     fprintf(1,'Digite Tolerância\n');
     TOL = input(' ');

     if TOL <= 0
         fprintf(2,'A tolerância dever ser positiva\n'); % Modificação: colocado o valor 2 no parâmetro ID

     else
         OK = TRUE;
     end
 end

 % Fim da iteração

 % Atribui à 'TOL', a tolerância a ser utilizada no método.

 % Verifica se TOL é menor ou igual a 0:

 % Caso seja, imprime uma mensagem de erro e recomeça a iteração.

 % Caso não, atribui à OK o valor de TRUE, encerrando a iteração.


 % Começo da iteração: "Enquanto OK equivale a FALSE"

 OK = FALSE;

 while OK == FALSE

     fprintf(1,'Insira o número máximo de iterações - número inteiro positivo\n');
     NO = input(' ');

     if NO <= 0
         fprintf(2,'Digite um número inteiro positivo\n'); % Modificação: colocado o valor 2 no parâmetro ID

     else
         OK = TRUE;
     end
 end

 % Fim da iteração

 % Atribui à variável 'NO', o número máximo de iterações que o método
 % executará.

 % Verifica se NO é menor ou igual a 0:

 % Caso seja, imprime uma mensagem de erro e recomeça iteração.
 
 % Caso não, atribui à OK o valor de TRUE, encerrando a iteração.


 % Trecho de código que define o meio pelo qual o usuário visualizará o(s) resultado(s):

 fprintf(1,'Selecione a saída de destino\n');
 fprintf(1,'1. Tela\n');
 fprintf(1,'2. Arquivo de texto\n');
 fprintf(1,'Digite 1 ou 2\n');

 FLAG = input(' ');

 % Atribui à 'FLAG', o valor 1 (para mostrar os resultados na tela) ou
 % 2 (para enviar os resultados para um arquivo)

 if FLAG == 2

     fprintf(1,'Insira o nome do arquivo na forma - drive:\\nome.ext\n');
     fprintf(1,'Por exemplo,   A:\\OUTPUT.DTA\n');
     NAME = input(' ','s');
     OUP = fopen(NAME,'wt');

 else
     OUP = 1;

 end

 % Verifica se FLAG é igual a 2:

 % Caso seja, atribui à 'NAME' o diretório em que o programa deve criar o 
 % arquivo, e o nome.extensão do mesmo, sem 'olhar' essa 'entrada' como
 % uma expressão matemática. Em seguida, atribui à 'OUP', o ID do arquivo
 % criado pela função fopen. (A ausência do segundo parâmetro ('s'), faria
 % com que a 'entrada' passasse por uma verificação sintática) ('wt' faz
 % com que tenhamos a permissão de escrever 'w' no modo texto '-t'. O uso desse modo
 % faz com que seja dado um 'enter' antes de cada atribuição de dados ao arquivo.

 % Caso não, atribui à OUP o valor 1. (pois se FLAG recebe 1, significa que
 % a saída será enviada para tela, sendo necessário que esse seja o valor do ID nos fprintf seguintes).



 % Trecho de código que define o(s) resultado(s) que deseja-se ver   

 fprintf(1,'Escolha um valor de saída\n');
 fprintf(1,'1. Somente a resposta\n');
 fprintf(1,'2. Todas as iterações\n');
 fprintf(1,'Digite 1 ou 2\n');

 FLAG = input(' ');

 % Atribui à FLAG, o valor 1 (para mostrar somente o valor de x em que o critério da parada é satisfeito) ou
 % 2 (para mostrar os valores de x em todas as iterações).

 fprintf(OUP, 'Método da Secante\n');

 % Envia para tela ou o arquivo, a mensagem acima, dependendo do valor de OUP.
 % Podemos dizer que o primeiro parâmetro do fprintf funciona como uma referência da saída. 

 if FLAG == 2
     fprintf(OUP,'%3s%12s%23s\n','K','X_(K+1)','|x_(K+1) - x_(K)|');
     % fprintf(OUP, '%3s%14f%10s\n', '0',  P0  ,  abs(U-P0));
 end

 % Se FLAG for igual a 2, ou seja, deseja-se ver o resultado de todas as iterações,
 % é primeiramente enviado ao ambiente de saída, as identificações dos campos: K, Xk e |Xk - Xk-1|.
 % O campo K é indicado como uma string de 3 bytes,
 % O campo Xk é indicado como uma string de 12 bytes,
 % E o campo do Erro Absoluto, como uma string de 23 bytes.



 % APLICAÇÃO DO MÉTODO DA SECANTE


 % PASSO 1

 % Definir os valores iniciais de: K, f(X_(K)) e f(X_(K-1))

 K = 1;
 F0 = F(P0); 
 F1 = F(P1);

 % P0 = X_(K-1)
 % F0 = f(X_(K-1))
 % P1 = X_(K)
 % F1 = f(X_(K))


 % PASSO 2

 % Começo da iteração: "Equanto K for menor ou igual a NO, e OK for equivalente a TRUE"

 OK = TRUE;

 while K <= NO && OK == TRUE


     % PASSO 3
     
     % Calcular X_(K+1):

     P = P1-F1*(P1-P0)/(F1-F0);

     % P = X_(K+1)


     % PASSO 4

     % Usar uma variável ( FP ) para receber o valor de f(X_(K+1)) ( F(P) ), pois se o
     % critério da parada não for satisfeito, na próxima iteração, X_(K+1) será X_(K),
     % e analogamente, f(X_(K+1)) será f(X_(K)).

     FP = F(P);

     if FLAG == 2
         fprintf(OUP, '%3d \t %3.10f  \t %3.10f\n', K, P, abs(P-P1));
     end

     % Se FLAG for igual a 2, ou seja, deseja-se mostrar os valores que estão associados a 
     % cada iteração, executa-se um fprintf mostrando esses variáveis para o atual valor de K. 


     % PASSO 5

     % Verificar se o Erro Absoluto é menor que a tolerância:

     % Caso for, é enviado o valor da raiz da equação, o número de
     % iterações executadas, e atribuímos a OK o valor de FALSE, 
     % encerrando a iteração. 

     % Caso não, prosseguimos incrementando o valor de K em uma unidade, 
     % e atualizamos os valores de P0, P1, F0 e F1, para a execução da 
     % próxima iteração.

     if abs(P-P1) < TOL

         fprintf(OUP,'\nSolução aproximada é %.10f\n',P);
         fprintf(OUP,'Número de iterações = %d\n',K);

         OK = FALSE;

     else

         K = K+1;

         P0 = P1;
         F0 = F1;
         P1 = P;
         F1 = FP;
     end
 end

 % Fim da iteração

 if OUP ~= 1
     fclose(OUP);
     fprintf(1,'Arquivo %s criado com sucesso!\n',NAME);
 end

 % Se o ID 'OUP' for diferente de 1, significa que a variável possui o ID
 % de um arquivo criado no drive do Matlab do usuário, sendo preciso
 % encerrar a edição do mesmo, e enviar uma mensagem transmitindo que os
 % resultados foram enviados com sucesso para o documento.