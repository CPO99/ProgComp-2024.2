import datetime

#Dados da data inicial
DATA_ANO = 1968
DATA_MES = 4
DATA_DIA = 27

#Ano controle
ANO_CONTROLE = DATA_ANO

#Dados da data atual
HOJE = datetime.datetime.today() 
HOJE_DIA = HOJE.day 
HOJE_MES = HOJE.month 
HOJE_ANO = HOJE.year

CONTADOR_DIAS = 0

#Controlador do laço
VER = True 

print(f"QUANTOS SÁBADOS HOUVE DO DIA {DATA_DIA}, MÊS {DATA_MES} E ANO {DATA_ANO} ATÉ O DIA {HOJE_DIA}, MÊS {HOJE_MES} E ANO {HOJE_ANO}?\n")

while VER: 
    #Condição para pegar somente os dias do ano inicial
    if ANO_CONTROLE == DATA_ANO:
        ANO = DATA_ANO
        MES = DATA_MES
        DIA = DATA_DIA
        
        BISSEXTO = 0 #bissexto como 1 ou 0 para somar aos dias na contagem no decorrer do codigo    

        #verificando se ano é bissexto
        if ANO % 400 == 0:
            BISSEXTO = 1
        else:
            if ANO % 4 == 0 and ANO % 100 != 0:
                BISSEXTO = 1
        
        if MES == 1:
            if DIA >= 1 and DIA <= 31: #verificando o intervalo de dias do mes
                CONTADOR_DIAS += DIA
        elif MES == 2: #fevereiro tem duas verificacoes de dias devido ao ano bissexto aumentar ou diminuir um dia desse mes
            if BISSEXTO == 1:
                if DIA >= 1 and DIA <= 29:
                   CONTADOR_DIAS += 31 + DIA 
            else:
                if DIA >= 1 and DIA <= 28:
                    CONTADOR_DIAS += 31 + DIA 
        elif MES == 3:
            if DIA >= 1 and DIA <= 31:
                CONTADOR_DIAS += 59 + DIA + BISSEXTO
        elif MES == 4:
            if DIA >= 1 and DIA <= 30:
                CONTADOR_DIAS += 90 + DIA + BISSEXTO
        elif MES == 5:
            if DIA >= 1 and DIA <= 31:
                CONTADOR_DIAS += 120 + DIA + BISSEXTO
        elif MES == 6:
            if DIA >= 1 and DIA <= 30:
                CONTADOR_DIAS += 151 + DIA + BISSEXTO
        elif MES == 7:
            if DIA >= 1 and DIA <= 31:
                CONTADOR_DIAS += 181 + DIA + BISSEXTO
        elif MES == 8:
            if DIA >= 1 and DIA <= 31:
                CONTADOR_DIAS += 212 + DIA + BISSEXTO
        elif MES == 9:
            if DIA >= 1 and DIA <= 30:
                CONTADOR_DIAS += 243 + DIA + BISSEXTO
        elif MES == 10:
            if DIA >= 1 and DIA <= 31:
                CONTADOR_DIAS += 273 + DIA + BISSEXTO
        elif MES == 11:
            if DIA >= 1 and DIA <= 30:
               CONTADOR_DIAS += 304 + DIA + BISSEXTO
        elif MES == 12:
            if DIA >= 1 and DIA <= 31:
               CONTADOR_DIAS += 334 + DIA + BISSEXTO
        
        if BISSEXTO == 1:
            CONTADOR_DIAS = 366 - CONTADOR_DIAS
        else:
            CONTADOR_DIAS = 365 - CONTADOR_DIAS

    #Condição para pegar somente os dias do ano final
    elif ANO_CONTROLE == HOJE_ANO:
        ANO = HOJE_ANO
        MES = HOJE_MES
        DIA = HOJE_DIA
        
        BISSEXTO = 0 #bissexto como 1 ou 0 para somar aos dias na contagem no decorrer do codigo    

        #verificando se ano é bissexto
        if ANO % 400 == 0:
            BISSEXTO = 1
        else:
            if ANO % 4 == 0 and ANO % 100 != 0:
                BISSEXTO = 1
        
        if MES == 1:
            if DIA >= 1 and DIA <= 31: #verificando o intervalo de dias do mes
                CONTADOR_DIAS += DIA
        elif MES == 2: #fevereiro tem duas verificacoes de dias devido ao ano bissexto aumentar ou diminuir um dia desse mes
            if BISSEXTO == 1:
                if DIA >= 1 and DIA <= 29:
                   CONTADOR_DIAS += 31 + DIA
            else:
                if DIA >= 1 and DIA <= 28:
                    CONTADOR_DIAS += 31 + DIA
        elif MES == 3:
            if DIA >= 1 and DIA <= 31:
                CONTADOR_DIAS += 59 + DIA + BISSEXTO
        elif MES == 4:
            if DIA >= 1 and DIA <= 30:
                CONTADOR_DIAS += 90 + DIA + BISSEXTO
        elif MES == 5:
            if DIA >= 1 and DIA <= 31:
                CONTADOR_DIAS += 120 + DIA + BISSEXTO
        elif MES == 6:
            if DIA >= 1 and DIA <= 30:
                CONTADOR_DIAS += 151 + DIA + BISSEXTO
        elif MES == 7:
            if DIA >= 1 and DIA <= 31:
                CONTADOR_DIAS += 181 + DIA + BISSEXTO
        elif MES == 8:
            if DIA >= 1 and DIA <= 31:
                CONTADOR_DIAS += 212 + DIA + BISSEXTO
        elif MES == 9:
            if DIA >= 1 and DIA <= 30:
                CONTADOR_DIAS += 243 + DIA + BISSEXTO
        elif MES == 10:
            if DIA >= 1 and DIA <= 31:
                CONTADOR_DIAS += 273 + DIA + BISSEXTO
        elif MES == 11:
            if DIA >= 1 and DIA <= 30:
               CONTADOR_DIAS += 304 + DIA + BISSEXTO
        elif MES == 12:
            if DIA >= 1 and DIA <= 31:
               CONTADOR_DIAS += 334 + DIA + BISSEXTO

        VER = False
        
    #Condição para pegar os dias dos anos entre o ano inicial e o ano final
    else:
        if ANO_CONTROLE % 400 == 0:
            CONTADOR_DIAS += 366
        else:
            if ANO_CONTROLE % 4 == 0 and ANO_CONTROLE % 100 != 0:
                CONTADOR_DIAS += 366
            else:
                CONTADOR_DIAS += 365

    ANO_CONTROLE += 1

print("Quantidade de sábados:",CONTADOR_DIAS // 7)