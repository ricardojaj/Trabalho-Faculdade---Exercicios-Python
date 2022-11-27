#Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção
#de app de vendas para uma determinada empresa X que vende em atacado. Para calcular o
#valor total que o deve-se levar em consideração o custo de embalagem conforme a tabela
#abaixo


#Elabore um programa em Python que:

#1. Entre com o valor unitário do produto (Lembrar que número decimal é feito
#com PONTO e não VÍRGULA);
#2. Entre com a quantidade desse produto;
#3. O programa deve retornar o valor total sem o custo de embalagem para frete;
#4. O programa deve retornar o valor total após o custo de embalagem para frete;
#5. Deve-se utilizar estruturas if, elif e else (EXIGÊNCIA 1 de 1);
#6. Colocar um exemplo de SAIDA DE CONSOLE de compra de mais de 1000 und.

print('Bem vindo a loja do Ricardo Jesus dos Anjos Junior');
#variaveis de entrada
valorProduto = float(input('Digite o valor do Produto: '));
quantidade = int(input('Digite a quantidade: '));

#variaveis de saida
valorSemFrete = quantidade * valorProduto;
valorComFrete = 0;
taxaFrete = 0;


#estrutura condicional para definir o valor do frete de acordo com a quantidade
if quantidade > 0 and quantidade < 11:
    taxaFrete = 30;
    valorComFrete = (quantidade *valorProduto) + taxaFrete;

elif quantidade >= 11 and quantidade < 101:
    taxaFrete = 60;
    valorComFrete = (quantidade * valorProduto) + taxaFrete;

elif quantidade >= 101 and quantidade < 1001:
    taxaFrete = 120;
    valorComFrete = (quantidade * valorProduto) + taxaFrete;
else:
    taxaFrete = 240;
    valorComFrete = (quantidade * valorProduto) + taxaFrete;

#saida das informações na tela
print('O valor sem frete foi: %.2f' % valorSemFrete)
print('O valor com frete foi: %.2f' % valorComFrete, '(frete de R$ %.2f)' % taxaFrete);
