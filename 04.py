def bissexto(ano):
    if (ano % 400 == 0) or ((ano % 4 == 0) and (ano % 100 != 0)):
        return True
    else:
        return False

anoInformado = int(input("Informe o ano: "))

if bissexto(anoInformado):
    print(f"{anoInformado} é ano bissexto")
else:
    print(f"{anoInformado} não é ano bissexto")