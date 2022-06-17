import funcoes

# a função menuCliente(), de acordo com o valor atribuido em escolhaCliente pela função menu1(), abre um novo menu de opções para cada valor.

def menuCliente(escolhaCliente):
    if escolhaCliente == 1:
        escolhaPix = funcoes.menu1_pix()
        #print(funcoes.concluir(escolhaCliente)) #pergunta se a dúvida foi resolvida ou não. Se sim, encerra. S não, volta o menu. 

    # Se o valor for escolhaCliente == 2 abrirá o menu sobre Conta.
    elif escolhaCliente == 2:
        escolhaConta = funcoes.menu1_conta()

    # Se o valor for escolhaCliente == 3 abrirá o menu sobre Carteiras Digitais.
    elif escolhaCliente == 3:
        escolhaCarteira = funcoes.menu1_carteira()
      
    # Se o valor for escolhaCliente == 4 abrirá o menu sobre Débito automático.
    elif escolhaCliente == 4:
        escolhaDebito = funcoes.menu1_debito()

    # Se o valor for escolhaCliente == 5 retornará ao menu anterior.
    elif escolhaCliente == 5:
        return(funcoes.inicio2())

    return


    

        
