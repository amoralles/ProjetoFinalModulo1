import funcoes_cl, menu_cliente, menu_credito, menu_invest
# A função inicial, que pergunta pela primeira vez qual opção o cliente deseja:
def inicio1():
    primeiraEscolha = int(input("""Seja Bem-Vindo(a) ao  menu de auto-atendimendo do Banco Squid! 
    Digite 1 se você já é cliente.
    Digite 2 se quer falar sobre cartão de crédito.
    Digite 3 se quer saber mais sobre investimentos.
    Digite 4 se quer saber mais sobre impréstimos.
    Digite 5 se ainda não é cliente do Banco Squid. 
    Digite 6 para sair.
    """))
    return primeiraEscolha

# Atribui um valor a variavel SquidBank ao solicitar qual opção ao usuário
primeiraEscolha = inicio1()

# A função 'começando' seleciona um dos menus iniciais (desenvolvidos por cada integrante do grupo individualmente) de acordo com o valor atribuído a 'squidBank' pela função 'inicio()' 

def começando(primeiraEscolha):
    # Se o usuário escolheu 1 em inicio(), uma nova variável chama a função 'menu1()', para tirar duvidas de quem já é cliente.
    if primeiraEscolha == 1:
        escolhaCliente = (funcoes_cl.menu1())
        # um valor foi atribuído  a escolhaCliente, de acordo com qual valor o usuário digitou para menu1()
        # esse valor será utilizado pela função menuCliente() para escolher uma das 4 opções de informações para clientes.
        menu_cliente.menuCliente(escolhaCliente)
        # a função concluir() pede ao usuário se ele está satisfeito com o atendimento ou quer voltar do início. Ao voltar pro início ele atribui um novo valor a squidBank
        primeiraEscolha = funcoes_cl.concluir()
        # o return solicita que a função começando comece de novo, agora como novo valor de squidBank.
        return começando(primeiraEscolha)

    if primeiraEscolha == 2:
        escolhaCliente = menu_credito.menu_credito()
        primeiraEscolha = funcoes_cl.concluir()
        return começando(primeiraEscolha)

    if primeiraEscolha == 3:
        escolhaCliente = (menu_invest.menu_invest())
        primeiraEscolha = funcoes_cl.concluir()
        return começando(primeiraEscolha)    
    
    if primeiraEscolha == 4:
        #chamar módulos e funções para menu4
        primeiraEscolha = funcoes_cl.concluir()
        return começando(primeiraEscolha)
    
    if primeiraEscolha == 5:
                #chamar módulos e funções para menu4
        primeiraEscolha = funcoes_cl.concluir()
        return começando(primeiraEscolha)
    
    if primeiraEscolha == 6:
        print("Até mais!")



começando(primeiraEscolha)

