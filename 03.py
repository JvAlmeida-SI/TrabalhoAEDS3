import random

numero_maximo = random.randint(1, 100)
atualizacoes_maximo = 0
print(f"O primeiro número gerado foi o {numero_maximo}\n")

for _ in range(99):
    numero_aleatorio = random.randint(1, 100)
    print(numero_aleatorio)

    if numero_aleatorio > numero_maximo:
        numero_maximo = numero_aleatorio
        atualizacoes_maximo += 1
        print(f"{numero_maximo} (atualizado)")

print(f"\nO valor máximo encontrado foi {numero_maximo}")
print(f"O número máximo de vezes que o maior valor foi atualizado foi {atualizacoes_maximo} vezes.")