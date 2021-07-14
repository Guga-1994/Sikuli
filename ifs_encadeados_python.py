# -*- coding: utf-8 -*-

realizouAulaDirecao = False
passouTesteVisao = True
passouTestePsicologico = False
notaExameFinal = 7.0

if realizouAulaDirecao:
    print("Realizou aulas de direção")
    if passouTesteVisao:
        print("Passou no teste de visão")
        if passouTestePsicologico:
            print("Passou no teste psicologico")
            if notaExameFinal >= 7:
                print("Parabéns. você tirou a carteira de motorista")
            else:
                print("Você não passou no exame final")
        else:
            print("Não passou no teste psicologico")
    else:
        print("Não passou no teste de visão")
else:
    print("Não realizou aulas de direção")