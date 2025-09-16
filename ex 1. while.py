nb = 0
np = 0
ng = 0
while nb < 20:
    n = int(input())
    if n>0:
        np+=n
    else:
        ng+=1
    nb+=1
print (f"a soma dos valores positivos é: {np}")
print (f"possuem {ng} números negativos")