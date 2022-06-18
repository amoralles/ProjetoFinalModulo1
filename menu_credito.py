import funcoes_cd

def menu_credito():
    print ('Sobre qual tema de cartão de credito deseja falar?')
    print ('1 - Desejo saber mais sobre os benefícios do meu cartão atual')
    print ('2 - Desejo um novo cartão!')
    print ('3 - Desejo obter mais informações sobre a minha fatura')
    print ('4 - Desejo receber a minha fatura por e-mail')

    selecao = int(input("Escolha uma opção entre 1 e 4: "))

    if selecao == 1:
        cartaoAtual = input('Informe a categoria do seu cartão: ')
        beneficiosGold = funcoes_cd.InformativoBeneficiosGold(cartaoAtual)
        beneficiosBlack = funcoes_cd.InformativoBeneficiosBlack(cartaoAtual)
        beneficiosPlatinum = funcoes_cd.InformativoBeneficiosPlatinum(cartaoAtual)
        beneficiosVIP = funcoes_cd.InformativoBeneficiosVIP(cartaoAtual)

    elif selecao == 2:
        cartaoAtual = input('Informe o seu cartão Atual: ')
        cartaoDesejado = input('Qual cartão deseja obter? ')
        desejoCartao = funcoes_cd.mesmoCartao (cartaoDesejado,cartaoAtual)
        renda = float(input ('Informe a sua renda: '))
        score = float(input('Informe o seu score Serasa: '))
        desejoCartao = funcoes_cd.novoCartao(cartaoDesejado, renda,score)

    elif selecao == 3:
        dataFechamento = float(input('Informe a data de fechamento da sua fatura: '))
        vencimento = funcoes_cd.venc(dataFechamento)
        melhorCompra = funcoes_cd.melhorCompra(dataFechamento)

    elif selecao == 4:
        email = input('Informe o seu e-mail: ')
        return('Fatura enviada para o e-mail!')
    else: 
        return('Opção Inválida. Por favor, tente novamente.')
