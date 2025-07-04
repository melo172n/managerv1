from flask_sqlalchemy import SQLAlchemy
import enum
from sqlalchemy import Enum

db = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(100), nullable=False)

class StatusOrdem(enum.Enum):
    EM_ANDAMENTO = "em andamento"
    CONCLUIDO = "concluído"
    PAUSADO = "pausado"

class Servicos(db.Model):
    __tablename__ = 'servicos'
    id = db.Column(db.Integer, primary_key=True)
    servico = db.Column(db.String, nullable=False)
    descricao = db.Column(db.String, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    status = db.Column(Enum(StatusOrdem), nullable=False, default=StatusOrdem.EM_ANDAMENTO)
    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionarios.id'))
    
class Funcionario(db.Model):
    __tablename__ = 'funcionarios'
    id = db.Column(db.Integer, primary_key=True)
    nome_funcionario = db.Column(db.String, nullable=False)
    saldo_funcionario = db.Column(db.Float, default=0.0)
    telefone_funcionario = db.Column(db.String(100), nullable=False)

    servicos = db.relationship('Servicos', backref='funcionario', lazy=True)
