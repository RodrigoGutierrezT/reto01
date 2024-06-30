from cifrador import crea_par_cesar

def test_par_cesar_3():
    msje_original = "ZIGZAG"
    msje_esperado = "BLJBDJ"

    cifrar, descifrar = crea_par_cesar(3)

    assert cifrar(msje_original) == msje_esperado
    assert descifrar(msje_esperado) == msje_original 