print("VERIFICANDO SE NÚMERO É PALÍNDROMO")
print("OBS: informe 0 (zero) para sair\n")

N = 1

while N != 0:
    try:
        N = int(input("Informe um número: "))

        VER = True #verificador para parar laço interação com o número informado
        DIV = 10 #divisor, para separar cada algarismo, iniciando com 10
        ALG_CONT = 1 #quantidade de algarismos que o número possui

        #verificando a quantidade de algarismos que o número possui
        while VER:
            if N // DIV != 0:
                ALG_CONT += 1
                
                DIV *= 10
            else:
                VER = False

        VER = True
        ALG = [None] * ALG_CONT #lista para guardar cada algarismo do número
        DIV = 10**(ALG_CONT - 1)
        N_COP = N
        
        for i in range(ALG_CONT - 1, 0 - 1, -1):
            if DIV == 10 and i == 0:
                ALG[i] = N_COP % DIV
                VER = False
            elif DIV == 10:
                ALG[i] = N_COP // DIV
                N_COP -= (N_COP // DIV) * DIV
            else:
                ALG[i] = N_COP // DIV
                N_COP -= (N_COP // DIV) * DIV
                DIV /= 10
     
        CONT = ALG_CONT - 1
        SOMA = 0
        
        for i in ALG:
            SOMA += i * (10**CONT)
            CONT -= 1
            
        PALINDROMO = "NÃO"
        
        if N == SOMA:
            PALINDROMO = "SIM"
            
        print("\nORIGINAL:",N)
        print("INVERTIDO:",int(SOMA))

        print("\nNÚMERO É PALÍNDROMO?",PALINDROMO)

        print("\n------------------------------------------------\n")
            

    except Exception as e:
        print("\n[ERRO] - VALOR INCORRETO INFORMADO. Tente novamente:", e)
        print("\n------------------------------------------------\n")
