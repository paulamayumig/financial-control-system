from src.validators import pedir_valor


def test_pedir_valor(monkeypatch):

    entradas = iter(["-10", "100"])

    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    resultado = pedir_valor()

    assert resultado == 100