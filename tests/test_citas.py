import pytest

from src.citas import calcular_copago


# Ejemplo de prueba (ya escrita para que vea el formato).
def test_particular_paga_todo():
    assert calcular_copago(100000, "particular") == 100000


# TDD 1: el afiliado contributivo paga el 10 % (con redondeo a 2 decimales).
def test_contributivo_paga_10_por_ciento():
    assert calcular_copago(100000, "contributivo") == 10000
    assert calcular_copago(33.33, "contributivo") == 3.33


# TDD 2: el afiliado subsidiado no paga nada.
def test_subsidiado_paga_cero():
    assert calcular_copago(100000, "subsidiado") == 0


# TDD 3: entradas inválidas lanzan ValueError.
def test_valores_invalidos_lanzan_error():
    with pytest.raises(ValueError):
        calcular_copago(-1, "particular")
    with pytest.raises(ValueError):
        calcular_copago(100000, "vip")

