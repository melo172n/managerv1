from flask import Blueprint, render_template, request, redirect, url_for
from models.models import db, Funcionario


funcionario_bp = Blueprint('funcionario', __name__, url_prefix="/funcionarios")

@funcionario_bp.route("/")
def listar_funcionarios():
    funcionarios = Funcionario.query.all()
    return render_template("funcionario_list.html", funcionarios = funcionarios)

@funcionario_bp.route("/criar-funcionario", methods=["GET", "POST"])
def criar_funcionario():
    if request.method == "POST":
        nome_funcionario = request.form["nome"]
        saldo_funcionario = request.form["saldo"]
        telefone_funcionario = request.form["telefone"]
        funcionario = Funcionario(nome=nome_funcionario, saldo = saldo_funcionario, telefone = telefone_funcionario)
        db.session.add(funcionario)
        db.session.commit()
        return redirect(url_for("funcionario.listar"))
    return render_template("funcionario_form.html")

@funcionario_bp.route("/delete-funcionario", methods = ["GET", "POST"])
def deletar_funcionario(id):
    if request.method == "POST":
        funcionario = Funcionario.query.all(id)
        db.session.delete(funcionario)
        db.session.commit()
        return redirect(url_for("funcionario.listar.html"))
    return render_template("funcionario_form.html")

@funcionario_bp.route("/modificar-funcionario", methods = ["GET", "PUT"])
def modificar_funcionario(id):
    if request.method == "PUT":
        funcionario = Funcionario.query.all(id)
        funcionario.nome = request.form["nome"]
        funcionario.saldo = float(request.form["saldo"])
        db.session.commit()
        return redirect(url_for("funcionario.listar.html"))
    return render_template("funcionario_form.html")

