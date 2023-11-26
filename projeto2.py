# Projeto Mini Game usando o Módulo Turtle

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


    
        

    
    

    




        

        
    

        
    


 
    


 





   

