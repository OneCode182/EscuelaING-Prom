
creditos = 15

notas = {

    "prem" : [
        31

    ], "ageo" : [
        41

    ], "fume" : [
        41

    ], "fco" : [
        48

    ], "afsa" : [
        50

    ], "iins" : [
        35

    ]

}

tercios = len(notas["prem"])

def prom():
    nota = 0
    for i in range(tercios):
        nota += notas["prem"][i]*4
        nota += notas["ageo"][i]*4
        nota += notas["fume"][i]*3
        nota += notas["fco"][i]*2
        nota += notas["afsa"][i]
        nota += notas["iins"][i]
        
    return round(nota / creditos, 2)

print("Su promedio de tercio es =", prom())




"""

notas = {
    # -------------- { 4 creditos } --------------
    "prem" : [
        31

    ], "ageo" : [
        41

    # -------------- { 3 creditos } --------------
    ], "fume" : [
        41

    # -------------- { 2 creditos } --------------
    ], "fco" : [
        48

    # -------------- { 1 creditos } --------------
    ], "afsa" : [
        50

    ], "iins" : [
        40

    ]

}

"""