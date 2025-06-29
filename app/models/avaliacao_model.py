from app import db

class Avaliacao(db.Model):
    __tablename__ = 'avaliacoes'

    id = db.Column(db.Integer, primary_key=True)
    nota = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.Text, nullable=True)

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    imovel_id = db.Column(db.Integer, db.ForeignKey('imoveis.id'), nullable=False)

    usuario = db.relationship("Usuario", backref="avaliacoes")
    imovel = db.relationship("Imovel", backref="avaliacoes")
