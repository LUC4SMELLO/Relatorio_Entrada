from flask import Blueprint, request, flash, redirect, url_for, render_template, session

from backend.models.usuarios import Usuario

from backend.validators.validar_cadastro import validar_cadastro


cadastro_bp = Blueprint("cadastro", __name__)

@cadastro_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    nome_completo = str(request.form.get("nome_completo")).rstrip()
    senha = str(request.form.get("senha")).rstrip()

    if request.method == "POST":

        valido, mensagem = validar_cadastro(nome_completo, senha)

        if not valido:
            flash(mensagem, "erro")
            return render_template("cadastro.html")
        
        else:

            novo_usuario = Usuario(nome_completo, senha)

            novo_usuario.inserir_usuario()

            session["username"] = nome_completo
            return redirect(url_for("selecionar_opcoes.selecionar_opcoes"))
        

        
    return render_template("cadastro.html")
