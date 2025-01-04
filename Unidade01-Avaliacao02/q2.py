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
        DIV = DIV**ALG_CONT
        
        for i in range(ALG_CONT, 0, -1):
            print(i)

        """
                       
            if DIV == 10 and len(ALG) == ALG_CONT - 1:
                ALG.append(N % DIV)
            elif DIV == 10:
                ALG.append(N // DIV)
                DIV *= 10
            else:
                if N // DIV != 0:
                    ALG.append(N // DIV)
                    DIV *= 10
                else:
                    VER = False
        """

        print("\nLista formada",ALG)
        print("------------------------------------------------\n")
            

    except Exception as e:
        print("\n[ERRO] - VALOR INCORRETO INFORMADO. Tente novamente.\n", e)
        print("------------------------------------------------\n")
