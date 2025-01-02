print("CONTADOR DE NÚMEROS DECRESCENTES ENTRE 10 E 987631\n")

N_INICIO = 10
N_FIM = 987631

N_INICIO_INTERACAO = N_INICIO

CONT = 0

while N_INICIO_INTERACAO <= N_FIM:
    VER = True
    
    for n in range(0, len(str(N_INICIO_INTERACAO)) - 1):
        if str(N_INICIO_INTERACAO)[n] < str(N_INICIO_INTERACAO)[n + 1]:
            VER = False

    if VER:
        CONT += 1
        print(N_INICIO_INTERACAO)
        
    N_INICIO_INTERACAO += 1

print("\nEntre",N_INICIO,"e",N_FIM,"existem",CONT,"números decrescentes")
