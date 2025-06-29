from app import db
from datetime import datetime

class Reclamacao(db.Model):
    __tablename__ = 'reclamacoes'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    imovel_id = db.Column(db.Integer, db.ForeignKey('imoveis.id'), nullable=False)

    usuario = db.relationship('Usuario', backref='reclamacoes')
    imovel = db.relationship('Imovel', backref='reclamacoes')