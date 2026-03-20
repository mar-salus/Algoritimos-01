=========================================================================== FAILURES ===========================================================================
____________________________________________________________________________ test5 _____________________________________________________________________________

    def test5():
>       assert arpovado(5.9, 80, 0) == "Precisa fazer prova final"
               ^^^^^^^^
E       NameError: name 'arpovado' is not defined

test_aprovado.py:17: NameError
____________________________________________________________________________ test6 _____________________________________________________________________________

    def test6():
>       assert aprovado(6, 89, 21) == "Reprovado por falta"
E       AssertionError: assert 'Aprovado' == 'Reprovado por falta'
E         
E         - Reprovado por falta
E         + Aprovado

test_aprovado.py:20: AssertionError
____________________________________________________________________________ test7 _____________________________________________________________________________

    def test7():
>       assert aprovado(6, 80, 20) == "Aprovado"
E       AssertionError: assert 'Reprovado por faltas' == 'Aprovado'
E         
E         - Aprovado
E         + Reprovado por faltas

test_aprovado.py:23: AssertionError
=================================================================== short test summary info ====================================================================
FAILED test_aprovado.py::test5 - NameError: name 'arpovado' is not defined
FAILED test_aprovado.py::test6 - AssertionError: assert 'Aprovado' == 'Reprovado por falta'
FAILED test_aprovado.py::test7 - AssertionError: assert 'Reprovado por faltas' == 'Aprovado'
================================================================= 3 failed, 5 passed in 0.10s ==================================================================
@mar-salus ➜ /workspaces/Algoritimos-01 (main) $ 




____________________________________________________________________________ test2 _____________________________________________________________________________

    def test2():
>       assert aprovado(7, 80, 80) == "Reprovado por faltas"
E       AssertionError: assert 'Aprovado' == 'Reprovado por faltas'
E         
E         - Reprovado por faltas
E         + Aprovado

test_aprovado.py:7: AssertionError
____________________________________________________________________________ test3 _____________________________________________________________________________

    def test3():
>       assert aprovado(0, 80, 0) == "Precisa fazer a prova final"
E       AssertionError: assert 'Reprovado por faltas' == 'Precisa fazer a prova final'
E         
E         - Precisa fazer a prova final
E         + Reprovado por faltas

test_aprovado.py:10: AssertionError
____________________________________________________________________________ test5 _____________________________________________________________________________

    def test5():
>       assert aprovado(5.9, 80, 0) == "Precisa fazer prova final"
E       AssertionError: assert 'Reprovado por faltas' == 'Precisa fazer prova final'
E         
E         - Precisa fazer prova final
E         + Reprovado por faltas

test_aprovado.py:17: AssertionError
____________________________________________________________________________ test6 _____________________________________________________________________________

    def test6():
>       assert aprovado(6, 89, 21) == "Reprovado por falta"
E       AssertionError: assert 'Aprovado' == 'Reprovado por falta'
E         
E         - Reprovado por falta
E         + Aprovado

test_aprovado.py:20: AssertionError
=================================================================== short test summary info ====================================================================
FAILED test_aprovado.py::test2 - AssertionError: assert 'Aprovado' == 'Reprovado por faltas'
FAILED test_aprovado.py::test3 - AssertionError: assert 'Reprovado por faltas' == 'Precisa fazer a prova final'
FAILED test_aprovado.py::test5 - AssertionError: assert 'Reprovado por faltas' == 'Precisa fazer prova final'
FAILED test_aprovado.py::test6 - AssertionError: assert 'Aprovado' == 'Reprovado por falta'
================================================================= 4 failed, 4 passed in 0.10s ==================================================================
@mar-salus ➜ /workspaces/Algoritimos-01 (main) $ 

