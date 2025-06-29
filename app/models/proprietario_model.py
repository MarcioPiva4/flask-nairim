from app import db

class Proprietario(db.Model):
    __tablename__ = 'proprietarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), unique=True)
    
    imoveis = db.relationship('Imovel', backref='proprietario', lazy=True)
