import random
continuar = "S"
Perro = 0
Pcerto = 0
while continuar.upper() == "S":
    ns = random.randint (1,10)
    T = 3
    while(T > 0):
        print ("você tem", T, "Tentativas")
        T = T -1
        nc = int(input("Digite um número entre 1 e 10:"))
        if ( ns == nc):
            print ("Você aertou.")
            T = 0
            Pcerto = Pcerto +1
        else:
            print("Você errou.")
            Perro = Perro +1
        print("número de acerto:",Pcerto)
        print("número de erros:",Perro)
    continuar = input("Deseja continuar? (s)im")             
