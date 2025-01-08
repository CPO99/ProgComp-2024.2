import random

print("T-E-R-M-O")

palavras = (
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

TENT = -1

#definindo as duas palavras de forma aleatória 
PALAVRA_1 = random.choice(palavras)
PALAVRA_2 = random.choice(palavras)

#lista com números ordinais, para uma melhor organização das tentativas
TENTATIVAS = ["PRIMEIRA","SEGUNDA","TERCEIRA","QUARTA","QUINTA","SEXTA","SÉTIMA"]

#laço que garante a distinção entre as palavras 1 e 2
while PALAVRA_1 == PALAVRA_2:
    PALAVRA_2 = random.choice(palavras)

print("Palavra 1:",PALAVRA_1)
print("Palavra 2:",PALAVRA_2)

#laço das 7 tentativas possíveis para encontrar as duas palavras
while TENT < 6:
    TENT += 1
    print("\n" + TENTATIVAS[TENT],"TENTATIVA")
    P = input("\nInforme a palavra: ")[:len(PALAVRA_1)] #salvando somente os primeiros dígitos até a quantidade de caracteres dos termos

    print("\nPalavra 1: ",end="")

    CONT = -1
        
    for i in P:
        CONT += 1
 
        if P[CONT] == PALAVRA_1[CONT]:
            print("\033[N;N;Nm Olá")#+i+"\033[m'",end="")
        else:
            print(i,end="")

    print("\n__________________________________________")
    
