from app import db
from app.models.imovel_model import Imovel

def listar_imoveis():
    return Imovel.query.all()

def buscar_imovel_por_id(id):
    return Imovel.query.get_or_404(id)

def criar_imovel(dados):
    imovel = Imovel(**dados)
    db.session.add(imovel)
    db.session.commit()
    return imovel

def deletar_imovel(id):
    imovel = buscar_imovel_por_id(id)
    db.session.delete(imovel)
    db.session.commit()

def atualizar_imovel(imovel, dados):
    imovel.preco = dados['preco']
    imovel.proprietario_id = dados['proprietario_id']
    imovel.imobiliaria_id = dados['imobiliaria_id']
    imovel.categoria_id = dados['categoria_id']
    db.session.commit()
    return imovel
