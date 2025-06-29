from flask import Blueprint, render_template, redirect, url_for, request
from app.services import proprietario_service

proprietarios_bp = Blueprint('proprietarios', __name__)

@proprietarios_bp.route('/')
def listar_proprietarios():
    proprietarios = proprietario_service.listar_proprietarios()
    return render_template('proprietarios/proprietarios.html', proprietarios=proprietarios)

@proprietarios_bp.route('/<int:id>')
def ver_proprietario(id):
    proprietario = proprietario_service.buscar_proprietario_por_id(id)
    return render_template('proprietarios/proprietario.html', proprietario=proprietario)

@proprietarios_bp.route('/deletar/<int:id>')
def deletar_proprietario(id):
    proprietario_service.deletar_proprietario(id)
    return redirect(url_for('proprietarios.listar_proprietarios'))

@proprietarios_bp.route('/criar', methods=['GET', 'POST'])
def criar_proprietario():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        dados = {'nome': nome, 'cpf': cpf}
        proprietario_service.criar_proprietario(dados)
        return redirect(url_for('proprietarios.listar_proprietarios'))

    return render_template('proprietarios/proprietario-criar.html')

@proprietarios_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_proprietario(id):
    proprietario = proprietario_service.buscar_proprietario_por_id(id)

    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        proprietario_service.atualizar_proprietario(proprietario, nome, email)
        return redirect(url_for('proprietarios.ver_proprietario', id=proprietario.id))

    return render_template('proprietarios/proprietario-editar.html', proprietario=proprietario)
