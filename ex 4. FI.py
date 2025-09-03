sh = 0
nj = int(input())
for i in range(nj):
    h = float(input())
    sh += h
media = sh/nj
print (f"a altura média do time é {media: .3} metros")