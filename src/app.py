# app.py

usuarios = []

def adicionar_usuario(nome, idade):
    """Adiciona um usuário ao sistema."""
    usuario = {"nome": nome, "idade": idade}
    usuarios.append(usuario)
    return usuario

def listar_usuarios():
    """Retorna todos os usuários cadastrados."""
    return usuarios

def contar_usuarios():
    """Retorna a quantidade de usuários cadastrados."""
    return len(usuarios)

def usuario_maior_que_18(nome):
    """Verifica se o usuário é maior de idade."""
    for u in usuarios:
        if u["nome"] == nome:
            return u["idade"] >= 18
    return None

if __name__ == "__main__":
    adicionar_usuario("Aline", 25)
    adicionar_usuario("Carlos", 17)
    print(listar_usuarios())
    print("Número de usuários:", contar_usuarios())
    print("Aline é maior de idade?", usuario_maior_que_18("Aline"))
