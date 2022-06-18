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
apelido="Ally"
print(f"######################## SquidInvest+ ########################")
print(f"Bem-vindo ao nosso canal de investimentos, {apelido}!")
print(f"Como podemos te ajudar hoje?")

# Simular ou Investir #
print(f"1 - Simular investimento | 2 - Quero investir agora! ")
escolha1= int(input("Digite a opção desejada: "))

#Simulação#

if escolha1 == 1:
    print("Qual das opções de investimento você deseja simular?")
    print("1- Tesouro Prefixado  | 2- Tesouro SELIC  | 3- Tesouro IPCA+ ")
    escolha=int(input("Informe a opção desejada: "))

    # Quero simular o investimento em Tesouro Prefixado! #

    if escolha == 1:
        c=float(input("Digite o valor inicial a ser investido: "))
        a=float(input("Digite o valor que você depositaria por mês: "))
        t=float(input("Por quanto tempo você deixaria seu dinheiro investido (ano)?  "))
        def prefix(c,t,a):
          i=12.48
          if a==0:
            m=c*((1+(i/100))**t)
            return m-0.40*t
          else:
            m=c+(a*t)*((1+(i/100)**t))
            return m-0.40*t
        prefix(c,t,a)
        print(f"Em {t} você teria {prefix(c,t,a)}")

    # Quero simular o investimento em Tesouro Selic! #

    elif escolha == 2:        
        c=float(input("Digite o valor inicial a ser investido: "))
        a=float(input("Digite o valor que você depositaria por mês: "))
        t=float(input("Por quanto tempo você deixaria seu dinheiro investido (ano)?  "))
        def selic(c,t,a):
          i=12.75
          if a==0:
            m=c*((1+(i))**t)
            return m-0.40*t
          else:
            m=c+(a*t)*((1+i)**t)
            return m-0.40*t
        selic(c,t,a)
        print(f"Em {t} você teria {selic(c,t,a)}")

    # Quero simular o investimento em Tesouro IPCA+! #

    elif escolha == 3:
        c=float(input("Digite o valor inicial a ser investido: "))
        a=float(input("Digite o valor que você depositaria por mês: "))
        t=float(input("Por quanto tempo você deixaria seu dinheiro investido (ano)?  "))
        def ipcam(c,t,a):
          i=0.0619
          if a==0:
              m=c*((1+(i))**t)
              return m-0.40*t
          else:
            m=c+(a*t)*((1+i)**t)
            return m-0.40*t
        ipcam(c,t,a)
        print(f"Em {t} você teria {ipcam(c,t,a)}")

    # Opção Inválida! :( #

    else:
          
          print("Opção inválida. Por favor tente novamente")

# Quero Investir! #

if escolha1 == 2:
    print("Onde você deseja investir?")
    print("1- Tesouro Prefixado  | 2- Tesouro SELIC  | 3- Tesouro IPCA+ ")
    escolha = int(input('Digite a opção desejada: '))

    # Quero investir em Tesouro Prefixado! #


    if escolha == 1:
      c=float(input("Digie o valor do investimento: "))
      a=float(input("Digite o valor do aporte: "))
      t=float(input("Por quanto tempo você deseja deixar o seu dinheiro investido(ano)?  "))
      def prefix(c,t,a):
          i=12.48
          if a==0:
            m=c*((1+(i/100))**t)
            return (f"Obrigado por investir com a SquidInvest! em {t} anos você terá um total de {m}!") 
            
          else:
            m=c+(a*t)*((1+(i/100)**t))
            return (f"Obrigado por investir com a SquidInvest! em {t} anos você terá um total de {m}!") 
      print(prefix(c,t,a))

    # Quero investir em Tesouro Selic! #


    elif escolha == 2:        
        c=float(input("Digie o valor do investimento: "))
        a=float(input("Digite o valor do aporte: "))
        t=float(input("Por quanto tempo você deseja deixar o seu dinheiro investido(ano)?  "))
        def selic(c,t,a):
          i=12.75
          if a==0:
            m=c*((1+(i))**t)
            return m-0.40*t
          else:
            m=c+(a*t)*((1+i)**t)
            return m-0.40*t
        selic(c,t,a)
        print(f"Em {t} você teria {selic(c,t,a)}")

    # Quero investir em Tesouro IPCA+ ! #


    elif escolha == 3:
        c=float(input("Digie o valor do investimento: "))
        a=float(input("Digite o valor do aporte: "))
        t=float(input("Por quanto tempo você deseja deixar o seu dinheiro investido(ano)?  "))
        def ipcam(c,t,a):
          i=0.0619
          if a==0:
              m=c*((1+(i))**t)
              return m-0.40*t
          else:
            m=c+(a*t)*((1+i)**t)
            return m-0.40*t
        ipcam(c,t,a)
        print(f"Em {t} você teria {ipcam(c,t,a)}")

    # Opção Inválida! :( #


    else:
          
          print("Opção inválida. Por favor tente novamente")
  
    