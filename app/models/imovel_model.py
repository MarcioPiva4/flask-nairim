from app import db

class Imovel(db.Model):
    __tablename__ = 'imoveis'
    
    id = db.Column(db.Integer, primary_key=True)
    preco = db.Column(db.Float, nullable=False)
    
    proprietario_id = db.Column(db.Integer, db.ForeignKey('proprietarios.id'), nullable=False)
    imobiliaria_id = db.Column(db.Integer, db.ForeignKey('imobiliarias.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
