from flask import Blueprint, render_template, request, redirect, url_for
from models.models import db, Servicos

servicos_bp = Blueprint('servicos', __name__, url_prefix="/servicos")

@servicos_bp.route("/")
def listar():
    servicos = Servicos.query.all()
    return render_template("servicos_list.html", servicos = servicos)

@servicos_bp.route("/criar-servico", methods=["GET", "POST"])
def criar_servico():
    if request.method == "POST":
        servico_a_ser_feito = request.form["servico"]
        descricao = request.form["descricao"]
        preco = request.form["preco"]
        servico = Servicos(servico = servico_a_ser_feito, descricao = descricao, preco = preco)
        db.session.add(servico)
        db.session.commit()
        return redirect(url_for("servicos.criar_servico"))
    return render_template("servicos_form.html")

@servicos_bp.route("/deletar-servico", methods=["GET", "POST"])
def deletar_servico():
    if request.method == "POST":
        servico = Servicos.query.all(id)
        db.session.delete(servico)
        db.session.commit()
        return redirect(url_for("servicos.deletar_servico"))
    return render_template("servicos_form.html")

@servicos_bp.route("/editar-servico", methods=["GET", "POST"])
def editar_servico():
    if request.method == "POST":
        servico = Servicos.query.all(id)
        servico.servico_a_ser_feito = request.form["servico"]
        servico.descricao = request.form["descricao"]
        servico.preco = float(request.form["preco"])
        servico.status = request.form["status"]
        db.session.commit()
        return redirect(url_for("servicos.editar_servico"))
    return render_template("servicos_form.html")
