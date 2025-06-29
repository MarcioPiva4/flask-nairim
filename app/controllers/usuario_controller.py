from flask import Blueprint, render_template, request, redirect, url_for
from app.services import usuario_service

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/')
def listar_usuarios():
    usuarios = usuario_service.listar_usuarios()
    return render_template('usuarios/usuarios.html', usuarios=usuarios)

@usuarios_bp.route('/<int:id>')
def ver_usuario(id):
    usuario = usuario_service.buscar_usuario(id)
    return render_template('usuarios/usuario.html', usuario=usuario)

@usuarios_bp.route('/criar', methods=['GET', 'POST'])
def criar_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        tipo = request.form['tipo']
        usuario_service.criar_usuario(nome, email, senha, tipo)
        return redirect(url_for('usuarios.listar_usuarios'))
    return render_template('usuarios/usuario-criar.html')

@usuarios_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar_usuario(id):
    usuario = usuario_service.buscar_usuario(id)
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        tipo = request.form['tipo']
        usuario_service.atualizar_usuario(usuario, nome, email, senha, tipo)
        return redirect(url_for('usuarios.ver_usuario', id=usuario.id))
    return render_template('usuarios/usuario-editar.html', usuario=usuario)

@usuarios_bp.route('/<int:id>/deletar')
def deletar_usuario(id):
    usuario = usuario_service.buscar_usuario(id)
    usuario_service.deletar_usuario(usuario)
    return redirect(url_for('usuarios.listar_usuarios'))
