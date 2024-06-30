from cifrador import crea_cifrador

def test_cifrador_delta_1():
    mensaje = "ZigZag"
    delta = 1
    cifrar = crea_cifrador(delta)

    mensaje_cifrado = cifrar(mensaje)

    assert mensaje_cifrado == " JH BH" 

def test_cifrador_delta_1_negativo():
    mensaje = " JH BH"
    delta = -1
    cifrar = crea_cifrador(delta)

    mensaje_cifrado = cifrar(mensaje)

    assert mensaje_cifrado == "ZIGZAG" 

def test_cifrador_delta_3():
    mensaje = "ZigZag"
    delta = 3
    cifrar = crea_cifrador(delta)

    mensaje_cifrado = cifrar(mensaje)

    assert mensaje_cifrado == "BLJBDJ" 