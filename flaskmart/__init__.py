# imports
from flask import Flask
from .models import db
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__) # criando app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'  # configuração do banco de dados
app.config['SECRET_KEY'] = "eusouomaioral" # secret key obrigatória


class CSRRFProtect:
    pass


csrf = CSRFProtect()
db.init_app(app) # iniciando app

# importando routes
from . import routes
