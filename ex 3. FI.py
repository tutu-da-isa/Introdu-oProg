nb = 0 
n = int(input())
for i in range(n):
    n += nb
    nb += 1
    if nb >= n:
        break
print(n)