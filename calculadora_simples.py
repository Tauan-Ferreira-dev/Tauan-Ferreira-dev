def pergunta_padrao_soma():
     numero1=int(input('Número1: '))
     numero2=int(input('Número2: '))
     print(numero1+numero2)
def pergunta_padrao_subtração():
    numero1=int(input('Número1: '))
    numero2=int(input('Número2: '))
    print(numero1-numero2)
def pergunta_padrao_divisão():
    numero1=int(input('Número1: '))
    numero2=int(input('Número2: '))
    print(int(numero1/numero2))
def pergunta_padrao_multiplicação():
    numero1=int(input('Número1: '))
    numero2=int(input('Número2: '))
    print(numero1*numero2)
    
calculadora = input('Qual operação deseja realizar? Soma[s],Subtração[su],Multiplicação[m] e divisão[d]')
if calculadora == 's':
    pergunta_padrao_soma()
elif calculadora == 'su':
    pergunta_padrao_subtração()
elif calculadora == 'm':
    pergunta_padrao_multiplicação()
elif calculadora == 'd':
    pergunta_padrao_divisão()
       
                
        
       
        



