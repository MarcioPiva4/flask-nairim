from app import db

class Favorito(db.Model):
    __tablename__ = 'favoritos'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    imovel_id = db.Column(db.Integer, db.ForeignKey('imoveis.id'), nullable=False)

    usuario = db.relationship('Usuario', backref=db.backref('favoritos', lazy=True))
    imovel = db.relationship('Imovel', backref=db.backref('favoritos', lazy=True))