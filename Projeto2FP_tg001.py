# Grupo 001
# Afonso Caetano nr 82539
# Hugo Gaspar nr 81977
# Matilde Nascimento nr 82083

#  TAD coordenada
# Representacao interna: tuplos
# O TAD coordenada sera utilizado para indexar as posicoes do tabuleiro, onde cada posicao do tabuleiro e indexada atraves da linha respetiva (um inteiro entre 1 e 4) e da coluna (um inteiro entre 1 e 4).

import random
import copy

# Construtor

def cria_coordenada (l,c):
    '''cria_coordenada: int x int -> coordenada
    cria_coordenada recebe dois argumentos do tipo inteiro, o l corresponde a linha e o c a coluna (ambos variam de 1 a 4) e devolve um elemento do tipo coordenada corresponde a posicao (l,c). Verifica a validade dos seus argumentos, e gera ValueError caso algum dos (ou ambos) dos argumentos introduzidos for invalido.'''
    
    if (isinstance(l,int) and isinstance(c,int)) and (1 <= l <= 4) and (1 <= c <=4): 
        return (l, c)
    else:
        raise ValueError('cria_coordenada: argumentos invalidos') 
    
# Seletor
    
def coordenada_linha (cc):
    '''coordenada_linha : coordenada -> inteiro
    coordenada_linha recebe como argumento um elemento do tipo coordenada e devolve a linha correspondente.'''
    l = cc[0]
    return l

# Seletor

def coordenada_coluna (cc):
    '''coordenada_coluna : coordenada -> inteiro
    coordenada_coluna recebe como argumento um elemento do tipo coordenada e devolve a coluna correspondente.'''    
    c = cc[1]
    return c

# Reconhecedor

def e_coordenada (universal):
    '''e_coordenada: universal -> logico
    e_coordenada recebe um unico argumento e devolve True caso esse argumento seja do tipo coordenada e False caso contrario.'''
    return isinstance(universal, tuple)\
                and len(universal) == 2\
                and (isinstance(universal[0], int)\
                and isinstance(universal[1], int))\
                and (1 <= universal[0] <= 4)\
                and (1 <= universal[1] <= 4)    

# Teste

def coordenadas_iguais (l,c):
    '''coordenadas_iguais: coordenada x coordenada -> logico
    coordenadas_iguais recebe como argumentos dois elementos do tipo coordenada e devolve True caso esses argumentos correspondam a mesma posicao (l,c) do tabuleiro, e False caso contrario.'''
    return l == c
  
#  TAD tabuleiro vai ser utilizado para representar o tabuleiro e permitira:
# a) um tabuleiro de 2048 (4x4) com a respectiva pontuacao;
# b) aceder a cada uma das posicoes do tabuleiro;
# c) aceder a pontuacao do tabuleiro;
# d) modificar o conteudo de cada uma das posicoes;
# e) actualizar a pontuacao do tabuleiro
# f) efetuar uma reducao, mover as pecas do tabuleiro numa dada direcao e combinar pecas continuas com o mesmo numero.'''

# Construtor  

def cria_tabuleiro ():
    '''cria_tabuleiro:
    cria_tabuleiro nao recebe qualquer argumento e devolve um elemento do tipo tabuleiro de acordo com a representacao interna escolhida (o tabuleiro vem com as posicoes todas a conter 0).'''
    
    return [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],0]
               
# Seletor                
    
def tabuleiro_posicao (t,c):
    '''tabuleiro_posicao: tabuleiro x coordenada -> inteiro
    tabuleiro_posicao recebe como argumentos um elemento t do tipo tabuleiro e outro c do tipo coordenada e devolve um elemento do tipo inteiro (que corresponde ao valor na posicao do tabuleiro correspondente a coordenada c. Se a posicao correspondente a c estiver vazia, devolve o valor 0. A funcao verifica se o segundo argumento e uma coordenada valida, e gera ValueError caso nao seja.'''
    if e_coordenada(c)==True:
    
        valor=t[coordenada_linha(c) - 1][coordenada_coluna(c) - 1]
        return valor
    
    else:
        raise ValueError('tabuleiro_posicao: argumentos invalidos')
    
# Seletor     
    
def tabuleiro_pontuacao(t):
    '''tabuleiro_pontuacao: tabuleiro -> inteiro
    tabuleiro_pontuacao recebe como argumento um elemento t do tipo tabuleiro e devolve a pontuacao atual do tabuleiro t.'''    
    
    return t[4]

# Seletor 

def tabuleiro_posicoes_vazias(t):
    '''tabuleiro_posicoes_vazias: tabuleiro -> lista
    tabuleiro_posicoes_vazias recebe como argumento um elemento t do tipo tabuleiro e devolve uma lista contendo as coordenadas de todas as posicoes vazias do tabuleiro t.'''    
    nova_lista=[]
    
    for linha_out in list(range(len(t)-1)):
        
        for coluna_out in list(range(len(t[linha_out]))):
            
                if t[linha_out][coluna_out]==0:
                        nova_lista =nova_lista + [cria_coordenada(linha_out+1,coluna_out+1)] 
    
    return nova_lista

# Modificador

def tabuleiro_preenche_posicao(t,c,v):
    '''tabuleiro_preenche_posicao: tabuleiro x coordenada x inteiro -> tabuleiro
    tabuleiro_preenche_posicao recebe como argumentos um elemento t do tipo tabuleiro, um elemento c do tipo coordenada, e um elemento v inteiro, e modifica o tabuleiro t colocando o valor v na posicao correspondente a coordenada c, e a funcao devolve o tabuleiro modificado. Verifica ainda se c e uma coordenada valida e se v e um inteiro. Caso pelo menos um dos argumentos introduzidos seja invalido a funcao gera ValueError.'''    
    
    if e_coordenada(c)==True and isinstance(v,int):
        
        linha=(coordenada_linha(c) - 1)
        coluna=(coordenada_coluna(c) - 1)
        t[linha][coluna]=v
        return t
    else:
        raise ValueError('tabuleiro_preenche_posicao: argumentos invalidos')
    
# Modificador    
    
def tabuleiro_actualiza_pontuacao(t,v):
    '''tabuleiro_actualiza_pontuacao: tabuleiro x inteiro -> tabuleiro
    tabuleiro_actualiza_pontuacao recebe como argumentos um elemento t do tipo tabuleiro e um elemento v inteiro, nao negativo e multiplo de 4. Modifica o tabuleiro t, acrescentando ao valor da respectiva pontuacao v pontos - e a funcao devolve o tabuleiro modificado. Verifica ainda se v e um inteiro nao negativo e multiplo de 4, e caso nao o seja, a funcao gera ValueError.'''    
    
    if isinstance(v,int)==True and v>=0 and v%4==0:        
        t[4]=t[4]+v
        
    else:
        raise ValueError('tabuleiro_actualiza_pontuacao: argumentos invalidos')
    
    return t

# Modificador

def tabuleiro_reduz(t,d):
    '''tabuleiro_reduz: tabuleiro x cadeia de caracteres -> tabuleiro
    tabuleiro_reduz recebe como argumentos um elemento t do tipo tabuleiro e uma cadeia de caracteres d (correspondente a uma das 4 posicoes possiveis: 'N', 'S', 'W' e 'E'). A funcao modifica o tabuleiro t, reduzindo-o na direcao d de acordo com as regras do jogo 2048 - e devolve o tabuleiro modificado com a pontuacao atualizada. Verifica ainda se d e uma jogada valida e caso nao seja gera ValueError.'''    
    
    if d=='N':
        
        for ciclo in range(4):
            for coluna in range(4):
                
                for linha in range(1,4):
                    
                    if t[linha][coluna]!=0 and t[linha-1][coluna]==0:
                        t[linha-1][coluna]=t[linha][coluna]
                        t[linha][coluna]=0
        
                        
        for coluna in range(4):
            
            for linha in range(1,4):
                
                if t[linha][coluna]==t[linha-1][coluna]:
                    t[linha-1][coluna]=t[linha-1][coluna] + t[linha][coluna]
                    t[linha][coluna]=0
                    t[4]=t[4]+t[linha-1][coluna]
                        
        for ciclo in range(4):
                    for coluna in range(4):
                        
                        for linha in range(1,4):
                            
                            if t[linha][coluna]!=0 and t[linha-1][coluna]==0:
                                t[linha-1][coluna]=t[linha][coluna]
                                t[linha][coluna]=0
        return t                       
    elif d=='S':
        
        for ciclo in range(4):
                    for coluna in range(4):
                        
                        for linha in range(2,-1,-1):
                            
                            if t[linha][coluna]!=0 and t[linha+1][coluna]==0:
                                t[linha+1][coluna]=t[linha][coluna]
                                t[linha][coluna]=0
                            
                       
        for coluna in range(4):
            
            for linha in range(2,-1,-1):
                
                if t[linha][coluna]==t[linha+1][coluna]:
                    t[linha+1][coluna]=t[linha+1][coluna] + t[linha][coluna]
                    t[linha][coluna]=0
                    t[4]=t[4]+t[linha+1][coluna]
                    
                        
        for ciclo in range(4):
                    for coluna in range(4):
                        
                        for linha in range(2,-1,-1):
                            
                            if t[linha][coluna]!=0 and t[linha+1][coluna]==0:
                                t[linha+1][coluna]=t[linha][coluna] 
                                t[linha][coluna]=0
        return t                   
    elif d=='E':
        
        for ciclo in range(4):
            for linha in range(4):
                
                for coluna in range(2,-1,-1):
                    
                    if t[linha][coluna]!=0 and t[linha][coluna+1]==0:
                        t[linha][coluna+1]=t[linha][coluna]
                        t[linha][coluna]=0
                                    
                        
        for linha in range(4):
            
            for coluna in range(2,-1,-1):
                
                if t[linha][coluna]==t[linha][coluna+1]:
                    t[linha][coluna+1]=t[linha][coluna+1] + t[linha][coluna]
                    t[linha][coluna]=0
                    t[4]=t[4]+t[linha][coluna+1]
                    
                        
        for ciclo in range(4):
            for linha in range(4):
                
                for coluna in range(2,-1,-1):
                    
                    if t[linha][coluna]!=0 and t[linha][coluna+1]==0:
                        t[linha][coluna+1]=t[linha][coluna] 
                        t[linha][coluna]=0  
        return t                
    elif d=='W':
        
        for ciclo in range(4):
            for linha in range(4):
                
                for coluna in range(1,4):
                    
                    if t[linha][coluna]!=0 and t[linha][coluna-1]==0:
                        t[linha][coluna-1]=t[linha][coluna]
                        t[linha][coluna]=0
        
        
        for linha in range(4):
            
            for coluna in range(1,4):
                
                if t[linha][coluna]==t[linha][coluna-1]:
                    t[linha][coluna-1]=t[linha][coluna-1] + t[linha][coluna]
                    t[linha][coluna]=0
                    t[4]=t[4]+t[linha][coluna-1]
                    
        for ciclo in range(4):
            for linha in range(4):
                
                for coluna in range(1,4):
                    
                    if t[linha][coluna]!=0 and t[linha][coluna-1]==0:
                        t[linha][coluna-1]=t[linha][coluna]
                        t[linha][coluna]=0
    
        return t   
    
    else:
        raise ValueError('tabuleiro_reduz: argumentos invalidos') 
    
# Reconhecedor    

def e_tabuleiro (universal):
    '''e_tabuleiro: universal -> logico
    e_tabuleiro funciona como um reconhecedor que recebe um unico argumento devolve True se o argumento for do tipo tabuleiro e, caso contrario, devolve False.'''
    
    if isinstance(universal,list)==True and len(universal)==5:
        if isinstance(universal[0],list) and isinstance(universal[1],list) and isinstance(universal[2],list) and isinstance(universal[3],list) and isinstance(universal[4],int):
            if len(universal[0])==4 and len(universal[1])==4 and len(universal[2])==4 and len(universal[3])==4:
                return True
            else: 
                return False
        else:
            return False         
    else:
        return False
    
# Funcao auxiliar

def copia_tabuleiro(t):
    '''copia_tabuleiro: tabuleiro -> tabuleiro
    copia_tabuleiro recebe como argumento um elemento t do tipo tabuleiro e devolve uma copia correspondente.'''    
    novo_tab=cria_tabuleiro()
    for linha in range(0,4):
        for coluna in range(0,4):
            tabuleiro_preenche_posicao(novo_tab,cria_coordenada(linha+1,coluna+1),tabuleiro_posicao(t,cria_coordenada(linha+1,coluna+1)))
    
    tabuleiro_actualiza_pontuacao(novo_tab,tabuleiro_pontuacao(t)) 
    
    return novo_tab

# Reconhecedor

def tabuleiro_terminado(t):
    '''tabuleiro_terminado: tabuleiro -> logico
    tabuleiro_terminado funciona como um reconhecedor que recebe como argumento um elemento t do tipo tabuleiro e devolve True caso o tabuleiro t esteja terminado (isto e, se o tabuleiro estiver cheio e nao existam mais movimentos possiveis) e, caso contrario, devolve False.'''    
    x = copia_tabuleiro(t)
    
    for j in ('N','S','W','E'):
        resultado=tabuleiro_reduz(x,j)
        
    if tabuleiro_posicoes_vazias(t)==[] and resultado==t:
        return True
            
    else:
        return False
    
# Teste    
    
def tabuleiros_iguais (t1, t2):
    '''tabuleiros_iguais: tabuleiro x tabuleiro -> logico
    tabuleiros_iguais funciona como um teste que recebe argumentos do tipo t1 e t2 do tipo tabuleiro e devolve True caso t1 = t2 (isto e, caso t1 e t2 tenham a mesma configuracao e pontuacao) e, caso contrario, devolve False.'''    
    return t1 == t2

# Funcao auxiliar

def pede_jogada():
    '''pede_jogada: {} -> cadeia de caracteres
    pede_jogada nao recebe nenhum argumento, mas pede ao utilizador que introduza uma direcao (N, S, E ou W). Caso o valor introduzido nao seja valido, a funcao volta a pedir novamente a informacao de jogada ao utilizador. A funcao devolve uma cadeia de caracteres correspondente a direcao escolhida.'''    
    jogada=input('Introduza uma jogada (N, S, E, W): ')
    if jogada=='N' or jogada=='S' or jogada=='E' or jogada=='W':
        return jogada
    else:
        print ('Jogada invalida.')
        pede_jogada()
    
# Funcao auxiliar    
    
def escreve_tabuleiro(t):
    '''escreve_tabuleiro: tabuleiro -> {}
    escreve_tabuleiro recebe como argumento um elemento t do tipo tabuleiro e escreve para o ecra a representacao externa de um tabuleiro do jogo 2048. Verifica ainda se t e um tabuleiro valido e, caso nao o seja, gera ValueError.'''    
    print('[',tabuleiro_posicao(t,cria_coordenada(1,1)),']','[',tabuleiro_posicao(t,cria_coordenada(1,2)),']','[',tabuleiro_posicao(t,cria_coordenada(1,3)),']','[',tabuleiro_posicao(t,cria_coordenada(1,4)),'] ')
    print('[',tabuleiro_posicao(t,cria_coordenada(2,1)),']','[',tabuleiro_posicao(t,cria_coordenada(2,2)),']','[',tabuleiro_posicao(t,cria_coordenada(2,3)),']','[',tabuleiro_posicao(t,cria_coordenada(2,4)),'] ')
    print('[',tabuleiro_posicao(t,cria_coordenada(3,1)),']','[',tabuleiro_posicao(t,cria_coordenada(3,2)),']','[',tabuleiro_posicao(t,cria_coordenada(3,3)),']','[',tabuleiro_posicao(t,cria_coordenada(3,4)),'] ')
    print('[',tabuleiro_posicao(t,cria_coordenada(4,1)),']','[',tabuleiro_posicao(t,cria_coordenada(4,2)),']','[',tabuleiro_posicao(t,cria_coordenada(4,3)),']','[',tabuleiro_posicao(t,cria_coordenada(4,4)),'] ')
    print('Pontuacao:', tabuleiro_pontuacao(t))
    
# Funcao auxiliar    

def preenche_posicao_aleatoria(t):
    '''preenche_posicao_aleatoria: tabuleiro -> tabuleiro
    preenche_posicao_aleatoria recebe como argumento um elemento t do tipo tabuleiro e devolve o tabuleiro modificado de acordo com as probabilidades correspondestes ao valor 2 e ao 4.'''    
    coordenada=random.choice(tabuleiro_posicoes_vazias(t))
    
    linha=coordenada_linha(coordenada)
    
    coluna=coordenada_coluna(coordenada)
    
    valor=int(random.choice('22224'))
    
    tabuleiro_preenche_posicao(t,cria_coordenada(linha,coluna),valor)
    
    return t

# Funcao auxiliar

def jogo_2048():
    '''jogo_2048: {} -> {}
    jogo_2048 e a funcao principal do jogo. Nao recebe qualquer argumento e permite ao utilizador que jogue um jogo completo de 2048.'''    
    
    t = cria_tabuleiro()
    
    preenche_posicao_aleatoria(t)
    preenche_posicao_aleatoria(t)
    
    escreve_tabuleiro(t)
    
    while tabuleiro_terminado(t) == False:
        copia=copia_tabuleiro(t)
        jogada=pede_jogada()
        
    
        reducao=tabuleiro_reduz(t,jogada)
        
        
        if tabuleiros_iguais(copia,reducao)==False:
        
            preenche_posicao_aleatoria(t)
        
        escreve_tabuleiro(t)