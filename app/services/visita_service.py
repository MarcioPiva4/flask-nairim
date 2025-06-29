from app.models.visita_model import Visita
from app import db

def listar_visitas():
    return Visita.query.all()

def buscar_visita_por_id(id):
    return Visita.query.get(id)

def criar_visita(data_hora, observacoes, usuario_id, imovel_id):
    nova_visita = Visita(
        data_hora=data_hora,
        observacoes=observacoes,
        usuario_id=usuario_id,
        imovel_id=imovel_id
    )
    db.session.add(nova_visita)
    db.session.commit()
    return nova_visita

def atualizar_visita(visita, data_hora, observacoes, usuario_id, imovel_id):
    visita.data_hora = data_hora
    visita.observacoes = observacoes
    visita.usuario_id = usuario_id
    visita.imovel_id = imovel_id
    db.session.commit()
    return visita

def deletar_visita(visita):
    db.session.delete(visita)
    db.session.commit()
