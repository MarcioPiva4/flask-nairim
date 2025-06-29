from flask import Blueprint, render_template, request, redirect, url_for
from app.services import avaliacao_service
from app.models.usuario_model import Usuario
from app.models.imovel_model import Imovel
from app.models.avaliacao_model import Avaliacao

avaliacao_bp = Blueprint("avaliacoes", __name__, url_prefix="/avaliacoes")

@avaliacao_bp.route("/")
def listar_avaliacoes():
    avaliacoes = avaliacao_service.listar_avaliacoes()
    return render_template("avaliacoes/avaliacoes.html", avaliacoes=avaliacoes)

@avaliacao_bp.route("/<int:id>")
def ver_avaliacao(id):
    avaliacao = avaliacao_service.buscar_avaliacao_por_id(id)
    return render_template("avaliacoes/avaliacao.html", avaliacao=avaliacao)

@avaliacao_bp.route("/criar", methods=["GET", "POST"])
def criar_avaliacao():
    if request.method == "POST":
        avaliacao_service.criar_avaliacao(request.form)
        return redirect(url_for("avaliacoes.listar_avaliacoes"))
    usuarios = Usuario.query.all()
    imoveis = Imovel.query.all()
    return render_template("avaliacoes/avaliacao-criar.html", usuarios=usuarios, imoveis=imoveis)

@avaliacao_bp.route("/<int:id>/editar", methods=["GET", "POST"])
def editar_avaliacao(id):
    avaliacao = avaliacao_service.buscar_avaliacao_por_id(id)
    if request.method == "POST":
        nota = request.form["nota"]
        comentario = request.form.get("comentario")
        usuario_id = request.form["usuario_id"]
        imovel_id = request.form["imovel_id"]
        avaliacao_service.atualizar_avaliacao(avaliacao, nota, comentario, usuario_id, imovel_id)
        return redirect(url_for("avaliacoes.listar_avaliacoes"))
    usuarios = Usuario.query.all()
    imoveis = Imovel.query.all()
    return render_template("avaliacoes/avaliacao-editar.html", avaliacao=avaliacao, usuarios=usuarios, imoveis=imoveis)

@avaliacao_bp.route("/<int:id>/deletar")
def deletar_avaliacao(id):
    avaliacao_service.deletar_avaliacao(id)
    return redirect(url_for("avaliacoes.listar_avaliacoes"))
