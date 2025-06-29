from flask import Blueprint, render_template, redirect, url_for, request
from app.services import imobiliaria_service

imobiliaria_bp = Blueprint('imobiliarias', __name__)

@imobiliaria_bp.route('/')
def listar_imobiliarias():
    imobiliarias = imobiliaria_service.listar_imobiliarias()
    return render_template('imobiliarias/imobiliarias.html', imobiliarias=imobiliarias)

@imobiliaria_bp.route('/<int:id>')
def ver_imobiliaria(id):
    imobiliaria = imobiliaria_service.buscar_imobiliaria_por_id(id)
    return render_template('imobiliarias/imobiliaria.html', imobiliaria=imobiliaria)

@imobiliaria_bp.route('/deletar/<int:id>')
def deletar_imobiliaria(id):
    imobiliaria_service.deletar_imobiliaria(id)
    return redirect(url_for('imobiliarias.listar_imobiliarias'))

@imobiliaria_bp.route('/criar', methods=['GET', 'POST'])
def criar_imobiliaria():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        dados = {'nome': nome, 'telefone': telefone}
        imobiliaria_service.criar_imobiliaria(dados)
        return redirect(url_for('imobiliarias.listar_imobiliarias'))

    return render_template('imobiliarias/imobiliaria-criar.html')

@imobiliaria_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_imobiliaria(id):
    imobiliaria = imobiliaria_service.buscar_imobiliaria_por_id(id)

    if request.method == 'POST':
        novo_nome = request.form['nome']
        novo_telefone = request.form['telefone']
        imobiliaria_service.atualizar_imobiliaria(imobiliaria, novo_nome, novo_telefone)
        return redirect(url_for('imobiliarias.listar_imobiliarias', id=imobiliaria.id))

    return render_template('imobiliarias/imobiliaria-editar.html', imobiliaria=imobiliaria)
