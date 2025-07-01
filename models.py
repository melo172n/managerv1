from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(100), nullable=False)

class Servicos(db.Model):
    __tablename__ = 'servicos'
    id = db.Column(db.Integer, primary_key=True)
    servico = db.Column(db.String, nullable=False)
    descricao = db.Column(db.String, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    status = db.Column(db.String, nullable = False)

    

class Funcionarios(db.Model):
    __tablename__ = 'funcionarios'
    id = db.Column(db.Integer, primary_key=True)
    nome_funcionario = db.Column(db.String, nullable=False)
    saldo_funcionario = db.Column(db.Float, default=0.0)

    servicos = db.relationship('Servico', backref='funcionario', lazy=True)