def menu_nãocliente():

    squidBank = int(input("  Seja Bem vindo(a) ao Squid Bank, você selecionou a opção: NÃO SOU CLIENTE! "
                        "\n  1 - Para informação sobre Solução De Dívidas."
                        "\n  2 - Para informação sobre Cartões."
                        "\n  3 - Para informação sobre Consórcio."
                        "\n  4 - Para informação sobre Empréstimos."
                        "\n  Digite a opção desejada: "))

    empréstimo = ("""Você selecionou Empréstimo, explicaremos em mais detalhes sobre: 
    É o crédito perfeito para você usar quando e como quiser: em uma viagem, 
    na realização de um sonho ou até mesmo na resolução dos imprevistos do dia a dia. 
    Se você não é cliente do Squid Bank: Consulte no aplicativo nossas condições de contratação.""")

    cartões = ("""Você selecionou Cartões, explicaremos em mais detalhes sobre: 
    Para solicitar seu cartão de crédito é só baixar o App do Squid Bank e seguir os passos a seguir.

    1º passo: baixe e acesse o App SB. Selecione a opção "Produtos para mim".
    2º passo: informe o seu CPF e depois escolha o item "Cartão de Crédito".
    3º passo: em seguida, informe os número do seu telefone para liberar o aparelho e siga as orientações e 
    solicitações do aplicativo. Tenha em mãos os seguintes itens para dar continuidade ao seu pedido: CNH ou 
    documento de identidade (RG) válido; câmera para tirar uma selfie para verificação facial e também fotografar 
    os seus documentos; comprovante de residência emitido a menos de 90 dias; comprovante de renda emitido nos 
    últimos 3 meses, caso seja estudante universitário, tenha em mãos um comprovante de escolaridade.
    4º passo: aguarde a análise da sua proposta, o SB enviará uma resposta para você por SMS ou pelo WhatsApp 
    em até 3 dias úteis.

    Agora selecione a opção do cartão desejado!""")

    consórcios = ("""Você selecionou Consórcio, explicaremos em mais detalhes sobre:
    Realize os seus sonhos de forma planejada e sem juros. O Consórcio do Squid Bank é uma solução segura 
    feita para você que tem planos de adquirir uma casa própria, comprar um carro, uma moto, um smartphone, 
    um tablet, um videogame e muito mais.

    De forma econômica e parcelada, você escolhe o prazo e o valor da parcela que cabem no seu bolso, com o 
    poder da compra à vista.

    Faça uma simulação em nosso aplicativo, escolha a melhor opção de acordo com os seus objetivos e conte 
    com as condições exclusivas do Consórcio do Squid Bank.""")

    solução_de_dívidas = ("""Para renegociar sua dívida entre em contato com o nosso SAC de atendimento e 
    peça uma simulação pelo valor do bem ou da parcela. Gostou da simulação? Ligue pelo telefone
    0800-990-8888 e contrate o nosso serviço.""")

    retornar_menu_principal = squidBank

    if (squidBank == 1):
        print(solução_de_dívidas)
    elif (squidBank == 2):
        print(cartões)
        if (squidBank == 2):
            escolha = int(input(" Digite 1 para saber sobre o nosso cartão ouro; "
                                "\n 1 - Para saber sobre o nosso cartão ourocard Pré-pago;  "
                                "\n 2 - Para saber sobre o nosso cartão Gold; "
                                "\n 3 - Para saber sobre o nosso cartão Platinum; "
                                "\n 4 - Para saber sobre o nosso cartão Black; "
                                "\n Escolha qual das opções que você deseja informação: "))

            if escolha == 1:
                ouro = ("""            CARACTERÍSTICAS - O seu cartão internacional cheio de vantagens.
                RENDA MENSAL - Análise de crédito no Banco.
                PRIMEIRA ANUIDADE - Sem anuidade.""")
                escolha == ouro
                print(ouro)

            if escolha == 2:
                ourocad_Pré_pago = ("""            CARACTERÍSTICAS - Ideal para mesadas ou compras do dia a dia. 
                PRIMEIRA ANUIDADE - Sem comprovação de renda.
                RENDA MENSAL - Sem anuidade.""")
                escolha = ourocad_Pré_pago
                print(ourocad_Pré_pago)

            if escolha == 3:
                gold = ("""            CARACTERÍSTICAS - Conte com um cartão com benefícios no Brasil e no exterior, 
                pontue relaciona e tenha acesso a outras vantagens.
                RENDA MENSAL - Análise de crédito no Banco.
                PRIMEIRA ANUIDADE - Titular: 12x de R$ 34,00 (R$ 408,00). 
                Adicional: 50% do valor da anuidade do cartão do titular.""")
                escolha = gold
                print(gold)

            if escolha == 4:
                platinum = ("""            CARACTERÍSTICAS - Pontuação diferenciada e benefícios exclusivos em viagens.
                RENDA MENSAL - Análise de crédito no Banco.
                PRIMEIRA ANUIDADE - Titular: 12x de 47,25 (R$ 567,00). 
                Adicional: 50% do valor da anuidade do cartão do titular.""")
                escolha = platinum
                print(platinum)

            if escolha == 5:
                black = ("""            CARACTERÍSTICAS - Pontuação especial, benefícios e vantagens exclusivas 
                em viagens e seguros.
                RENDA MENSAL - Análise de crédito no Banco.
                PRIMEIRA ANUIDADE - Titular: 12x de R$ 91,50 (R$ 1.098,00). 
                Adicional: 50% do valor da anuidade do cartão do titular.""")
                escolha = black
                print(black)

    elif (squidBank == 3):
        print(consórcios)
    elif (squidBank == 4):
        print(empréstimo)
    else:
        squidBank != (1, 2, 3, 4)
        print(f"Você selecionou um opção que não existe.")
