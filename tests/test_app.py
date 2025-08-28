# tests/test_app.py
from app import saudacao

def test_saudacao():
    assert saudacao("Aline") == "Olá Aline! Bem-Vindo ao Python!!"