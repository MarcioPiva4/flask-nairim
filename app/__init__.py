import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

path = os.getcwd()

template_dir = os.path.join(path, 'templates')
print("Template path:", template_dir)

app = Flask(__name__, template_folder=template_dir)

app.config.from_object('config')

db = SQLAlchemy(app)


from app.models import imovel_model, proprietario_model, imobiliaria_model, categoria_model, usuario_model, favorito_model, visita_model, avaliacao_model, reclamacao_model

from app.services import imovel_service, proprietario_service, imobiliaria_service, categoria_service, usuario_service, favorito_service, visita_service, avaliacao_service, reclamacao_service

from app.controllers import imovel_controller, proprietario_controller, imobiliaria_controller, categoria_controller, usuario_controller, favorito_controller, visita_controller, avaliacao_controller, reclamacao_controller

app.register_blueprint(imovel_controller.imovel_bp, url_prefix='/imoveis')
app.register_blueprint(proprietario_controller.proprietarios_bp , url_prefix='/proprietarios')
app.register_blueprint(imobiliaria_controller.imobiliaria_bp, url_prefix='/imobiliarias')
app.register_blueprint(categoria_controller.categoria_bp, url_prefix='/categorias')
app.register_blueprint(usuario_controller.usuarios_bp, url_prefix='/usuarios')
app.register_blueprint(favorito_controller.favoritos_bp, url_prefix='/favoritos')
app.register_blueprint(visita_controller.visita_bp, url_prefix='/visitas')
app.register_blueprint(avaliacao_controller.avaliacao_bp, url_prefix='/avaliacoes')
app.register_blueprint(reclamacao_controller.reclamacao_bp, url_prefix='/reclamacoes')

from app.controllers import home_controller
app.register_blueprint(home_controller.home_bp)

with app.app_context():
    db.create_all()
