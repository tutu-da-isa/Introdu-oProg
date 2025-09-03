nb = 1 
dp = 0
n = int(input())
if n < 2:
    print (f"{n} não é primo")
else:
    for i in range (n):
      if n%nb ==0:
          dp+= 1
      nb += 1
    if dp > 2:
        print (f"{n} não é primo")
    else:
        print(f"{n} é primo")