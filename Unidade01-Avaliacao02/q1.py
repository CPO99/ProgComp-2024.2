print("CONTADOR DE NÚMEROS DECRESCENTES ENTRE 10 E 987631\n")

N_INICIO = 10
N_FIM = 50

N_INICIO_INTERACAO = N_INICIO

CONT = 0 #contador

while N_INICIO_INTERACAO <= N_FIM: #rodando até o número final
    VER = True
    
    for n in range(0, len(str(N_INICIO_INTERACAO)) - 1):
        if int(str(N_INICIO_INTERACAO)[n]) < int(str(N_INICIO_INTERACAO)[n + 1]): #conversão dos números inteiros para tring, de modo a serem manipulados, e retornados para inteiro para condicional
            VER = False #false se algum dos algarismos do número o impedir de ser decrescente

    if VER:
        CONT += 1
        print(N_INICIO_INTERACAO)
        
    N_INICIO_INTERACAO += 1

print("\nEntre",N_INICIO,"e",N_FIM,"existem",CONT,"números decrescentes")
