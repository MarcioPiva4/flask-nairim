from flask import Blueprint, render_template, request, redirect, url_for
from app.services import categoria_service
from app.models.categoria_model import Categoria

categoria_bp = Blueprint('categorias', __name__)

@categoria_bp.route('/')
def listar_categorias():
    categorias = categoria_service.get_todas_categorias()
    return render_template('categorias/categorias.html', categorias=categorias)

@categoria_bp.route('/<int:id>')
def ver_categoria(id):
    categoria = categoria_service.get_categoria_por_id(id)
    return render_template('categorias/categoria.html', categoria=categoria)

@categoria_bp.route('/criar', methods=['GET', 'POST'])
def criar_categoria():
    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        categoria_service.criar_categoria_completo(nome, descricao)
        return redirect(url_for('categorias.listar_categorias'))
    return render_template('categorias/categorias-criar.html')

@categoria_bp.route('/deletar/<int:id>')
def deletar_categoria(id):
    categoria_service.deletar_categoria(id)
    return redirect(url_for('categorias.listar_categorias'))

@categoria_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_categoria(id):
    categoria = categoria_service.get_categoria_por_id(id)

    if request.method == 'POST':
        novo_nome = request.form.get('nome')
        nova_descricao = request.form.get('descricao')
        categoria_service.atualizar_categoria(categoria, novo_nome, nova_descricao)
        return redirect(url_for('categorias.listar_categorias'))
    
    return render_template('categorias/categorias-editar.html', categoria=categoria)
