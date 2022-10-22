from platform import python_branch


#!/usr/bin/python

def conjucion(V1, V2):
    return (V1 and V2)

def disyuncion(V1, V2):
    return (V1 or V2)

def negacion(V):
    return not(V)

def condicional(V1, V2):
    if (V1 == 1 and V2 == 0):
        return 0
    else:
        return 1

def bicondicional(V1, V2):
    return(condicional(V1, V2) and condicional (V1, V2))

def main():
    for A in range(2):
        for B in range(2):
            for C in range(2):
                formula = bool(conjucion(disyuncion(disyuncion(A, negacion(A)), negacion(B)), disyuncion(C, negacion(C))))
                print ("Entrada >" ,A,B,C, "Resultados >", formula)


main()