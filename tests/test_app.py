import pytest
from src.app import adicionar_usuario, listar_usuarios, contar_usuarios, usuario_maior_que_18, usuarios
from src.app import saudacao

def test_saudacao():
    assert saudacao("Aline") == "Olá Aline! Bem-Vindo ao Python!!"


def setup_function():
    """Limpa a lista de usuários antes de cada teste."""
    usuarios.clear()

def test_adicionar_usuario():
    resultado = adicionar_usuario("Aline", 25)
    assert resultado == {"nome": "Aline", "idade": 25}
    assert contar_usuarios() == 1

def test_listar_usuarios():
    adicionar_usuario("Aline", 25)
    adicionar_usuario("Carlos", 17)
    assert listar_usuarios() == [{"nome": "Aline", "idade": 25}, {"nome": "Carlos", "idade": 17}]

def test_contar_usuarios():
    assert contar_usuarios() == 0
    adicionar_usuario("Aline", 25)
    assert contar_usuarios() == 1

def test_usuario_maior_que_18_true():
    adicionar_usuario("Aline", 25)
    assert usuario_maior_que_18("Aline") == True

def test_usuario_maior_que_18_false():
    adicionar_usuario("Carlos", 17)
    assert usuario_maior_que_18("Carlos") == False

def test_usuario_maior_que_18_nao_existente():
    assert usuario_maior_que_18("Bruno") == None
