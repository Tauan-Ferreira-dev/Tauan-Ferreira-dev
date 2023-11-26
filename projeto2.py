# # Desafio 🥇

# ### Desafio 1 

# Monte um mini-game turtle, que possibilite que o usuário controle para qual direção a tartaruga deve andar(frente/trás) e qual ângulo deverá ser tomado a cada nova movimentação

# ### Desafio 2 

# Usando o mini-game, desenha um quadrado passando instruções para a turtle, totalmente através do input do usuário

# #### Dicas Iniciais

# * Crie uma nova turtle primeiro

# * Coloca seu programa em loop 

# * Faça perguntas ao usuário para decidir se a tartaruga deve movimentar para frente ou para trás

# * Após decidir se ele deve movimentar para frente ou para trás, receba do usuário quantos pixels devem ser percorridos

# * Faça perguntas ao usuário para decidir se a tartaruga deve rotacionar para esquerda ou direta

# * Após decidir se ele deve rotacionar para esquerda ou direita, receba do usuário quantos pixels devem ser rotacionados

# * Ao executar essa ação pergunte ao usuário "Continuar andando?", e reaga de acordo com a resposta do usuário.

# #### Dicas Adicionais

# * Não esqueça de converter o input do usuário para o tipo apropriado

# * Resolva um problema de cada vez e lembre de seguir a seguinte lógica: 

# # Pergunte -> Processe resposta -> A
from turtle import Turtle 
t = Turtle()
t.speed(1)
while True:
    primeiro_passo = input('Devo movimentar para frente ou para tras?Digite f para frente e t para tras ')
    qtdpixels1 = int(input('Quantos pixels devo movimentar? '))
    if primeiro_passo == 'f':
        t.forward(qtdpixels1)
    elif primeiro_passo == 't':
        t.back(qtdpixels1)
    segundo_passo = input('Para qual direção devemos rotacionar?Digite[d] para direita e [e] para esquerda')
    if segundo_passo == 'd':
        qtdpixels_direita = int(input('Quantos pixels devemos rotacionar para a direita? '))
        t.right(qtdpixels_direita)
    elif segundo_passo == 'e':
        qtdpixels_esquerda = int(input('Quantos pixels devemos rotacionar para a esquerda? '))
        t.left(qtdpixels_esquerda)
    terceiro_passo = input('Quer continuar andando?Digite [s] para sim e [n] para não')
    if terceiro_passo == 's':
        continuar = primeiro_passo
    else:break


    
        

    
    

    




        

        
    

        
    


 
    


 





   

