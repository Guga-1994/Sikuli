# -*- coding: utf-8 -*-

automovel = "Moto"
tempo = 4 
pagamento = 0


print("=====================================")
print("Ticket de Estacionamento")
print("=====================================")

if automovel == "Carro":
    print("Automovel tipo Carro")
    if tempo == 1:
        print("Estacionamento Grátis!")
    else:
        pagamento = 3*tempo
        print("O valor do estacionamento é: ")
        print(pagamento)
else :
    print("Automovel tipo moto")
    if tempo == 1:
        print("Estacionamento Grátis!")
    else:
        pagamento = 6*tempo
        print("O valor do estacionamento é: ")
        print(pagamento)