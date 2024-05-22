def forca(tentativa):
    f1 = " +--------+ "
    f2 = " |        | "
    f3 = " |        o "
    f4 = " |       /|\ "
    f5 = " |        |  "
    f6 = " |       / \ "
    f7 = "_|___________"

    if tentativa>= 1:
        f2 = "   |      | "
    if tentativa>= 2:
        f3="     |    o  "
    if tentativa>= 3:
        f4 = " |       /|\ "
    if tentativa>= 4:  
       f5 = " |        |  "
    if tentativa>= 5:    
         f6 = " |       / \ "           

def Continua():
    while True:
        print("-" * 20)
        Novamente = input("Quer jogar de novo S/N:").upper()
        if Novamente == "S":
            Acabou = True
            break
        elif Novamente == "N":
            Acabou = False
            break
        else:
            print("Digite S ou N ")
    return Acabou  

Jogar = True
while Jogar :
    Jogar = Continua()

