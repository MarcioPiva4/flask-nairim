from app import db
from flask import Blueprint, render_template, jsonify, send_file
from app.models.imovel_model import Imovel
from app.models.imobiliaria_model import Imobiliaria
from app.models.categoria_model import Categoria
from app.models.usuario_model import Usuario
from app.models.proprietario_model import Proprietario
from app.models.visita_model import Visita
from sqlalchemy import func
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return render_template('home.html')

@home_bp.route('/api/dashboard-data')
def dashboard_data():
    imoveis_por_categoria = (
        db.session.query(Categoria.nome, func.count(Imovel.id))
        .join(Imovel, Imovel.categoria_id == Categoria.id)
        .group_by(Categoria.nome)
        .all()
    )

    imoveis_por_imobiliaria = (
        db.session.query(Imobiliaria.nome, func.count(Imovel.id))
        .join(Imovel, Imovel.imobiliaria_id == Imobiliaria.id)
        .group_by(Imobiliaria.nome)
        .all()
    )

    preco_medio_por_imobiliaria = (
        db.session.query(Imobiliaria.nome, func.avg(Imovel.preco))
        .join(Imovel, Imovel.imobiliaria_id == Imobiliaria.id)
        .group_by(Imobiliaria.nome)
        .all()
    )

    usuarios_por_tipo = (
        db.session.query(Usuario.tipo, func.count(Usuario.id))
        .group_by(Usuario.tipo)
        .all()
    )

    imoveis_por_proprietario = (
        db.session.query(Proprietario.nome, func.count(Imovel.id))
        .join(Imovel, Imovel.proprietario_id == Proprietario.id)
        .group_by(Proprietario.nome)
        .all()
    )

    visitas_por_imovel = (
        db.session.query(Imovel.id, func.count(Visita.id))
        .join(Visita, Visita.imovel_id == Imovel.id)
        .group_by(Imovel.id)
        .all()
    )

    visitas_por_usuario = (
        db.session.query(Usuario.nome, func.count(Visita.id))
        .join(Visita, Visita.usuario_id == Usuario.id)
        .group_by(Usuario.nome)
        .all()
    )

    return jsonify({
        "imoveis_por_categoria": [
            {"categoria": nome, "total": total}
            for nome, total in imoveis_por_categoria
        ],
        "imoveis_por_imobiliaria": [
            {"imobiliaria": nome, "total": total}
            for nome, total in imoveis_por_imobiliaria
        ],
        "preco_medio_por_imobiliaria": [
            {"imobiliaria": nome, "preco_medio": round(preco, 2) if preco else 0}
            for nome, preco in preco_medio_por_imobiliaria
        ],
        "usuarios_por_tipo": [
            {"tipo": tipo, "total": total}
            for tipo, total in usuarios_por_tipo
        ],
        "imoveis_por_proprietario": [
            {"proprietario": nome, "total": total}
            for nome, total in imoveis_por_proprietario
        ],
        "visitas_por_imovel": [
            {"imovel": f"Imovel {i}", "total": t}
            for i, t in visitas_por_imovel
        ],
        "visitas_por_usuario": [
            {"usuario": nome, "total": total}
            for nome, total in visitas_por_usuario
        ],
    })


@home_bp.route("/gerar-relatorio-pdf")
def gerar_relatorio_pdf():
    # 🔹 Consultas do banco
    imoveis_por_categoria = (
        db.session.query(Categoria.nome, func.count(Imovel.id))
        .join(Imovel, Imovel.categoria_id == Categoria.id)
        .group_by(Categoria.nome)
        .all()
    )

    imoveis_por_imobiliaria = (
        db.session.query(Imobiliaria.nome, func.count(Imovel.id))
        .join(Imovel, Imovel.imobiliaria_id == Imobiliaria.id)
        .group_by(Imobiliaria.nome)
        .all()
    )

    preco_medio_por_imobiliaria = (
        db.session.query(Imobiliaria.nome, func.avg(Imovel.preco))
        .join(Imovel, Imovel.imobiliaria_id == Imobiliaria.id)
        .group_by(Imobiliaria.nome)
        .all()
    )

    usuarios_por_tipo = (
        db.session.query(Usuario.tipo, func.count(Usuario.id))
        .group_by(Usuario.tipo)
        .all()
    )

    imoveis_por_proprietario = (
        db.session.query(Proprietario.nome, func.count(Imovel.id))
        .join(Imovel, Imovel.proprietario_id == Proprietario.id)
        .group_by(Proprietario.nome)
        .all()
    )

    visitas_por_imovel = (
        db.session.query(Imovel.id, func.count(Visita.id))
        .join(Visita, Visita.imovel_id == Imovel.id)
        .group_by(Imovel.id)
        .all()
    )

    visitas_por_usuario = (
        db.session.query(Usuario.nome, func.count(Visita.id))
        .join(Visita, Visita.usuario_id == Usuario.id)
        .group_by(Usuario.nome)
        .all()
    )

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    largura, altura = A4
    y = altura - 50

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, y, "Relatorio de Dados - Nairim Holding")
    pdf.setFont("Helvetica", 10)
    pdf.drawString(50, y - 20, f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}")

    y -= 60

    def add_section(title, data):
        nonlocal y
        pdf.setFont("Helvetica-Bold", 13)
        pdf.drawString(50, y, title)
        pdf.setFont("Helvetica", 11)
        y -= 20
        for linha in data:
            if y < 80:
                pdf.showPage()
                y = altura - 50
                pdf.setFont("Helvetica-Bold", 13)
                pdf.drawString(50, y, title)
                pdf.setFont("Helvetica", 11)
                y -= 20
            pdf.drawString(60, y, linha)
            y -= 15
        y -= 20

    add_section("Imoveis por Categoria", [f"- {nome}: {total}" for nome, total in imoveis_por_categoria])
    add_section("Imoveis por Imobiliaria", [f"- {nome}: {total}" for nome, total in imoveis_por_imobiliaria])
    add_section("Preco Medio por Imobiliaria", [f"- {nome}: R$ {round(preco, 2) if preco else 0}" for nome, preco in preco_medio_por_imobiliaria])
    add_section("Usuarios por Tipo", [f"- {tipo}: {total}" for tipo, total in usuarios_por_tipo])
    add_section("Imoveis por Proprietario", [f"- {nome}: {total}" for nome, total in imoveis_por_proprietario])
    add_section("Visitas por Imovel", [f"- Imovel {i}: {t}" for i, t in visitas_por_imovel])
    add_section("Visitas por Usuario", [f"- {nome}: {total}" for nome, total in visitas_por_usuario])

    pdf.showPage()
    pdf.save()
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="relatorio_nairim.pdf",
        mimetype="application/pdf"
    )
