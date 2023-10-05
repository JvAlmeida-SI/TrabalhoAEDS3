pãesDormidos = int(input("Quantos pães dormidos você está comprando? "))

preçoNormal = 4.60

totalPaes = preçoNormal * pãesDormidos
    
desconto = totalPaes * 0.60
    
preçoTotal = totalPaes - desconto
    
largura = 20
    
preçoNormalFormatado = "{:.2f}".format(preçoNormal).rjust(largura - 6)
descontoFormatado = "{:.2f}".format(desconto).rjust(largura)
preçoTotalFormatado = "{:.2f}".format(preçoTotal).rjust(largura - 5)

print("Preço normal por pão: " + preçoNormalFormatado)
print("Desconto (60%): " + descontoFormatado)
print("Preço total a pagar: " + preçoTotalFormatado)