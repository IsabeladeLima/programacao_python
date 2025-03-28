impar = 0
par = 0
 

numero = int(input("Digite um número ou digite 0 para parar: "))
 
while numero != 0:

    if numero % 2 == 1:
        impar += 1
    else:
        par += 1

    numero = int(input("Digite um número ou digite 0 para parar: "))
 

print("Números ímpares contam:", impar)
print("Números pares contam:", par)
