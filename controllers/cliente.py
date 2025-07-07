from flask import Blueprint, render_template, request, redirect, url_for
from models.models import db, Cliente

cliente_bp = Blueprint('cliente', __name__, "url_prefix/cliente")

@cliente_bp.route("/")
def listar_clientes():
    clientes = Cliente.query.all()
    return render_template("cliente_list.html", clientes = clientes)

@cliente_bp.route("/criar-cliente", methods = ["GET", "POST"])
def criar_cliente():
    if request.method == "POST":
        nome_cliente = request.form["nome"]
        telefone_cliente = request.form["telefone"]
        cliente = Cliente(nome = nome_cliente, telefone = telefone_cliente)
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for("cliente.criar_cliente"))
    return render_template("cliente_form.html")

@cliente_bp.route("/deletar-cliente", methods = ["GET", "POST"])
def deletar_cliente():
    if request.method == "POST":
        cliente = Cliente.query.all(id)
        db.session.delete(cliente)
        db.session.commit()
        return redirect(url_for("cliente.deletar_cliente"))
    return render_template("cliente_form.html")

@cliente_bp.route("/modificar-cliente", methods = ["GET", "POST"])
def modificar_cliente():
    if request.method == "POST":
        cliente = Cliente.query.all(id)
        cliente.nome = request.form["nome"]
        cliente.telefone = request.form["telefone"]
        db.session.commit()
        return redirect(url_for("cliente.modificar_cliente"))
    return render_template("cliente_form.html")


        
