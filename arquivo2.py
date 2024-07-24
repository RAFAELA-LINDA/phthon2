for i in range(1, 100):
    print(i)
i = 0
c = True
while c :
    i = i + 1
    print (i)
    if i < 99 :
        c = False 



with open("arquivo.txt", "w") as f :
    f. write ("text 1/h")
    f.write ("text 2/n")




try:
    f= open("arquivo2Txt", "w")
    f. write("eu 1/n")
    f.write("eu 2/n")
finally:
    f.close()


with open("arquivo.txt", "r") as f:
    txt = f.readline()
    print(txt)

    txt2 = f.readline
    print(txt2)
    
with open("arquivo2txt", "r") as f :
    l = f.readline()
    print (l)
    for lh in l:
     print(lh)

with open("arquivo.txt", "r") as f:
    txt = f.readline()
    print(txt)



def media(n1, n2, n3, n4):
    nota = n1 + n2 + n3 + n4
    m = nota/4
    return m 
print ("media 1", media(1,8,3,7))
print ("media 2", media(7,5,6,4))
print ("media 3", media(9,5,2))     

    
