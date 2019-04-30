import numpy as np

T =  np.array([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1], [1, 0, 1, 0]])

C = np.array([1, 1, 1, 0, 0, 0])

N = np.array([1,0,0,1])

pVitoria = 3/6 
pDerrota = 3/6

def calcularProbabilidades(X, Y):
    pAtrVitoria = np.zeros(4)
    pAtrDerrota = np.zeros(4)

    ########################## COMPLETE O CÓDIGO AQUI  ########################
    #  Instrucoes: Complete o codigo para encontrar a probabilidade de
    #                ocorrencia de um atributo para uma determinada classe.
    #                Ex.: para a classe 1 (vitoria), devera ser computada um
    #                vetor pAtrVitoria (n x 1) contendo n valores:
    #                P(Atributo1=1|Classe=1), ..., P(Atributo5=1|Classe=1), e o
    #                mesmo para a classe 0 (derrota):
    #                P(Atributo1=1|Classe=0), ..., P(Atributo5=1|Classe=0).
    # 

    indexY1 = np.where(Y==1)
    pAtrVitoria = (X[indexY1]==1).sum(axis=0)
    pAtrVitoria = pAtrVitoria/sum(Y==1)    
    indexY0 = np.where(Y==0)
    pAtrDerrota = (X[indexY0]==1).sum(axis=0)
    pAtrDerrota = pAtrDerrota/sum(Y==0)				
    return pAtrVitoria, pAtrDerrota

pAtrVitoria, pAtrDerrota = calcularProbabilidades(T,C)

def classificacao(x,pVitoria,pDerrota,pAtrVitoria,pAtrDerrota):

    classe = 0;
    probVitoria= 0;
    probDerrota = 0;

    probVitoria= pVitoria;
    probDerrota = pDerrota;
    for i in range(len(x)) :
        if x[i] == 1:
            probVitoria = probVitoria * pAtrVitoria[i]
            probDerrota = probDerrota * pAtrDerrota[i]
        else:
            probVitoria = probVitoria * (1 - pAtrVitoria[i])
            probDerrota = probDerrota * (1 - pAtrDerrota[i])
            
    classe = 1 if probVitoria > probDerrota else 0
    ########################################################################## 

    return classe, probVitoria, probDerrota 

classe, probVitoria, probDerrota = classificacao( N,pVitoria,pDerrota,pAtrVitoria,pAtrDerrota )

if classe ==1:
    print('\n>>> Predicao = doente!')       
else:
    print('\n>>> Predicao = saudavel!')

print('\n>>>>>> Prob. doente = %0.6f!' %(probVitoria))
print('\n>>>>>> Prob. saudavel = %0.6f!\n\n'  %(probDerrota))    