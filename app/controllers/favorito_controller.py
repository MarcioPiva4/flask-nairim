from flask import Blueprint, render_template, request, redirect, url_for
from app.services import favorito_service
from app.models.usuario_model import Usuario
from app.models.imovel_model import Imovel
from app import db

favoritos_bp = Blueprint('favoritos', __name__, url_prefix='/favoritos')

@favoritos_bp.route('/')
def listar_favoritos():
    favoritos = favorito_service.listar_favoritos()
    return render_template('favoritos/favoritos.html', favoritos=favoritos)

@favoritos_bp.route('/<int:id>')
def ver_favorito(id):
    favorito = favorito_service.obter_favorito_por_id(id)
    return render_template('favoritos/favorito.html', favorito=favorito)

@favoritos_bp.route('/criar', methods=['GET', 'POST'])
def criar_favorito():
    if request.method == 'POST':
        usuario_id = request.form['usuario_id']
        imovel_id = request.form['imovel_id']
        favorito_service.criar_favorito(usuario_id, imovel_id)
        return redirect(url_for('favoritos.listar_favoritos'))
    
    usuarios = Usuario.query.all()
    imoveis = Imovel.query.all()
    return render_template('favoritos/favorito-criar.html', usuarios=usuarios, imoveis=imoveis)

@favoritos_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_favorito(id):
    favorito = favorito_service.obter_favorito_por_id(id)
    if request.method == 'POST':
        usuario_id = request.form['usuario_id']
        imovel_id = request.form['imovel_id']
        favorito_service.atualizar_favorito(id, usuario_id, imovel_id)
        return redirect(url_for('favoritos.ver_favorito', id=id))
    
    usuarios = Usuario.query.all()
    imoveis = Imovel.query.all()
    return render_template('favoritos/favorito-editar.html', favorito=favorito, usuarios=usuarios, imoveis=imoveis)

@favoritos_bp.route('/deletar/<int:id>')
def deletar_favorito(id):
    favorito_service.deletar_favorito(id)
    return redirect(url_for('favoritos.listar_favoritos'))
