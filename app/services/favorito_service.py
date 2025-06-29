from app import db
from app.models.favorito_model import Favorito

def listar_favoritos():
    return Favorito.query.all()

def obter_favorito_por_id(id):
    return Favorito.query.get(id)

def criar_favorito(usuario_id, imovel_id):
    favorito = Favorito(usuario_id=usuario_id, imovel_id=imovel_id)
    db.session.add(favorito)
    db.session.commit()
    return favorito

def atualizar_favorito(id, usuario_id, imovel_id):
    favorito = Favorito.query.get(id)
    if favorito:
        favorito.usuario_id = usuario_id
        favorito.imovel_id = imovel_id
        db.session.commit()
    return favorito

def deletar_favorito(id):
    favorito = Favorito.query.get(id)
    if favorito:
        db.session.delete(favorito)
        db.session.commit()
