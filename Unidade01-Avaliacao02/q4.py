import random

print("----------------------TERMO----------------------\n")

#cores
VERD = "\033[42m"
VERM = "\033[41m"
AMA = "\033[43m"
RES = "\033[m"

print("DICAS DO JOGO\n")
print("-Cores das letras:")
print(f"--{VERD}Verde{RES}: posição e letra corretos")
print(f"--{AMA}Amarelo{RES}: letra existe, mas a posição está incorreta")
print(f"--{VERM}Vermelho{RES}: letra incorreta\n")
print("-Jogadas:")
print("--Você tem até 7 tentativas para descobrir as palavras\n")
print("-Obs:")
print("--Só valem palavras pré-selecionadas, demais serão ignoradas e tentativa se repete\n\n")

print("BOM JOGO!!!\n")

#palavras pré-selecionadas
PALAVRAS = (
    "ADAGA", "ADUBO", "AMIGO", "ANEXO", "ARAME", "ARARA", "ARROZ",
    "ASILO", "ASTRO", "BAILE", "BAIXA", "BALAO", "BALSA", "BARCO",
    "BARRO", "BEIJO", "BICHO", "BORDA", "BORRA", "BRAVO", "BREJO",
    "BURRO", "CAIXA", "CALDO", "CANJA", "CARRO", "CARTA", "CERVO",
    "CESTA", "CLIMA", "COBRA", "COLAR", "COQUE", "COURO", "CRAVO",
    "DARDO", "FAIXA", "FARDO", "FENDA", "FERRO", "FESTA", "FLUOR",
    "FORCA", "FORNO", "FORTE", "FUNDO", "GAITA", "GARRA", "GENIO",
    "GESSO", "GRADE", "GRANA", "GRAMA", "GURIA", "GREVE", "GRUTA",
    "HEROI", "HOTEL", "ICONE", "IMPAR", "IMUNE", "INDIO", "JUNTA",
    "LAPIS", "LARVA", "LAZER", "LENTO", "LESTE", "LIMPO", "LIVRO",
    "MACIO", "MAGRO", "MALHA", "MANSO", "MARCO", "METAL", "MORTE",
    "MORRO", "MURAL", "MOVEL", "NACAO", "NINHO", "NOBRE", "NORMA",
    "NORTE", "NUVEM", "PACTO", "PALHA", "PARDO", "PARTE", "PEDRA",
    "PEDAL", "PEIXE", "PRADO", "PISTA", "POMBO", "POETA", "PONTO",
    "PRATO", "PRECO", "PRESO", "PROSA", "PRUMO", "PULGA", "PULSO",
    "QUEPE", "RAIVA", "RISCO", "RITMO", "ROSTO", "ROUPA", "SABAO",
    "SALTO", "SENSO", "SINAL", "SITIO", "SONHO", "SOPRO", "SURDO",
    "TARDE", "TERNO", "TERMO", "TERRA", "TIGRE", "TINTA", "TOLDO",
    "TORRE", "TRAJE", "TREVO", "TROCO", "TRONO", "TURMA", "URUBU",
    "VALSA", "VENTO", "VERDE", "VISAO", "VINHO", "VIUVO", "ZEBRA"
)

#número de tentativas iniciando com -1, de modo que possa percorrer lista ou string iniciando no laço com zero
TENT = -1

#definindo as duas palavras de forma aleatória 
PALAVRA_1 = [random.choice(PALAVRAS), False]
PALAVRA_2 = [random.choice(PALAVRAS), False]

#lista com números ordinais, para uma melhor organização das tentativas
TENTATIVAS = ["PRIMEIRA","SEGUNDA","TERCEIRA","QUARTA","QUINTA","SEXTA","SÉTIMA"]
CLASSIFIC = ["Impossível","Ninja","Impressionante","Interessante","Pode melhorar","Foi por pouco"]

#laço que garante a distinção entre as palavras 1 e 2
while PALAVRA_1[0] == PALAVRA_2[0]:
    PALAVRA_2[0] = random.choice(PALAVRAS)

print("\nPalavra 1:",len(PALAVRA_1[0]) * "-")
print("Palavra 2:",len(PALAVRA_2[0]) * "-")

#laço das 7 tentativas possíveis para encontrar as duas palavras
while TENT < 6:
    TENT += 1
    print("\n" + TENTATIVAS[TENT],"TENTATIVA")
    
    #salvando somente os primeiros dígitos até a quantidade de caracteres dos termos, e convertendo para maiúsculo
    P = input("\nInforme a palavra: ")[:len(PALAVRA_1[0])].upper()
    
    if P in PALAVRAS:
        print("\nPalavra 1: ",end="")

        CONT = -1
        if P == PALAVRA_1[0] or PALAVRA_1[1] == True:   
            PALAVRA_1[1] = True
            print(f"{VERD}{PALAVRA_1[0]}{RES}",end="")
        else:
            for i in P:
                CONT += 1
 
                if i == PALAVRA_1[0][CONT]:
                    print(f"{VERD}{i}{RES}",end="")
                elif i in PALAVRA_1[0][CONT:]:
                    print(f"{AMA}{i}{RES}",end="")
                else:
                    print(f"{VERM}{i}{RES}",end="")

        CONT = -1
    
        print("\nPalavra 2: ",end="")
        if P == PALAVRA_2[0] or PALAVRA_2[1] == True:   
            PALAVRA_2[1] = True
            print(f"{VERD}{PALAVRA_2[0]}{RES}",end="")
        else:
            for i in P:
                CONT += 1
 
                if i == PALAVRA_2[0][CONT]:
                    print(f"{VERD}{i}{RES}",end="")
                elif i in PALAVRA_2[0][CONT:]:
                    print(f"{AMA}{i}{RES}",end="")
                else:
                    print(f"{VERM}{i}{RES}",end="")
    else:
        print("\n[ERRO] - Palavra não aceita")
        TENT -= 1

    if PALAVRA_1[1] == True == PALAVRA_2[1]:
        print(f"\n\n{CLASSIFIC[TENT]}!!! PARABÉNS!!")
        input("")

    print("\n__________________________________________")
    
