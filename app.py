from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.models import db
from controllers.funcionario import funcionario_bp
from controllers.cliente import cliente_bp
from controllers.servico import servicos_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://melo172n:12345@localhost/gestaotecnochip'

db.init_app(app)

app.register_blueprint(funcionario_bp)
app.register_blueprint(cliente_bp)
app.register_blueprint(servicos_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)