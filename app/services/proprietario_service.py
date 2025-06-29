from app import db
from app.models.proprietario_model import Proprietario

def listar_proprietarios():
    return Proprietario.query.all()

def buscar_proprietario_por_id(id):
    return Proprietario.query.get_or_404(id)

def criar_proprietario(dados):
    proprietario = Proprietario(**dados)
    db.session.add(proprietario)
    db.session.commit()
    return proprietario

def atualizar_proprietario(proprietario, nome, email):
    proprietario.nome = nome
    proprietario.email = email
    db.session.commit()
    return proprietario

def deletar_proprietario(id):
    proprietario = buscar_proprietario_por_id(id)
    db.session.delete(proprietario)
    db.session.commit()
