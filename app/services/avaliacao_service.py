from app import db
from app.models.avaliacao_model import Avaliacao

def listar_avaliacoes():
    return Avaliacao.query.all()

def buscar_avaliacao_por_id(id):
    return Avaliacao.query.get_or_404(id)

def criar_avaliacao(form):
    avaliacao = Avaliacao(
        nota=form["nota"],
        comentario=form.get("comentario"),
        usuario_id=form["usuario_id"],
        imovel_id=form["imovel_id"]
    )
    db.session.add(avaliacao)
    db.session.commit()
    return avaliacao

def atualizar_avaliacao(avaliacao, nota, comentario, usuario_id, imovel_id):
    avaliacao.nota = nota
    avaliacao.comentario = comentario
    avaliacao.usuario_id = usuario_id
    avaliacao.imovel_id = imovel_id
    db.session.commit()
    return avaliacao

def deletar_avaliacao(id):
    avaliacao = buscar_avaliacao_por_id(id)
    db.session.delete(avaliacao)
    db.session.commit()
