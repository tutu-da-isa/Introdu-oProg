nb = 1
n = int(input())
for i in range (n-1):
    n*= nb
    nb += 1
    if nb >= n:
        break
print(n)