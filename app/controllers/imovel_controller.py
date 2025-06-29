from flask import Blueprint, render_template, redirect, url_for, request
from app.services import imovel_service
from app.models.proprietario_model import Proprietario
from app.models.imobiliaria_model import Imobiliaria
from app.models.categoria_model import Categoria

imovel_bp = Blueprint('imoveis', __name__)

@imovel_bp.route('/')
def listar_imoveis():
    imoveis = imovel_service.listar_imoveis()
    return render_template('imoveis/imoveis.html', imoveis=imoveis)

@imovel_bp.route('/<int:id>')
def ver_imovel(id):
    imovel = imovel_service.buscar_imovel_por_id(id)
    return render_template('imoveis/imovel.html', imovel=imovel)

@imovel_bp.route('/deletar/<int:id>')
def deletar_imovel(id):
    imovel_service.deletar_imovel(id)
    return redirect(url_for('imoveis.listar_imoveis'))

@imovel_bp.route('/criar', methods=['GET', 'POST'])
def criar_imovel():
    if request.method == 'POST':
        dados = {
            'preco': float(request.form['preco']),
            'proprietario_id': int(request.form['proprietario_id']),
            'imobiliaria_id': int(request.form['imobiliaria_id']),
            'categoria_id': int(request.form['categoria_id'])
        }
        imovel_service.criar_imovel(dados)
        return redirect(url_for('imoveis.listar_imoveis'))

    proprietarios = Proprietario.query.all()
    imobiliarias = Imobiliaria.query.all()
    categorias = Categoria.query.all()
    return render_template('imoveis/imoveis-criar.html', proprietarios=proprietarios, imobiliarias=imobiliarias, categorias=categorias)

@imovel_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_imovel(id):
    imovel = imovel_service.buscar_imovel_por_id(id)

    if request.method == 'POST':
        dados = {
            'preco': float(request.form['preco']),
            'proprietario_id': int(request.form['proprietario_id']),
            'imobiliaria_id': int(request.form['imobiliaria_id']),
            'categoria_id': int(request.form['categoria_id'])
        }
        imovel_service.atualizar_imovel(imovel, dados)
        return redirect(url_for('imoveis.listar_imoveis'))

    proprietarios = Proprietario.query.all()
    imobiliarias = Imobiliaria.query.all()
    categorias = Categoria.query.all()
    return render_template('imoveis/imoveis-editar.html', imovel=imovel, proprietarios=proprietarios, imobiliarias=imobiliarias, categorias=categorias)
