vp = 0
vn = 0
for i in range (20):
    n= int(input())
    if n >= 0:
        vp += n
    else:
        vn += 1
print ("valores positivos:", vp)
print ("tem", vn, "valores negativos")