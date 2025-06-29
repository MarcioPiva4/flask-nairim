from app import db
from datetime import datetime

class Visita(db.Model):
    __tablename__ = 'visitas'

    id = db.Column(db.Integer, primary_key=True)
    data_hora = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    observacoes = db.Column(db.String(300))

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    imovel_id = db.Column(db.Integer, db.ForeignKey('imoveis.id'), nullable=False)

    usuario = db.relationship('Usuario', backref='visitas')
    imovel = db.relationship('Imovel', backref='visitas')

    def __repr__(self):
        return f"<Visita {self.id}>"
