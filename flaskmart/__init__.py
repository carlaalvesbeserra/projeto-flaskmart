from flask import Flask
from .models import db
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'  # Configuração do banco de dados
app.config['SECRET_KEY'] = "eusouomaioral"


class CSRRFProtect:
    pass


csrf = CSRFProtect()
db.init_app(app)

from . import routes
