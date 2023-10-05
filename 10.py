def distancia_edicao(p1, p2):
    if len(p1) == 0:
        return len(p2)
    if len(p2) == 0:
        return len(p1)

    if p1[-1] == p2[-1]:
        custo = 0
    else:
        custo = 1

    deletar = distancia_edicao(p1[:-1], p2) + 1
    inserir = distancia_edicao(p1, p2[:-1]) + 1
    substituir = distancia_edicao(p1[:-1], p2[:-1]) + custo

    return min(deletar, inserir, substituir)

p1 = input("Informe a primeira palavra: ")
p2 = input("Informe a segunda palavra: ")

distancia = distancia_edicao(p1, p2)
print(f"A distância de edição entre '{p1}' e '{p2}' é {distancia}")