def encontre_primos(limite):
    numeros_primos = [True] * (limite + 1)

    numeros_primos[0] = numeros_primos[1] = False

    for numero in range(2, int(limite**0.5) + 1):
        if numeros_primos[numero]:
            for multiplo in range(numero * numero, limite + 1, numero):
                numeros_primos[multiplo] = False

    primos_encontrados = [numero for numero, eh_primo in enumerate(numeros_primos) if eh_primo]

    return primos_encontrados

limite = int(input("Digite um limite para encontrar números primos: "))

if limite <= 1000000:
    primos = encontre_primos(limite)
    print(f"Números primos até {limite}:")
    print(primos)
else:
    print("Desculpe, o programa suporta limite de até 1.000.000.")