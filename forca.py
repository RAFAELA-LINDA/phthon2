def forca(tentativa):
    f1 = " +--------+ "
    f2 = " |         "
    f3 = " |         "
    f4 = " |        "
    f5 = " |          "
    f6 = " |        "
    f7 = "_|___________"

    if tentativa >= 1:
        f2 = "   |      | "
    if tentativa >= 2:
        f3="     |      o  "
    if tentativa >= 3:
        f4 = " |        | "
    if tentativa >= 4:  
        f4 = " |         |\  "
    if tentativa >= 5:    
        f4 = " |      /|\ "  
    if tentativa >= 6:
        f5 = "|        |"
    if tentativa >= 7:
         f6 = "        / "
    if tentativa >= 8:
         f6 = "          \ "          

         print(f1)
         print(f2)
         print(f3)
         print(f4)
         print(f5)
         print(f6)
         print(f7)


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
x=0
while Jogar :
    print(x)
    forca(x)
    Jogar = Continua()
