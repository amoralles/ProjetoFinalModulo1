def mesmoCartao (cartaoDesejado,cartaoAtual):
    if cartaoDesejado == cartaoAtual:
        return print((f'O seu cartão atual já é da categoria {cartaoAtual}'))

def novoCartao (cartaoDesejado,renda,score):
    if cartaoDesejado == 'Platinum' and renda >= 5000 and score >= 750:
        return print(('O seu perfil é eligível para esse cartão. Em até 10 minutos o cartão estará disponível no app para solicitar.'))
    elif cartaoDesejado == 'Black' and renda >= 10000 and score >= 850:
        return print(('O seu perfil é eligível para esse cartão. Em até 10 minutos o cartão estará disponível no app para solicitar.'))
    elif cartaoDesejado == 'VIP' and renda >= 20000 and score >= 950:
        return print(('O seu perfil é eligível para esse cartão. Em até 10 minutos o cartão estará disponível no app para solicitar.'))
    else: 
        return print(('Infelizmente, você não se enquarda no perfil necessário.'))


def InformativoBeneficiosGold(cartaoAtual):
    if cartaoAtual == 'Gold':
        return(print( ("""
        Os benefícios do seu cartão são:
        1 - Seguro Proteção de Preço 
        2 - Garantia Estendida Original 
        3 - Seguro Compra Protejida
        4 - Mastercard Surpreenda
        5 - Isenção de anuidade 
        """)))

def InformativoBeneficiosPlatinum(cartaoAtual):
    if cartaoAtual == 'Platinum':
        return print( (""" 
        Os benefícios do seu cartão são
        1 - Concierge de viagem 24h por dia 
        2 - Seguro Automóvel
        3 - Seguro Médico
        4 - Cashback de 0,5 porcento em todas as compras
        5 - Isenção de anuidade gastando R$ 2.500,00 por mês
        6 - Isenção de rolha em milhares de restaurantes
        """))

def InformativoBeneficiosBlack(cartaoAtual):
    if cartaoAtual == 'Black':
        return print(("""
        Os benefícios do seu cartão são:
        1 -Todos os benefícios do cartão Gold e Platinum:
        2 - Wifi gratuito em todos os aeroportos brasileiros 
        3 - Acesso ilimitado a SalasVip através do LoungeKey
        4 - Proteção de Bagagem')
        5 - Cashback de 1 porcento em todas as compras
        6 - Isenção de anuidade gastando R$ 7.000,00 por mês
        7 - Isenção de rolha em milhares de restaurantes
        """))

def InformativoBeneficiosVIP(cartaoAtual):
    if cartaoAtual == 'VIP':
        return print(("""
        Os benefícios do seu cartão são:
        1- Todos os benefícios do cartão Gold, Platinum e Black
        2 - Acesso ilimitado a SalasVip através do LoungeKey com 3 acompanhantes
        3 - Cashback de 1.5 porcento em todas as compras
        4 - Isenção de anuidade gastando R$ 15.000,00 por mês
        5 - Assoria de Investimentos gratuita
        6 - Acesso as melhores Taxas de Câmbio do mercado
        7 - Isenção de IOF em compras internacionais
        """))


def venc (dataFechamento):
    if dataFechamento == 5:
        return print(('A data de fechamento da sua fatura é todo dia 15 de cada mês.'))
    elif dataFechamento == 8:
        return print(('A data de fechamento da sua fatura é todo dia 18 de cada mês.'))
    elif dataFechamento == 10:
        return print(('A data de fechamento da sua fatura é todo dia 18 de cada mês.'))
    elif dataFechamento == 20:
        return print(('A data de fechamento da sua fatura é todo dia 27 de cada mês.'))
    elif dataFechamento == 25:
        return print(('A data de fechamento da sua fatura é todo dia 30 de cada mês.'))                    
    

def melhorCompra (dataFechamento):
    if dataFechamento == 5:
        return print(('A melhor data de compra é todo dia 6 de cada mês.'))
    elif dataFechamento == 8:
        return print(('A melhor data de compra é todo dia 9 de cada mês.'))
    elif dataFechamento == 10:
        return print(('A melhor data de compra é todo dia 11 de cada mês.'))
    elif dataFechamento == 20:
        return print(('A melhor data de compra é todo dia 21 de cada mês.'))
    elif dataFechamento == 25:
        return print(('A melhor data de compra é todo dia 26 de cada mês.'))
