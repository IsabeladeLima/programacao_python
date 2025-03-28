secret_number = 777

print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")

num = int(input("Digite o numero para advinhar se é o correto: "))

while num !=777:
    print("Ha ha! Você está preso no meu loop!")
    num = int(input("Digite novamente o numero para advinhar se é o correto: "))

print("Muito bem, trouxa! Você está livre agora.")
