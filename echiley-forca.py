# o import importa um biblioteca, random é uma biblioteca para palavras aleatorias.
import random
#criando uma variavel para armazenar as palavras que serão sorteadas.
palavras = []
#variavel para quando o jogador digitar uma letra errada, que no entanto está vazia
letrasErradas = ''
# variavel para quando o jogador digitar uma letra certa, que no entanto está vazia
letrasCertas = ''
#variavel para adicionar um caractere a cada letra errada.
FORCAIMG = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
def palavraAdd():
    global palavras
    while True:
        p = input('digite as palavras para começar a jogar: ')
        palavras.append(p)
        if p == "":
            break
    
#função para criar uma função
def principal():
    """
    Função Princial do programa
    """
    print('F O R C A')
    palavraAdd()
#palavrasecreta vai ser definida pela função sortearpalavra,assim sairá uma palavra aleatoria.
    palavraSecreta = sortearPalavra()
#o jogador irá palpitar uma letra
    palpite = ''
#função que assim que o jogador errar irá para proxima imagem do FORCAIMG.
    desenhaJogo(palavraSecreta,palpite)
#while serve para começar um loop, que no caso 
    while True:
        palpite = receberPalpite() 
        desenhaJogo(palavraSecreta,palpite)
#se a pessoa estiver encerrado as suas chances o jogo ira avisar que a pessoa perdeu.
        if perdeuJogo():
            print('Voce Perdeu!!!')
#o break ira quebrar o loop
            break
#quando a pessoa completar a palavra ira mostrar que ela ganhou 
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')
            break            
#função para quando a pessoa errar, aumentar os caracteres na variavel FORCAIMG.       
def perdeuJogo():
#quando quero usar uma variavel fora da função usamos a tag global. 
    global FORCAIMG
#se a quantidade de letras erradas da pessoa foi igual a quantidade de caracteris de forcaimg a pessoa perdeu o jogo, pois len serve para contar a quantidade da lista.    
    if len(letrasErradas) == len(FORCAIMG):
#A função return retorna a função perdeu o jogo por ser verdadeira.        
        return True
    else:
#Quando o return é falso ele nao faz nada.
        return False
#aqui esta a função para quando a pessoa acertar.    
def ganhouJogo(palavraSecreta):
#global chamou a variavel letras certas 
    global letrasCertas
    ganhou = True
#para cada letra que estiver na palavrasecreta e nao estiver na lista de letrascertas vc errou e o ganhou é falso.     
    for letra in palavraSecreta:
        if letra not in letrasCertas:
            ganhou = False
#caso contrario o return retorna a ganhou true.            
    return ganhou        
        

#função para o jogador palpitar.
def receberPalpite():
#quando o jogador digitar mais de uma letra, irá aparecer na tela para ele digitar so uma por vez.    
    palpite = input("Adivinhe uma letra: ")
    palpite = palpite.upper()
    if len(palpite) != 1:
        print('Coloque um unica letra.')
#quando vc ja estiver digitado a letra, ira aparecer que essa letra ja foi digitada        
    elif palpite in letrasCertas or palpite in letrasErradas:
        print('Voce ja disse esta letra.')
#se o jogador digitar um caractere diferente do alfabeto, aparecerá para escolher so letras.        
    elif not "A" <= palpite <= "Z":
        print('Por favor escolha apenas letras')
#se caso todas as afirmações acima for falsa ele retorna no palpite para a pessoa palpitar.       
    else:
        return palpite
    
#nessa função vai chamar as variveis letrascertas letraserradas e FORCAIMG para printar na tela as letras certas e erradas e quando a pessoa errar desenha uma parte do boneco.      
def desenhaJogo(palavraSecreta,palpite):
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)])
    
#para cada letra da palavra secreta adiciona um "-"(tracinho).     
    vazio = len(palavraSecreta)*'-'
#se o palpite do jogador estiver na palvra secreta vai adicionar na variavel letrascertas .Se não adiciona em letraserradas.   
    if palpite in palavraSecreta:
        letrasCertas += palpite
    else:
        letrasErradas += palpite
#quando o jogador digitar uma letra que tem na palavrasecreta sustituirá cada tracinho(vazio) para a letra digitada corretamente.
    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
#vai printar na tela as letras erradas e certas e tambem os tracinhos.                
    print('Acertos: ',letrasCertas )
    print('Erros: ',letrasErradas)
    print(vazio)
     
#nessa função sotea uma palavra.
def sortearPalavra():
    global palavras
    return random.choice(palavras).upper()
#função upper é para deixar tudo em maiusculo.

principal()
