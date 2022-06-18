######### Tesouro Prefixado #########
def prefix(c,t,a):
    i=12.48
    if a==0:
        m=c*((1+(i/100))**t)
        return m-0.40*t
    else:
        m=c+(a*t)*((1+(i/100)**t))
        return m-0.40*t

######### Tesouro SELIC #########

def selic(c,t,a):
    i=12.75
    if a==0:
        m=c*((1+(i))**t)
        return m-0.40*t
    else:
        m=c+(a*t)*((1+i)**t)
        return m-0.40*t

            
######## Tesouro IPCA+ ######## 

def ipcam(c,t,a):
    i=0.0619
    if a==0:
        m=c*((1+(i))**t)
        return m-0.40*t
    else:
        m=c+(a*t)*((1+i)**t)
        return m-0.40*t