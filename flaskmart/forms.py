from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class CadastroProdutos(FlaskForm):
    nome = StringField("Nome:", validators=[DataRequired()])
    quantidade = IntegerField("Quantidade:", validators=[DataRequired(), NumberRange(min(0, 1000))])
    preco = FloatField("Preço(un):", validators=[DataRequired(), NumberRange(0, 1000)])
    botao = SubmitField("Adicionar Produto")
