# -*- coding: utf-8 -*-

#Iremos verificar a escala de febre de uma pessoa. Para isso iremos informar a 
#temperatura que a pessoa esta no momento. E o python irá responder a classificação
#de acordo com os seguintes valores: 
#Se a temperatura for menor que 37,3° : não tem febre;
#Se a temperatura for entre 37,3 e 37,8: febrícula;
#se a temperatura for maior que 37,8°: Febre

temperatura = 38

if temperatura < 37.3 :
    print("Não tem febre")
elif temperatura >= 37.3 and temperatura <= 37.8:
    print("Tem febricula")
else:
    print("Tem febre")
