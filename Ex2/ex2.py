"""""
print("Código" + "| " + "Descrição" + "            | "  + "Tamanho P(500 ml)" + "| "  +
      "Tamanho M(1000 ml)" + "| " +  "Tamanho G(2000 ml)")
print("TR" + "    | " + "Sabores tradicionais " + "|  R$ 6,00         |" +"  R$ 10,00         " + "| " +  "R$ 18,00")
print("ES" + "    | " + "Sabores especiais    " + "|  R$ 7,00         |" +"  R$ 12,00         " + "| " +  "R$ 21,00")
print("PR" + "    | " + "Sabores premium    " + "  |  R$ 8,00         |" +"  R$ 14,00         " + "| " +  "R$ 24,00")


Elabore um programa em Python que:
1. Entre com o tamanho do pote de sorvete desejado;
2. Entre com o código do sorvete desejado;
3. Pergunte se o cliente quer pedir mais alguma coisa (se sim repetir a partir do
item 1. Caso contrário ir para próximo passo);
4. Encerre a conta do cliente com o valor total;
5. Deve-se utilizar estruturas if, elif e else (EXIGÊNCIA 1 de 3);
6. Se a pessoa digitar um TAMANHO de sorvete e/ou código diferente dos da
tabela printar na tela: ‘TAMANHO ou CÓDIGO inválido(s)’ e voltar para o menu
(EXIGÊNCIA 2 de 3);
7. Deve-se utilizar while, break, continue (EXIGÊNCIA 3 de 3);
o (DICA: utilizar o continue dentro else que verifica a opção inválida)
o (DICA: utilizar o break dentro if que verifica a opção sair)
8. Colocar um exemplo de SAIDA DE CONSOLE com 3 (três) sorvetes
9. Colocar um exemplo de SAIDA DE CONSOLE com erro tamanho
10 -  Colocar um exemplo de SAIDA DE CONSOLE com erro código
"""


totalCompra = 0;
resposta = 'S';

#estrutura de repeticao - só continua o processo se a resposta do usuario for = 'S'(SIM)
while(resposta == 'S'):
    tamanhoSorvete = input('Digite o tamanho do sorvete: (P/M/G)');
    codigoSorvete = input('Digite o codigo do sorvete: (TR/ES/PR)');
    if tamanhoSorvete == 'P' and codigoSorvete =='TR':
            totalCompra = totalCompra + 6;
            print('Voce pediu um sorvete tradicional pequeno!')
    elif tamanhoSorvete == 'M' and codigoSorvete == 'TR':
            totalCompra = totalCompra + 10;
            print('Voce pediu um sorvete tradicional médio!')
    elif tamanhoSorvete == 'G' and codigoSorvete == 'TR':
            totalCompra = totalCompra + 18;
            print('Voce pediu um sorvete tradicional grande!')
    elif tamanhoSorvete == 'P' and codigoSorvete == 'ES':
            totalCompra = totalCompra + 7;
            print('Voce pediu um sorvete especial pequeno!')
    elif tamanhoSorvete == 'M' and codigoSorvete == 'ES':
            totalCompra = totalCompra + 12;
            print('Voce pediu um sorvete especial médio!')
    elif tamanhoSorvete == 'G' and codigoSorvete == 'ES':
            totalCompra = totalCompra + 21;
            print('Voce pediu um sorvete especial grande!')
    elif tamanhoSorvete == 'P' and codigoSorvete == 'PR':
            totalCompra = totalCompra + 8;
            print('Voce pediu um sorvete premium pequeno!')
    elif tamanhoSorvete == 'M' and codigoSorvete == 'PR':
            totalCompra = totalCompra + 14;
            print('Voce pediu um sorvete premium médio!')
    elif tamanhoSorvete == 'G' and codigoSorvete == 'PR':
            totalCompra = totalCompra + 24;
            print('Voce pediu um sorvete premium grande!')
    else:
            print('TAMANHO ou CÓDIGO inválido(s)');

    resposta = str(input('Deseja continuar: (S/N) '))

print('O total a ser pago é: %.2f' %totalCompra);
