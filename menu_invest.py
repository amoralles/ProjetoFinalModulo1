########## SQUID INVEST+ #############
#
#               Legenda:
#
#           c -  valor inicial de investimento
#           a -  valor do aporte (depósitos mensais)
#           t -  tempo (anos)
#           i -  taxa de juros ao ano
#           m -  montante (total)
#           
#       _____________________________________________


# Introdução #
def menu_invest():

    # Simular ou Investir #

    escolha1= int(input("""################## SquidInvest+ #################
    Bem-vindo(a) ao nosso canal de investimentos!
    1 - Simular investimento
    2 - Quero investir agora!
    3 - Saiba Mais
    Como podemos te ajudar hoje?
    Digite a opção desejada: """))

    #Simulação#


    if escolha1 == 1:

        escolha=int(input(""" Qual das opções de investimento você deseja simular?
        1- Tesouro Prefixado
        2- Tesouro SELIC  
        3- Tesouro IPCA+ 
        Informe a opção desejada: """))

        # Tesouro Prefixado #

        if escolha == 1:
            c=float(input("Digite o valor inicial a ser investido: "))
            a=float(input("Digite o valor que você depositaria por mês: "))
            t=float(input("Por quanto tempo você deixaria seu dinheiro investido (ano)?  "))
            from funcoes_si import prefix
            prefix(c,t,a)
            return(f"Em {t} anos você teria R${prefix(c,t,a)}")

        # Tesouro SELIC #

        elif escolha == 2:        
            c=float(input("Digite o valor inicial a ser investido: "))
            a=float(input("Digite o valor que você depositaria por mês: "))
            t=float(input("Por quanto tempo você deixaria seu dinheiro investido (ano)?  "))
            from funcoes_si import selic
            selic(c,t,a)
            return(f"Em {t} anos você teria R${selic(c,t,a)}")

        # Tesouro IPCA+ #

        elif escolha == 3:
            c=float(input("Digite o valor inicial a ser investido: "))
            a=float(input("Digite o valor que você depositaria por mês: "))
            t=float(input("Por quanto tempo você deixaria seu dinheiro investido (ano)?  "))
            from funcoes_si import ipcam
            ipcam(c,t,a)
            return(f"Em {t} anos você teria R${ipcam(c,t,a)}")
        else:
            return (f"Opção inválida, tente novamente")

    # Quero Investir! #


    if escolha1 == 2:

        escolha = int(input("""Onde você deseja investir?
        1- Tesouro Prefixado
        2- Tesouro SELIC 
        3- Tesouro IPCA+        
        Digite a opção desejada: """))

        # Quero investir em Tesouro Prefixado! #

        if escolha == 1:
            c=float(input("Digite o valor do investimento: "))
            a=float(input("Digite o valor do aporte: "))
            t=float(input("Por quanto tempo você deseja deixar o seu dinheiro investido(ano)?  "))
            from funcoes_si import prefix
            return(prefix(c,t,a))

        # Quero investir em Tesouro Selic! #

        elif escolha == 2:        
            c=float(input("Digite o valor do investimento: "))
            a=float(input("Digite o valor do aporte: "))
            t=float(input("Por quanto tempo você deseja deixar o seu dinheiro investido(ano)?  "))
            from funcoes_si import selic
            selic(c,t,a)
            return(f"Em {t} anos você teria R${selic(c,t,a)}")

        # Quero investir em Tesouro IPCA+! #

        elif escolha == 3:
            c=float(input("Digite o valor do investimento: "))
            a=float(input("Digite o valor do aporte: "))
            t=float(input("Por quanto tempo você deseja deixar o seu dinheiro investido(ano)?  "))
            from funcoes_si import ipcam
            ipcam(c,t,a)
            return(f"Em {t} anos você teria R${ipcam(c,t,a)}")

        # Opção Inválida :( #

        else:
            
            return("Opção inválida. Por favor tente novamente")
        
    if escolha1 == 3:
        
        escolha = input(""" 
        Aqui na SquidInvest+ te ajudamos a investir da melhor forma no Tesouro Direto! )
        Tesouro Direto é um programa da Secretaria do Tesouro Nacional do Brasil lançado em 7 de janeiro de 2002 em parceria com a B3 com o objetivo de democratizar a compra e venda de títulos públicos federais para pessoas físicas de forma 100% online. 

        1 - Tesouro Prefixado
        2 - Tesouro SELIC 
        3 - Tesouro IPCA+
        Digite a opção desejada para obter mais informações:  """)

        if escolha == 1:
                print(" Tesouro Prefixado: O Tesouro Direto prefixado é um título de Renda Fixa com taxas de juros determinadas no momento da contratação. Ou seja, quando você empresta o seu dinheiro ao governo e já sabe de cara exatamente o quanto vai receber ao final do prazo do título")
        elif escolha == 2:
                print("Tesouro SELIC: O Tesouro Selic é um investimento de renda fixa. Ele costuma ser bastante recomendado, principalmente aos que procuram uma alternativa à poupança. Esse ativo tende a oferecer rentabilidade mais atrativa do que a caderneta. Além disso, ele ainda pode ser adaptado para objetivos sob qualquer prazo.")
        elif escolha == 3:
                print("Tesouro IPCA+ : O Tesouro Direto IPCA+ é um título público do governo federal. Parte da sua taxa de rendimento acompanha a inflação, enquanto a outra parcela é composta por um valor fixo. Ele tem investimento inicial de pouco mais de R$ 30 e diferentes datas de vencimento, que podem se encaixar em vários objetivos")
        else:
                print("Opção Inválida. Tente novamente!")
       
   

       





