print("CONTADOR DE PARES DE NÚMEROS PRIMOS ÍMPARES CONSECUTVOS ATÉ 10000\n")

CONT = 3
CONT_2 = 0
VER = 0
PRIMO = 0
N = 3

while N < 10000:
    while CONT <= N / 2:
        if N % CONT == 0:
            VER += 1
        CONT += 1
    if VER == 0:
        if PRIMO == 0:
            PRIMO = N
        elif PRIMO + 2 == N:
            print(PRIMO,"-",N)
            PRIMO = N
            CONT_2 += 1
        else:
            PRIMO = N 

    VER = 0
    CONT = 2
    N += 1

print("\nTOTAL:",CONT_2,"pares")
