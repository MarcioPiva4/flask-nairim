from app import db
from app.models.reclamacao_model import Reclamacao

def listar_reclamacoes():
    return Reclamacao.query.all()

def buscar_reclamacao_por_id(id):
    return Reclamacao.query.get_or_404(id)

def criar_reclamacao(titulo, descricao, usuario_id, imovel_id):
    nova_reclamacao = Reclamacao(
        titulo=titulo,
        descricao=descricao,
        usuario_id=usuario_id,
        imovel_id=imovel_id
    )
    db.session.add(nova_reclamacao)
    db.session.commit()
    return nova_reclamacao

def atualizar_reclamacao(reclamacao, titulo, descricao, usuario_id, imovel_id):
    reclamacao.titulo = titulo
    reclamacao.descricao = descricao
    reclamacao.usuario_id = usuario_id
    reclamacao.imovel_id = imovel_id
    db.session.commit()
    return reclamacao

def deletar_reclamacao(reclamacao):
    db.session.delete(reclamacao)
    db.session.commit()
