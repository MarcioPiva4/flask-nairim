from app import db
from app.models.usuario_model import Usuario

def listar_usuarios():
    return Usuario.query.all()

def buscar_usuario(id):
    return Usuario.query.get(id)

def criar_usuario(nome, email, senha, tipo):
    novo_usuario = Usuario(nome=nome, email=email, senha=senha, tipo=tipo)
    db.session.add(novo_usuario)
    db.session.commit()
    return novo_usuario

def atualizar_usuario(usuario, nome, email, senha, tipo):
    usuario.nome = nome
    usuario.email = email
    usuario.senha = senha
    usuario.tipo = tipo
    db.session.commit()
    return usuario

def deletar_usuario(usuario):
    db.session.delete(usuario)
    db.session.commit()
