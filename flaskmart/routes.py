# imports
from flaskmart import app, db
from flask import Flask, render_template, redirect, url_for
from flaskmart.forms import CadastroProdutos
from flaskmart.models import Produto, db


@app.route("/", methods=["GET", "POST"])
def homepage():
    form = CadastroProdutos()
    if form.validate_on_submit(): # só acontece se o usuário apertar no botão submit
        novo_produto = Produto(nome=form.nome.data, quantidade=form.quantidade.data, preco=form.preco.data)
        db.session.add(novo_produto)
        db.session.commit()
        return redirect(url_for("lista_produtos"))

    return render_template("homepage.html", form=form)


@app.route("/lista_produtos")
def lista_produtos():
    produtos = Produto.query.all() # procurando produtos
    return render_template("lista_produtos.html", produtos=produtos)
