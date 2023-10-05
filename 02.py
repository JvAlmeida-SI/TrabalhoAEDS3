import random

numeros_vermelhos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36, 37, 38]

numero_selecionado = random.randint(1, 38)

if numero_selecionado == 37:
    numero_selecionado = 0
if numero_selecionado == 38:
    numero_selecionado = "00"

if int(numero_selecionado) == 0 or int(numero_selecionado) == 00:
    cor_selecionada = "verde"
elif numero_selecionado in numeros_vermelhos:
    cor_selecionada = "vermelho"
else:
    cor_selecionada = "preto"


if int(numero_selecionado)%2 == 0:
    paridade_selecionada = "ímpar"
else:
    paridade_selecionada = "par"


if int(numero_selecionado) >= 1 and int(numero_selecionado) <= 18:
    intervalo_selecionado = "1 a 18"
else:
    intervalo_selecionado = "19 a 36"

if cor_selecionada == "verde":
    print(f"Número sorteado: {numero_selecionado}")
    print(f"Pagar: {numero_selecionado}")
    print(f"Pagar: {cor_selecionada}")
else:
    print(f"Número sorteado: {numero_selecionado}")
    print(f"Pagar: {numero_selecionado}")
    print(f"Pagar: {cor_selecionada}")
    print(f"Pagar: {paridade_selecionada}")
    print(f"Pagar: {intervalo_selecionado}")