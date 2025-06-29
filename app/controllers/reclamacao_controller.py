from flask import Blueprint, render_template, request, redirect, url_for
from app.services import reclamacao_service
from app.models.usuario_model import Usuario
from app.models.imovel_model import Imovel

reclamacao_bp = Blueprint('reclamacoes', __name__, url_prefix='/reclamacoes')

@reclamacao_bp.route('/')
def listar_reclamacoes():
    reclamacoes = reclamacao_service.listar_reclamacoes()
    return render_template('reclamacoes/reclamacoes.html', reclamacoes=reclamacoes)

@reclamacao_bp.route('/<int:id>')
def ver_reclamacao(id):
    reclamacao = reclamacao_service.buscar_reclamacao_por_id(id)
    return render_template('reclamacoes/reclamacao.html', reclamacao=reclamacao)

@reclamacao_bp.route('/criar', methods=['GET', 'POST'])
def criar_reclamacao():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        usuario_id = request.form['usuario_id']
        imovel_id = request.form['imovel_id']
        reclamacao_service.criar_reclamacao(titulo, descricao, usuario_id, imovel_id)
        return redirect(url_for('reclamacoes.listar_reclamacoes'))
    
    usuarios = Usuario.query.all()
    imoveis = Imovel.query.all()
    return render_template('reclamacoes/reclamacao-criar.html', usuarios=usuarios, imoveis=imoveis)

@reclamacao_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar_reclamacao(id):
    reclamacao = reclamacao_service.buscar_reclamacao_por_id(id)
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        usuario_id = request.form['usuario_id']
        imovel_id = request.form['imovel_id']
        reclamacao_service.atualizar_reclamacao(reclamacao, titulo, descricao, usuario_id, imovel_id)
        return redirect(url_for('reclamacoes.listar_reclamacoes'))

    usuarios = Usuario.query.all()
    imoveis = Imovel.query.all()
    return render_template('reclamacoes/reclamacao-editar.html', reclamacao=reclamacao, usuarios=usuarios, imoveis=imoveis)

@reclamacao_bp.route('/<int:id>/deletar')
def deletar_reclamacao(id):
    reclamacao = reclamacao_service.buscar_reclamacao_por_id(id)
    reclamacao_service.deletar_reclamacao(reclamacao)
    return redirect(url_for('reclamacoes.listar_reclamacoes'))
