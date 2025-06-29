from flask import Blueprint, render_template, request, redirect, url_for
from app.services import visita_service
from datetime import datetime
from app.models.usuario_model import Usuario
from app.models.imovel_model import Imovel
from app.models.visita_model import Visita

visita_bp = Blueprint("visitas", __name__, url_prefix="/visitas")

@visita_bp.route("/")
def listar_visitas():
    visitas = visita_service.listar_visitas()
    return render_template("visitas/visitas.html", visitas=visitas)

@visita_bp.route("/<int:id>")
def ver_visita(id):
    visita = visita_service.buscar_visita_por_id(id)
    return render_template("visitas/visita.html", visita=visita)

@visita_bp.route("/criar", methods=["GET", "POST"])
def criar_visita():
    if request.method == 'POST':
        data_hora = datetime.strptime(request.form['data_hora'], "%Y-%m-%dT%H:%M")
        observacoes = request.form['observacoes']
        usuario_id = int(request.form['usuario_id'])
        imovel_id = int(request.form['imovel_id'])

        visita_service.criar_visita(data_hora, observacoes, usuario_id, imovel_id)
        return redirect(url_for("visitas.listar_visitas"))
    usuarios = Usuario.query.all()
    imoveis = Imovel.query.all()
    return render_template('visitas/visita-criar.html', usuarios=usuarios, imoveis=imoveis)

@visita_bp.route("/<int:id>/editar", methods=["GET", "POST"])
def editar_visita(id):
    visita = Visita.query.get_or_404(id)
    if request.method == 'POST':
        data_hora_str = request.form['data_hora']
        observacoes = request.form['observacoes']
        usuario_id = int(request.form['usuario_id'])
        imovel_id = int(request.form['imovel_id'])

        data_hora = datetime.strptime(data_hora_str, "%Y-%m-%dT%H:%M")

        visita_service.atualizar_visita(visita, data_hora, observacoes, usuario_id, imovel_id)
        return redirect(url_for('visitas.listar_visitas'))
    usuarios = Usuario.query.all()
    imoveis = Imovel.query.all()
    return render_template('visitas/visita-editar.html', visita=visita, usuarios=usuarios, imoveis=imoveis)

@visita_bp.route("/<int:id>/deletar")
def deletar_visita(id):
    visita = visita_service.buscar_visita_por_id(id)
    visita_service.deletar_visita(visita)
    return redirect(url_for("visitas.listar_visitas"))
