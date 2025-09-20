# tests/test_calculadora.py
import pytest
from src.calculadora import somar, dividir, subtracao, multiplicacao

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0

def test_dividir():
    assert dividir(10, 2) == 5
    with pytest.raises(ValueError):
        dividir(10, 0)  

def test_subtrair():
    assert subtracao(3,2) == 1
    assert subtracao(0, 1) == -1

def test_multiplicacao():
    assert multiplicacao(2, 3) == 6
    assert multiplicacao(0, 10) == 0 
