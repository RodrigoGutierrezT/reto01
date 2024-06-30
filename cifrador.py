alfabeto = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ ")

def crea_cifrador(d: int) -> callable:

    def cifrador(mensaje):

        resultado = ""
        
        for caracter in mensaje:
            caracter = caracter.upper()
            if caracter in alfabeto:
                indice_actual = alfabeto.index(caracter)
                indice_nuevo = (indice_actual + d) % len(alfabeto)
                resultado += alfabeto[indice_nuevo]
            else:
                resultado += caracter
        
        return resultado


    return cifrador

def crea_par_cesar(d: int) -> tuple[callable, callable]:
    delta_negativo = -d
    cifrar = crea_cifrador(d)
    descifrar = crea_cifrador(delta_negativo)

    return (cifrar, descifrar)

