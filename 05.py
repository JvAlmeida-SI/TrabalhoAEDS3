def bissexto(ano):
    if (ano % 400 == 0) or ((ano % 4 == 0) and (ano % 100 != 0)):
        return True
    else:
        return False

def quantidade_de_dias_em_um_mes(mes, ano):
    if mes < 1 or mes > 12:
        return "Mês inválido"

    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if bissexto(ano):
        dias_por_mes[1] = 29

    return dias_por_mes[mes - 1]


anoInformado = int(input("Informe o ano: "))
mesInformado = int(input("Informe o mês: "))

dias_no_mes = quantidade_de_dias_em_um_mes(mesInformado, anoInformado)
print(f"O mês {mesInformado}/{anoInformado} possui {dias_no_mes} dias.")