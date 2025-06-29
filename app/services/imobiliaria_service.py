from app import db
from app.models.imobiliaria_model import Imobiliaria

def listar_imobiliarias():
    return Imobiliaria.query.all()

def buscar_imobiliaria_por_id(id):
    return Imobiliaria.query.get_or_404(id)

def criar_imobiliaria(dados):
    imobiliaria = Imobiliaria(**dados)
    db.session.add(imobiliaria)
    db.session.commit()
    return imobiliaria

def deletar_imobiliaria(id):
    imobiliaria = buscar_imobiliaria_por_id(id)
    db.session.delete(imobiliaria)
    db.session.commit()

def atualizar_imobiliaria(imobiliaria, nome, telefone):
    imobiliaria.nome = nome
    imobiliaria.telefone = telefone
    db.session.commit()
    return imobiliaria
