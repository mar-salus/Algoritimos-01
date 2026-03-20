from aprovado2 import aprovado 

def test1():
    assert aprovado(10, 80, 0) == "Aprovado"

def test2():
    assert aprovado(7, 80, 80) == "Reprovado por faltas"

def test3():
    assert aprovado(0, 80, 0) == "Precisa fazer a prova final"

#teste nota 6 sem faltas 
def test4():
    assert aprovado(6.1, 80, 0) == "Aprovado"

def test5():
    assert aprovado(5.9, 80, 0) == "Precisa fazer prova final"

def test6():
    assert aprovado(6, 89, 21) == "Reprovado por falta"

def test7():
    assert aprovado(6, 80, 20) == "Aprovado"

def test8():
    assert aprovado(6, 80, 19) == "Aprovado"