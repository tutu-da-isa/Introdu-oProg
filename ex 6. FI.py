Mmedia = 0
mmedia = 999
aa = 0
ar = 0
for i in range(3):
    n1 = float(input("nota 1: "))
    n2 = float(input("nota 2: "))
    n3 = float(input("nota 3: "))
    m = (n1+n2+n3)/3
    if m> Mmedia:
        Mmedia = m
    if m<mmedia:
        mmedia = m
    if m>=6:
        aa+=1
    else:
        ar+=1
print ("a maior média é", Mmedia )
print ("a menor média é", mmedia )
print (f"{aa: .2} alunos foram aprovados")
print (f"{ar: .2} alunos foram reprovados")
    