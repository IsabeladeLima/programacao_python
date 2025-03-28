palavra_secreta = 'chupacabra'

while True:
    entrada= input("digite uma palavra para saber se é a secreta: ")
    
    if entrada == palavra_secreta:
        print("parabens voce descobriu a palavra secreta.")
        break
    else:
        print("palavra", entrada,  "errada. Tente de novo.")
