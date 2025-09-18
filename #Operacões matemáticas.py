#Operacões matemáticas
import sys
sys.set_int_max_str_digits(999999999)
pv = ["1", "2", "3", "4", "5", "6", "7", "sair"]
print("Escolha uma das seguintes opções: \n 1- soma \n 2- subtração \n 3- multiplicação \n 4- divisão \n 5- par ou impar \n 6- primo \n 7- fatorial \n para encerrar digite sair. ")
n = (input("digite o número da operação desejada: "))
n1=n.lower()

while n1 != "sair":
    if n1 == "1":
        x = int(input("digite o primeiro número: "))
        y = int(input("digite o segundo número: "))
        print (f"o resultado da soma de {x} e {y} é {x+y}")
    if n1 == "2":
        x = int(input("digite o primeiro número: "))
        y = int(input("digite o segundo número: "))
        print (f"o resultado da subtração de {x} e {y} é {x-y}")
    if n1 =="3":
        x = int(input("digite o primeiro número: "))
        y = int(input("digite o segundo número: "))
        print (f"o resultado da multiplicação de {x} e {y} é {x*y}")
    if n1 =="4":
        x = int(input("digite o primeiro número: "))
        y = int(input("digite o segundo número: "))
        print (f"o resultado da divisão de {x} e {y} é {x/y}")
    if n1 =="5":
        x = int(input("digite o número: "))
        if x%2 ==0:
            print (f"o número {x} é par")
        else:
            print (f"o número {x} é impar")
    if n1 =="6":
        x = int(input("digite o número: "))
        nb = 1
        dp = 0
        if x < 2:
            print (f"{x} não é primo")
        else:
            for i in range (x):
                if x%nb ==0:
                    dp +=1
                nb +=1
            if dp > 2:
                print(f"tem {dp} divisões possiveis, portanto não é primo")
            else:
                print(f"tem {dp} divisões possiveis, portanto é primo")
    if n1 =="7":
        x = int(input("digite o número: "))
        fat = 1
        nb=1
        while nb <=x:
            fat*=nb
            nb += 1
        print (f"o fatorial do número digitado é {fat}")
    print ("  \n  ")
    print("Escolha uma das seguintes opções: \n 1- soma \n 2- subtração \n 3- multiplicação \n 4- divisão \n 5- par ou impar \n 6- primo \n 7- fatorial \n para encerrar digite sair. ")    
    n = (input("digite o número da operação desejada: "))
    n1=n.lower()
