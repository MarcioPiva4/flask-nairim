from app import db

class Imobiliaria(db.Model):
    __tablename__ = 'imobiliarias'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20))
    
    imoveis = db.relationship('Imovel', backref='imobiliaria', lazy=True)
