n = int(input())
nb= 0
sh =  0
while nb < n:
    h = float(input())
    sh +=h
    nb +=1
mh = sh/n
print (f"a média das alturas dos jogadores é: {mh: .3}")