a = int(input("Digite o primeiro valor:"))
b = int(input("Digite o segundo valor:"))

print()

if a < b:
    sequencia = list(range(a, b+1))
    print(sequencia)
elif a > b:
    sequencia = list(range(a, b-1, -1)) 
    #sequencia = list(range(b, a+1))
    print(sequencia)
else: #a e b são iguais
    print(a)

print("\n===========FIM===========")

############################################################

a = int(input("Digite o primeiro valor:"))
b = int(input("Digite o segundo valor:"))

print()

if (a < b):
    sequencia = list(range(a,b+1))
    print(sequencia)
elif(a > b):
    sequencia = list(range(b,a+1)) 
    print(sequencia)
else:
    print(a)
    
print("\n===========FIM===========")