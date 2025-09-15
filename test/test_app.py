# test/test_app.py
from src.app import saudacao

def test_saudacao():
    assert saudacao("Aline") == "Olá Aline! Bem-Vindo ao Python!!"