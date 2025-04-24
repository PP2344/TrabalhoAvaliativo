# TrabalhoAvaliativo
Descrição do programa:

Ao executar o ficheiro irá aparecer um menu com opções numeradas de 0 a 5, de seguida surgirá um prompt para selecionar uma das opções. O programa não aceitará quaisquer outras opções senão aquelas listadas.

As opções são:

-Visualizar produtos, onde é possível ver os produtos existentes;

-Adicionar produto ao carrinho, onde será mostrado a lista dos produtos e um input para selecionar um deles e a quantidade desejada;

-Quantidade existente e valor do carrinho, mostra se o carrinho possui ou não itens e o valor total dos itens do carrinho;

-Adicionar Saldo, pede um input sobre uma quantia desejada para adicionar ao saldo;

-Pagar, finaliza a compra dos itens do carrinho, reduz o saldo, zera o total da compra e limpa o carrinho;

-Sair, fecha o programa.

Erros personalizados criados:

Número inválido - NumeroInvalidoError, é executado quando o input não corresponde a número inteiro e não pertencente ao intervalo numérico especificado caso exista;

Saldo insuficiente para realizar a compra - SaldoInsuficienteError, é executado na opção de pagar quando o saldo existente é inferior ao valor total do carrinho;

Carrinho vazio ao realizar a compra - CarrinhoVazioError, é executado quando é selecionada a opção de pagar tendo o carrinho vazio;
