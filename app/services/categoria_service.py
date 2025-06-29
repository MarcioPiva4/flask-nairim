from app.models.categoria_model import Categoria
from app import db

def get_todas_categorias():
    return Categoria.query.all()

def get_categoria_por_id(id):
    return Categoria.query.get_or_404(id)

def criar_categoria(nome):
    nova = Categoria(nome=nome)
    db.session.add(nova)
    db.session.commit()
    return nova

def criar_categoria_completo(nome, descricao):
    nova = Categoria(nome=nome, descricao=descricao)
    db.session.add(nova)
    db.session.commit()
    return nova

def deletar_categoria(id):
    categoria = get_categoria_por_id(id)
    db.session.delete(categoria)
    db.session.commit()

def atualizar_categoria(categoria, novo_nome, nova_descricao):
    categoria.nome = novo_nome
    categoria.descricao = nova_descricao
    db.session.commit()
    return categoria
