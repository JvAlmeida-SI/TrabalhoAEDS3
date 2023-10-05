def dataMagica(dia, mes, ano):
    return dia * mes == ano % 100

def datasMagicasDoSeculoXX():
    for ano in range(1900, 2000):
        for mes in range(1, 13):
            for dia in range(1, 32):
                if dataMagica(dia, mes, ano):
                    print(f"{dia:02}/{mes:02}/{ano}")

datasMagicasDoSeculoXX()